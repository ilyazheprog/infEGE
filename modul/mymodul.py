#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import getcwd
from functools import wraps
true, false, maxValue, minValue = True, False, float('inf'), float('-inf')

def fibonacci(n):
    numbers = [0, 1]
    for var in range(2, n+1):
         numbers += [numbers[var -2]+numbers[var-1]]
    return numbers[-1]

def cache(f):
    ch = {}
    @wraps(f)
    def wrapper(*args, **kwargs):
        key = str(args)+str(kwargs)
        if key not in ch:
            ch[key]=f(*args, **kwargs)
        return ch[key]
    return wrapper

def power(n, exp):
    return n ** exp

def sqrt(n):
    return power(n, 0.5)

def factorize(number):
    prime_factors = []
    while number % 2 == 0:
        prime_factors.append(2)
        number = number / 2
    for i in range(3, int(sqrt(number)) + 1, 2):
        while number % i == 0:
            prime_factors.append(int(i))
            number = number / i
    if number > 2:
        prime_factors.append(int(number))
    return prime_factors

def factorial(n):
    r = 1
    for var in range(1, n+1):
        r*=var
    return r

def div(n, d):
    return n//d

def mod(n, d):
    return abs(n%d)

def divizors(n):
    divs=set()
    for d in range(2, int(sqrt(n))+1):
        if mod(n, d)==0:
            divs.add(d)
            divs.add(n//d)
    divs=list(divs)
    divs.sort()
    return divs


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
    


def dataTR(n, old,new):
    s = {'bit':1, 'byte': 8, 'kbit': 1000,
         'kbyte': 8 * 10**3, 'mbyte': 8*10**6,
         'mbit': 10 ** 6, 'gbyte': 8 * 10 ** 9,
         'gbit': 10 ** 9,'tbyte': 8 * 1024 ** 4,
         'tbit': 10 ** 12}
    return n*s[old]/s[new]

def isPrime(n):
    if int(sqrt(n))**2==n or n in [0, 1]:
        return false
    for i in range(2, int(sqrt(n))):
        if mod(n, i)==0:
            return false
    return true

def quickIn(a,el):
    d={x:1 for x in a}
    return el in d

def indexN(string, substring, N=1):
    """
    Returns the index of N occurrence of the substring in the source string
    """
    index, count = None, 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring):] == substring:
            count += 1
            if count==N:
                index=i
                break
    if count==0:
        pass
    return index

def count(string, substring):
    """
    Returns the number of occurrences of the substring in the source string
    """
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring):] == substring:
            count += 1
    return count

def Translation_systems_counts(number, old_base=10, new_base=10):
    """
    Coming soon...
    """
    if old_base == new_base:
        return number
    elif not (2 < old_base < 36) and not(2 < new_base < 36):
        return None
    elif new_base == 10:
        return int(str(number), old_base)
    elif old_base == 10:
        mods = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        r=''
        while number:
            number, y = divmod(number, new_base)
            r=mods[y]+r
        return r
    else:
        return Translation_systems_counts(Translation_systems_counts(number,old_base,10),10,new_base)
