#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cache(f):
    ch = {}
    @wraps(f)
    def wrapper(*args, **kwargs):
        key = str(args)+str(kwargs)
        if key not in ch:
            ch[key]=f(*args, **kwargs)
        return ch[key]
    return wrapper

def read(**kwargs):
    vr = kwargs
    v = len(vr)
    def var(n, /, **vr):
        path = getcwd()
        path += '/temp.py'
        f = open(path, 'w')
        for (key, val ), r in zip(vr.items(), n):
            s = str(key) + ' = ' + str(val(r)) + '\n'
            f.write(s)
        f.close()
        
    def logics():
        contents = []
        c = 0
        while c < v:
            s = input()
            if s == '':
                pass
            else:
                while s[0] == ' ':
                    s = s[1:]
                while s[-1] == ' ':
                    s = s[:-1]
                c += len(list(s.split()))
                contents += [*s.split()]
            if v < len(contents):
                raise TypeError(f"read() takes exactly {v} argument ({c} given)")
        nn = [str(x) for x in contents]
        return nn
        
    var(logics(), **vr)
    


