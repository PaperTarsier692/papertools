import os


class Dir:
    '''Easier functions for directories'''
    @staticmethod
    def listfiles(path: str, include_hidden: bool = True) -> list[str]:
        '''Returns a list of all files in the given directory'''
        return [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)) if not file.startswith('.') or include_hidden]

    @staticmethod
    def listdirs(path: str, include_hidden: bool = True) -> list[str]:
        '''Returns a list of all subdirs in the given directory'''
        return [dir for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir)) if not dir.startswith('.') or include_hidden]

    @staticmethod
    def walk(path: str):
        '''Returns a generator for all files in the given directory'''
        for file in Dir._walk(path):
            yield file

    @staticmethod
    def _walk(path: str) -> list[str]:
        output: list[str] = []
        output.extend([os.path.join(path, file)
                      for file in Dir.listfiles(path)])
        for dir in Dir.listdirs(path):
            output.extend(Dir._walk(os.path.join(path, dir)))
        return output
