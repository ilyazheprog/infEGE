from typing import Callable


def cache(f: Callable) -> Callable:
    """
    Кэширование функции (декоратор).
    """
    ch = {}

    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in ch:
            ch[key] = f(*args, **kwargs)
        return ch[key]

    wrapper.__name__ = f.__name__
    wrapper.__doc__ = f.__doc__
    return wrapper
