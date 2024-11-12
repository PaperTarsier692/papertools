from typing import Any
from .File import File
from .Encasings import Encasings
from .Misc import Misc


class Cfg:
    '''Class for handling .cfg files'''

    def __init__(self) -> None:
        pass

    @staticmethod
    def path_to_dict(path: str, error_ok: bool = False, include_empty: bool = False) -> dict[str, dict[str, Any]]:
        '''Returns a dict representation of a .cfg file'''
        if not path.endswith('.cfg') and not error_ok:
            raise SyntaxError("File not ending in .cfg")
        output: dict[str, dict[str, Any]] = {}
        content: list[str] = File(path).readlines()
        current_category: str = ''
        for line in content:
            if Encasings.encased(line, '[', ']'):
                current_category = Encasings.decase(line, '[', ']')
                output[current_category] = {}
            elif '=' in line:
                if not include_empty and line.split('=', 1)[1].strip() == '':
                    continue
                output[current_category][line.split(
                    '=')[0].strip()] = Misc.auto_convert(line.split('=', 1)[1].strip())
            elif line.strip() == '':
                continue
            elif not error_ok:
                raise SyntaxError("'=' not found")
        return output

    @staticmethod
    def list_to_dict(content: list[str], error_ok: bool = False, include_empty: bool = False) -> dict[str, dict[str, Any]]:
        '''Returns a dict representation of a list of strings representing a .cfg file'''
        output: dict[str, dict[str, Any]] = {}
        current_category: str = ''
        for line in content:
            if Encasings.encased(line, '[', ']'):
                current_category = Encasings.decase(line, '[', ']')
                output[current_category] = {}
            elif '=' in line:
                if not include_empty and line.split('=', 1)[1].strip() == '':
                    continue
                output[current_category][line.split(
                    '=')[0].strip()] = Misc.auto_convert(line.split('=', 1)[1].strip())
            elif line.strip() == '':
                continue
            elif not error_ok:
                raise SyntaxError("'=' not found")
        return output
