import requests


class Ollama:
    '''Simple wrapper for the Ollama API'''

    def __init__(self, model: str, url: str = 'http://127.0.0.1:11434', temperature: float = 1, system: str = '') -> None:
        self.url: str = url
        self.chat: str = f'{url}/api/chat'
        self.model: str = model
        self.temperature: float = temperature
        self.system: str = system
        self.messages: list[dict[str, str]] = []
        if self.system != '':
            self.messages.append({'role': 'system', 'content': self.system})

    def single(self, inp: str) -> str:
        '''Sends the input without any history to the AI and returns the response'''
        return requests.post(self.chat,
                             json={'messages': [{'role': 'system', 'content': self.system},
                                                {'role': 'user', 'content': inp}],
                                   'model': self.model,
                                   'temperature': self.temperature,
                                   'stream': False}
                             ).json()['message']['content']

    def send(self, inp: str) -> str:
        '''Sends the input with history from every previous call of send'''
        self.messages.append({'role': 'user', 'content': inp})
        response: str = requests.post(self.chat,
                                      json={'messages': self.messages,
                                            'model': self.model,
                                            'temperature': self.temperature,
                                            'stream': False}
                                      ).json()['message']['content']
        self.messages.append({'role': 'assistant', 'content': response})
        return response

    async def send_async(self, inp: str) -> str:
        '''Sends the input with history from every previous call of send'''
        self.messages.append({'role': 'user', 'content': inp})
        response: str = requests.post(self.chat,
                                      json={'messages': self.messages,
                                            'model': self.model,
                                            'temperature': self.temperature,
                                            'stream': False}
                                      ).json()['message']['content']
        self.messages.append({'role': 'assistant', 'content': response})
        return response
