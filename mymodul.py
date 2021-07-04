#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cache(f: object)-> object:
    '''
    Кэширование функции
    :param f:
    :return: object
    '''
    ch = {}
    
    def wrapper(*args, **kwargs):
        key = str(args)+str(kwargs)
        if key not in ch:
            ch[key]=f(*args, **kwargs)
        return ch[key]
    wrapper.__name__ = f.__name__
    wrapper.__doc__ =f.__doc__
    return wrapper

def read(*kwargs):
    def clear(s):
        copy_s =s
        while copy_s[0] == ' ':
            copy_s = copy_s[1:]
            if len(copy_s)==0:
                return [False]
        while copy_s[-1] == ' ':
            if len(copy_s)==0:
                return [False]
            copy_s = copy_s[:-1]
        return [True, copy_s]
    types_vars = kwargs
    count_vars = len(types_vars)
    def convert(*kwargs):
        nn=[]
        types_vars = kwargs
        for ty, val in zip(types_vars, values_vars):
            if type(7)==ty:
                nn.append(int(val))
            if type(7.0)==ty:
                nn.append(float(val))
        return nn
    values_vars = []
    cur_count_vars = 0
    while cur_count_vars < count_vars:
        s = input()
        if s == '':
            pass
        else:
            s = clear(s)
            if s[0]:
                s= s[1]
                cur_count_vars += len(list(s.split()))
                values_vars += [*s.split()]
                if count_vars < len(values_vars):
                    raise TypeError(f"read() takes exactly {count_vars} argument ({cur_count_vars} given)")
    return convert(*types_vars, values_vars)
    
    


