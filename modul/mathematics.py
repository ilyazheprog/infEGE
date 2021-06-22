from .varibles import *


def fib(n):
    '''
    Возвращает n-ый член последовательности Фибоначчи
    :param n:
    :return int:
    '''
    __author__ = 'kaazniy'
    
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
        return (quick_exp([[1, 1], [1, 0]], n - 1))[0][0]


def div(n, d):
    '''
    Возвращает целую часть от деления n на d
    :param n:
    :param d:
    :return int:
    '''
    return n // d


def mod(n, d):
    '''
    Возвращает остаток от деления n на d
    :param n:
    :param d:
    :return int:
    '''
    return abs(n % d)


def divided(n, d):
    '''
    Если n делится на d, то возващается True, иначе - False
    :param n:
    :return bool:
    '''
    return mod(n, d) == 0


def not_divisible(n, d):
    '''
    Если n не делится на d, то возващается True, иначе - False
    :param n:
    :return bool:
    '''
    return mod(n, d) != 0


def is_Even(n):
    '''
    Если n - чётно, то возващается True, иначе - False
    :param n:
    :return bool:
    '''
    return divided(n, 2)


def is_Odd(n):
    '''
    Если n - нечётно, то возващается True, иначе - False
    :param n:
    :return bool:
    '''
    return not_divisible(n, 2)


def power(n, exp):
    '''
    Возвращает n в степени exp
    :param n:
    :param exp:
    :return float:
    '''
    return n ** exp


def sqrt(n):
    '''
    Возвращает корень из n
    :param n:
    :return float:
    '''
    return power(n, 0.5)


def factorize(number):
    '''
    Возвращает разложение числа n на простые
    множители
    :param n:
    :return list:
    '''
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
    '''
    Возвращает n!
    :param n:
    :return int:
    '''
    r = 1
    for var in range(1, n + 1):
        r *= var
    return r


def divizors(n):
    '''
    Возвращает все делители числа  n
    :param n:
    :return list
    '''
    divs = set()
    for d in range(2, int(sqrt(n)) + 1):
        if mod(n, d) == 0:
            divs.add(d)
            divs.add(n // d)
    divs = list(divs)
    divs.sort()
    return divs


def isPrime(n):
    '''
    Если n - простое, то возващается True, иначе - False
    :param n:
    :return bool:
    '''
    if int(sqrt(n)) ** 2 == n or n in [0, 1]:
        return false
    for i in range(2, int(sqrt(n))):
        if mod(n, i) == 0:
            return false
    return true
