import requests
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

        data = {
            'content': msg,
            'username': name,
            'avatar_url': image
        }
        return requests.post(self.url, json=data)
