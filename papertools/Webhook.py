import os
import requests
from .File import File
from typing import Union


class Webhook:
    '''Simple Class for interacting with Discord Webhooks'''

    def __init__(self, url: str, name: Union[str, None] = None, image: Union[str, None] = None) -> None:
        self.url: str = url
        self.name: Union[str, None] = name
        self.image: Union[str, None] = image

    def send(self, msg: str, name: Union[str, None] = None, image: Union[str, None] = None) -> requests.Response:
        '''Sends a message to the webhook'''
        if name == None:
            name = self.name
        if image == None:
            image = self.image

        data: dict = {
            'content': msg,
            'username': name,
            'avatar_url': image
        }
        return requests.post(self.url, json=data)

    def send_file(self, path: str, name: Union[str, None] = None, image: Union[str, None] = None) -> int:
        '''Sends a file to the webhook'''
        if name == None:
            name = self.name
        if image == None:
            image = self.image

        data = {
            'username': name,
            'avatar_url': image
        }

        response: requests.Response = requests.post(
            self.url, json=data, files={
                'file': (os.path.basename(path), File(path).read_b())})

        try:
            if int(response.json().get('code')) == 40005:
                print("<<<Datei zu groß für Discord>>>")
                return 0
        except TypeError:
            pass
        return response.status_code
