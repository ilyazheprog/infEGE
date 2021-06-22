def dataTR(n, old, new):
    s = {'bit': 1, 'byte': 8,
         'kbit': 2 ** 10, 'kbyte': 8 * 2 ** 10,
         'mbyte': 8 * 2 ** 20, 'mbit': 2 ** 20,
         'gbyte': 8 * 2 ** 30, 'gbit': 2 ** 30,
         'tbyte': 8 * 2 ** 40, 'tbit': 10 ** 40}
    return n * s[old] / s[new]

def indexN(string, substring, N=1):
    """
    Returns the index of N occurrence of the substring in the source string
    """
    index, count = None, 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring):] == substring:
            count += 1
            if count == N:
                index = i
                break
    if count == 0:
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
        return Translation_systems_counts(Translation_systems_counts(number, old_base, 10), 10, new_base)
