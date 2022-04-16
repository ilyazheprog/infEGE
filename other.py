#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cache(f: object) -> object:
    """
    Кэширование функции
    :param f:
    :return: object
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
