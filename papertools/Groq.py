from groq import Groq as Gq


class Groq:
    def __init__(self, model: str, key: str, temperature: float = 1, system: str = '') -> None:
        self.model: str = model
        self.client: Gq = Gq(api_key=key)
        self.temperature: float = temperature
        self.system: str = system

    def single(self, inp: str) -> str:
        return self.client.chat.completions.create(
            messages=[{'role': 'system', 'content': self.system}, {'role': 'user', 'content': inp}], model=self.model, temperature=self.temperature).model_dump()['choices'][0]['message']['content']
