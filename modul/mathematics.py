from .varibles import *

def fib(n):
    __author__='kaazniy'

    def matrix_mult(matrix1, matrix2):
        return [
            [matrix1[0][0] * matrix2[0][0] + matrix1[0][1] * matrix2[1][0],
             matrix1[0][0] * matrix2[0][1] + matrix1[0][1] * matrix2[1][1]],
            [matrix1[1][0] * matrix2[0][0] + matrix1[1][1] * matrix2[1][0],
             matrix1[1][0] * matrix2[0][1] + matrix1[1][1] * matrix2[1][1]],
        ]

    def quick_exp(matrix: list[list[int]], power: int):
        if power == 0:
            return [[1, 0], [0, 1]]
        elif power == 1:
            return matrix
        else:
            p = power // 2
            m = power % 2
    
            sub = quick_exp(matrix, p)
            squared = matrix_mult(sub, sub)
            rem = quick_exp(matrix, m)
            return matrix_mult(squared, rem)

    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return (quick_exp([[1, 1], [1, 0]], n-1))[0][0]

def div(n, d):
    return n//d

def mod(n, d):
    return abs(n%d)

def is_Even(n):
    return mod(n, 2)==0

def is_Odd(n):
    return mod(n, 2)==1

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


def divizors(n):
    divs=set()
    for d in range(2, int(sqrt(n))+1):
        if mod(n, d)==0:
            divs.add(d)
            divs.add(n//d)
    divs=list(divs)
    divs.sort()
    return divs

def isPrime(n):
    if int(sqrt(n))**2==n or n in [0, 1]:
        return false
    for i in range(2, int(sqrt(n))):
        if mod(n, i)==0:
            return false
    return true