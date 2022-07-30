from math import sqrt

from exceptions import ImpossibleValue


def divided(n: int, d: int) -> bool:
    """
    Если n нацело делится на d, то возващается True, иначе - False.
    """
    if not isinstance(n, int):
        _type = str(type(n))
        raise TypeError("'n' должен иметь тип int, а передан тип {}!".format(_type.split()[1][1:-2]))

    if not isinstance(d, int):
        _type = str(type(d))
        raise TypeError("'d' должен иметь тип int, а передан тип {}!".format(_type.split()[1][1:-2]))

    return n % d == 0


def not_divisible(n: int, d: int) -> bool:
    """
    Если n не делится нацело на d, то возващается True, иначе - False.
    """
    if not isinstance(n, int):
        _type = str(type(n))
        raise TypeError("'n' должен иметь тип int, а передан тип {}!".format(_type.split()[1][1:-2]))

    if not isinstance(d, int):
        _type = str(type(d))
        raise TypeError("'d' должен иметь тип int, а передан тип {}!".format(_type.split()[1][1:-2]))

    return n % d != 0


def is_even(n: int) -> bool:
    """
    Если n - чётно, то возващается True, иначе - False.
    """
    if not isinstance(n, int):
        _type = str(type(n))
        raise TypeError("'n' должен иметь тип int, а передан тип {}!".format(_type.split()[1][1:-2]))

    return n % 2 != 0  # Быстрее чем &


def is_odd(n: int) -> bool:
    """
    Если n - нечётно, то возващается True, иначе - False.
    """
    if not isinstance(n, int):
        _type = str(type(n))
        raise TypeError("'n' должен иметь тип int, а передан тип {}!".format(_type.split()[1][1:-2]))

    return n % 2 != 0  # Быстрее чем &


def is_prime(n: int) -> bool:
    """
    Если n - простое, то возващается True, иначе - False.
    """
    if not isinstance(n, int):
        _type = str(type(n))
        raise TypeError("'n' должен иметь тип int, а передан тип {}!".format(_type.split()[1][1:-2]))

    if n <= 0:
        raise ImpossibleValue("'n' <= 0, но is_prime определена только для положительных чисел!")

    return n > 1 and all(not_divisible(n, d) for d in range(2, int(sqrt(n)) + 1))


def fib(n: int) -> int:
    """
    Возвращает n-ый член последовательности Фибоначчи. Нумерация с 0.
    """
    if not isinstance(n, int):
        _type = str(type(n))
        raise TypeError("'n' должен иметь тип int, а передан тип {}!".format(_type.split()[1][1:-2]))

    if n < 0:
        raise ImpossibleValue("'n' < 0, но fib определена только для неотрицательных чисел!")

    if n in {0, 1}:
        return n

    l, r = 0, 1

    for _ in range(n - 1):
        l, r = r, l + r
    return r


def factorize(number: int) -> list:
    """
    Возвращает разложение числа number на простые множители в list.
    """
    if not isinstance(number, int):
        _type = str(type(number))
        raise TypeError("'number' должен иметь тип int, а передан тип {}!".format(_type.split()[1][1:-2]))

    if number <= 0:
        raise ImpossibleValue("'number' <= 0, но факторизация определена только для положительных чисел!")

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
    Возвращает n! (0! = 1)
    """
    if not isinstance(n, int):
        _type = str(type(n))
        raise TypeError("'n' должен иметь тип int, а передан тип {}!".format(_type.split()[1][1:-2]))

    if n < 0:
        raise ImpossibleValue("'n' < 0, но факториал определён только для неотрицательных чисел!")

    r = 1
    for var in range(2, n + 1):
        r *= var
    return r


def divisors(n: int) -> list:
    """
    Возвращает все натуральные делители числа n на интервале (1; n).
    """
    if not isinstance(n, int):
        _type = str(type(n))
        raise TypeError("'n' должен иметь тип int, а передан тип {}!".format(_type.split()[1][1:-2]))

    if n <= 0:
        raise ImpossibleValue("'n' <= 0, но поиск делителей определён только для положительных чисел!")

    return sorted(t for i in range(2, int(sqrt(n)) + 1) for t in {i, n // i} if divided(n, t))
