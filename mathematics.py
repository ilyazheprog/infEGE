from .constants import *


def fib(n: int) -> int:
    """
    Возвращает n-ый член последовательности Фибоначчи
    :param n:
    :return: int
    """
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


def divided(n: int, d: int) -> bool:
    """
    Если n делится на d, то возващается True, иначе - False
    :param n:
    :param d:
    :return: bool
    """
    return n % d == 0


def not_divisible(n: int, d: int) -> bool:
    """
    Если n не делится на d, то возващается True,
    иначе - False
    :param n:
    :param d:
    :return: bool
    """
    return n % d != 0


def is_Even(n: int) -> bool:
    """
    Если n - чётно, то возващается True, иначе - False
    :param n:
    :return: bool
    """
    return divided(n, 2)


def is_Odd(n: int) -> bool:
    """
    Если n - нечётно, то возващается True, иначе - False
    :param n:
    :return: bool
    """
    return not_divisible(n, 2)


def power(n: float, exp: float) -> float:
    """
    Возвращает n в степени exp
    :param n:
    :param exp:
    :return: float
    """
    return n ** exp


def sqrt(n: float) -> float:
    """
    Возвращает корень из n
    :param n:
    :return: float
    """
    return power(n, 0.5)


def factorize(number: int) -> list:
    """
    Возвращает разложение числа n на простые
    множители в list
    :param number:
    :return: list
    """
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


def factorial(n: int) -> int:
    """
    Возвращает n!
    :param n:
    :return: int
    """
    r = 1
    for var in range(1, n + 1):
        r *= var
    return r


def divisors(n: int) -> list:
    """
    Возвращает все натуральные делители числа n на интервале (1; n)
    :param n:
    :return: list
    """
    return sorted({t for i in range(2, int(sqrt(n)) + 1) for t in {i, n//i} if divided(n, t)})


def isPrime(n: int) -> bool:
    """
    Если n - простое, то возващается True, иначе - False
    :param n:
    :return: bool
    """
    return n > 1 and all(not_divisible(n, d) for d in range(2, int(sqrt(n)) + 1))