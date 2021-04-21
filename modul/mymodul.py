true, false, maxValue, minValue = True, False, float('inf'), float('-inf')

def div(n, d):
    return n//d

def mod(n, d):
    return n%d

def divizors(n):
    divs=set()
    for d in range(2, int(n**0.5)+1):
        if mod(n, d)==0:
            divs.add(d)
            divs.add(n//d)
    divs=list(divs)
    divs.sort()
    return divs


def read(type=int, sep=' ', n=1):
    if n==1:
        return type(input())
    else:
        if sep!='\n':
            return map(type, input().split(sep))
        else:
            a, i = [], 1
            while i<=n:
                x = input()
                if x!='':
                    a+=[type(x)]
                    i+=1
            return a

def dataTR(n, old,new):
    s = {'bit':1, 'byte': 8, 'kbit': 1000,
         'kbyte': 8 * 10**3, 'mbyte': 8*10**6,
         'mbit': 10 ** 6, 'gbyte': 8 * 10 ** 9,
         'gbit': 10 ** 9,'tbyte': 8 * 1024 ** 4,
         'tbit': 10 ** 12}
    return n*s[old]/s[new]

def isPrime(n):
    if int(n**0.5)**2==n:
        return false
    for i in range(2, int(n**0.5)):
        if n%i==0:
            return false
    return n > 1

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
