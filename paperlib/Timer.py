from typing import Callable, Any
from time import time


class Timer:
    @staticmethod
    def simple_dec(func: Callable) -> Callable:
        def _inner(*args, **kwargs) -> Any:
            before: float = time()
            result: Any = func(*args, **kwargs)
            print(f'{func.__name__} took {time() - before} seconds')
            return result
        return _inner

    @staticmethod
    def simple(func: Callable, *args, **kwargs) -> Any:
        before: float = time()
        result: Any = func(*args, **kwargs)
        print(f'{func.__name__} took {time() - before} seconds')
        return result

    class Comparison:
        def __init__(self, path: str, exclude_params: list[int] = []) -> None:
            self.path: str = path
            self.exclude: list[int] = exclude_params
            self.results: dict = {}

        def record(self, func: Callable, *args, **kwargs) -> Any:
            before: float = time()
            func(*args, **kwargs)
            after: float = time()
