import os
import json


class File:
    def __init__(self, path: str) -> None:
        self.path: str = os.path.abspath(path)

    def exists(self) -> bool:
        return os.path.exists(self.path)

    def read(self, error_ok: bool = False) -> str:
        if not self.exists:
            if error_ok:
                return ''
            raise FileNotFoundError(f"File: {self.path} not found")
        with open(self.path, 'r', encoding='utf-8') as f:
            return f.read()

    def readlines(self) -> list[str]:
        return self.read().splitlines()

    def write(self, content: str, create_path: bool = False) -> None:
        if create_path:
            self.create_path(self.path)

        with open(self.path, 'w', encoding='utf-8') as f:
            f.write(content)

    def writelines(self, content: list[str], create_path: bool = False) -> None:
        if create_path:
            self.create_path(self.path)

        with open(self.path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(content))

    def json_r(self) -> dict:
        return json.loads(self.read())

    def json_w(self, content: dict, indent: int = 2, create_path: bool = False, check_json: bool = True) -> None:
        if create_path:
            self.create_path(self.path)

        if check_json:
            try:
                json.dumps(content)
            except TypeError:
                raise TypeError(f"Content: {content} is not JSON serializable")

        with open(self.path, 'w') as f:
            json.dump(content, f, indent=indent)

    def append(self, content: str, create_path: bool = False) -> None:
        if create_path and not self.exists():
            self.create_path(self.path)
            inp: list[str] = [content]
        else:
            inp: list[str] = self.readlines()
            inp.append(content)
        self.writelines(inp)

    def __str__(self) -> str:
        return self.read()

    @staticmethod
    def create_path(path: str, mode: int = 777, exists_ok: bool = True):
        if not exists_ok and os.path.exists(path):
            raise FileExistsError(f"File: {path} already exists")
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path), mode, exists_ok)
