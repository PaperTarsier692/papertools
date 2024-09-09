from os import name as os
from os import system
from typing import Literal

colours: dict[str, str] = {'red': "\033[91m", 'yellow': "\033[93m",
                           'blue': "\033[94m", 'green': "\033[92m", 'end': "\033[0m"}


class Console:
    @staticmethod
    def clear() -> None:
        if os == 'nt':
            system('cls')
        else:
            system('clear')

    @staticmethod
    def print_colour(inp: str, colour: Literal['red', 'yellow', 'blue', 'green']) -> None:
        print(f'{colours.get(colour, "")}{inp}{colours["end"]}')
