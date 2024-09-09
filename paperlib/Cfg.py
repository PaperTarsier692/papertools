from .File import File
from .Encasings import Encasings


class Cfg:
    def __init__(self) -> None:
        pass

    @staticmethod
    def path_to_dict(path: str, error_ok: bool = False) -> dict[str, dict[str, str]]:
        if not path.endswith('.cfg') and not error_ok:
            raise SyntaxError("File not ending in .cfg")
        output: dict[str, dict[str, str]] = {}
        content: list[str] = File(path).readlines()
        current_category: str = ''
        for line in content:
            if Encasings.encased(line, '[', ']'):
                current_category = Encasings.decase(line, '[', ']')
                output[current_category] = {}
            elif '=' in line:
                output[current_category][line.split(
                    '=')[0]] = line.split('=', 1)[1]
            elif not error_ok:
                raise SyntaxError("'=' not found")
        return output

    @staticmethod
    def list_to_dict(content: list[str], error_ok: bool = False) -> dict[str, dict[str, str]]:
        output: dict[str, dict[str, str]] = {}
        current_category: str = ''
        for line in content:
            if Encasings.encased(line, '[', ']'):
                current_category = Encasings.decase(line, '[', ']')
                output[current_category] = {}
            elif '=' in line:
                output[current_category][line.split(
                    '=')[0]] = line.split('=', 1)[1]
            elif not error_ok:
                raise SyntaxError("'=' not found")
        return output
