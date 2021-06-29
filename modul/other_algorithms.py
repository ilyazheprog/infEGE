def new_num_sys(number: object, old_base: int = 10, new_base: int = 10) -> object:
    """
    Переводит число number с основанием old_base в
    число с основанием new_base
    :param number:
    :param old_base:
    :param new_base:
    :return: object
    """
    if old_base == new_base:
        return number
    elif not (2 < old_base < 36) and not (2 < new_base < 36):
        return None
    elif new_base == 10:
        return int(str(number), old_base)
    elif old_base == 10:
        mods = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        r = ''
        while number:
            number, y = divmod(number, new_base)
            r = mods[y] + r
        return r
    else:
        return new_num_sys(new_num_sys(number, old_base), 10, new_base)


def permutation_repeat(vars, k):
    masks=[]
    res=[]
    for v in range(len(vars)**k):
        n=new_num_sys(v, new_base=len(vars))
        masks+=['0'*(k-len(n))+n]
    if type(vars)==str:
        for m in masks:
            s=''
            for i in m:
                s+=' '+vars[int(i)]
            res.append(tuple(map(str, s.split())))
        
    if type(vars)==list:
        for m in masks:
            s=[]
            for i in m:
                s+=[vars[int(i)]]
            res.append(tuple(s))
    return tuple(res)

def permutations(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1:]
        for p in permutations(remLst):
            l.append([m] + p)
    return l

def printTrueTable(vars, expretion, value='all'):
    d = permutation_repeat([0, 1], len(vars))
    print(vars, 'F')
    for el in d:
        copyexp = expretion
        for varib in vars:
            copyexp = copyexp.replace(varib, str(el[vars.index(varib)]))
        if int(eval(copyexp))==value:
            print(*el, ' ', value, sep='')
        if value=='all':
            print(*el, ' ', int(eval(copyexp)), sep='')

def data_tr(n: float, old: str, new: str) -> float:
    """
    Переводит объёмы информации
    :param n:
    :param old:
    :param new:
    :return: float
    """
    s = {'bit': 1, 'byte': 8,
         'kbyte': 8 * 2 ** 10, 'kbit': 2 ** 10,
         'mbyte': 8 * 2 ** 20, 'mbit': 2 ** 20,
         'gbyte': 8 * 2 ** 30, 'gbit': 2 ** 30,
         'tbyte': 8 * 2 ** 40, 'tbit': 2 ** 40}
    return n * s[old] / s[new]


def index_n(substring: str, string: str, n: int = 1) -> int:
    """
    Возвращает n-ое вхождение СЛЕВА подстроки
    substring в строку string. Если такого вхождения
    нет, возвращается -1000
    :param n:
    :param string:
    :param substring:
    :return: int
    """
    index, count = -1000, 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring):] == substring:
            count += 1
            if count == n:
                index = i
                break
    if count == 0:
        pass
    return index


def count(substring: str, string: str) -> int:
    """
    Возвращает количество вхождений подстроки
    substring в строку string
    :param substring:
    :param string:
    :return: int
    """
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring):] == substring:
            count += 1
    return count



