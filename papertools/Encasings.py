class Encasings:
    '''Functions for handling [Encased] strings'''
    @staticmethod
    def encase(inp: str, case1: str, case2: str = '') -> str:
        if case2 == '':
            case2 = case1
        return case1 + inp + case2

    @staticmethod
    def decase(inp: str, case1: str, case2: str = '') -> str:
        if case2 == '':
            case2 = case1
        if case1 in inp and case2 in inp:
            return ''.join(inp.split(case1, 1)[1].split(case2)[:1])
        return inp

    @staticmethod
    def decase_inner(inp: str, case1: str, case2: str = '') -> str:
        if case2 == '':
            case2 = case1
        if case1 in inp and case2 in inp:
            return ''.join(inp.split(case1, 1)[1].split(case2, 1)[:1])
        return inp

    @staticmethod
    def encased(inp: str, case1: str, case2: str = '') -> bool:
        if case2 == '':
            case2 = case1
        return inp.startswith(case1) and inp.endswith(case2)
