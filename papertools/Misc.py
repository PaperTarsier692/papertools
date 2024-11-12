from typing import Any


class Misc:
    @staticmethod
    def auto_convert(inp: str) -> Any:
        inp = inp.strip()
        try:
            return int(inp)
        except ValueError:
            pass

        try:
            return float(inp)
        except ValueError:
            pass

        if inp.lower() in ['true', 'false']:
            return inp.lower() == 'true'

        return inp
