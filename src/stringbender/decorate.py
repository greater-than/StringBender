from functools import wraps
from typing import Any, Callable

from stringbender import String


def camel(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> String:
        return String(func(*args, *kwargs)).pascal()
    return wrapper


def kebob(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> String:
        return String(func(*args, *kwargs)).kebob()
    return wrapper


def pascal(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> String:
        return String(func(*args, *kwargs)).pascal()
    return wrapper


def snake(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> String:
        return String(func(*args, *kwargs)).snake()
    return wrapper
