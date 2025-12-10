import functools
from typing import Callable


NUM_WORDS = {1: 'ONE', 2: 'TWO'}
REGISTERED = []


def registered_functions() -> list[tuple[str, int, Callable]]:
    return REGISTERED

def register(filename: str, part: int):
    def _register(func):
        @functools.wraps(func)
        def wrapper(data_file: str):
            return func(data_file)
        REGISTERED.append((filename, part, wrapper))
        return wrapper
    return _register