from functools import wraps
from superstring import String


def camel(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return String(func(*args, *kwargs)).pascal()
    return wrapper


def kebob(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return String(func(*args, *kwargs)).kebob()
    return wrapper


def pascal(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return String(func(*args, *kwargs)).pascal()
    return wrapper


def snake(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return String(func(*args, *kwargs)).snake()
    return wrapper
