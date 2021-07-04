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