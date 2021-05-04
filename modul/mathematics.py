from .varibles import *
def fibonacci(n):
    numbers = [0, 1]
    for var in range(2, n+1):
         numbers += [numbers[var -2]+numbers[var-1]]
    return numbers[-1]


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

def isPrime(n):
    if int(sqrt(n))**2==n or n in [0, 1]:
        return false
    for i in range(2, int(sqrt(n))):
        if mod(n, i)==0:
            return false
    return true