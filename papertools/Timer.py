from typing import Callable, Any
from time import time


class Timer:
    '''Simple Timer Utils'''
    @staticmethod
    def simple_dec(func: Callable) -> Callable:
        '''Decorator for functions, which records the time taken for every execution'''
        def _inner(*args, **kwargs) -> Any:
            before: float = time()
            result: Any = func(*args, **kwargs)
            print(f'{func.__name__} took {time() - before} seconds')
            return result
        return _inner

    @staticmethod
    def simple(func: Callable, *args, **kwargs) -> Any:
        '''Calls the given function with the given arguments and record the time taken'''
        before: float = time()
        result: Any = func(*args, **kwargs)
        print(f'{func.__name__} took {time() - before} seconds')
        return result
