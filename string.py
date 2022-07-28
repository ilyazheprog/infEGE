def replacing(string: str, substring: str, new_string: str, mode: str = 'обычно', cnt: str = 'all') -> str:
    """
    Возвращает строку string с заменённой подстрокой
    substring на  подстроку new_string в количестве
    cnt.

    Режим "обычно":
                    замена стандартным replace

    Режим "целиком":
                    замена подстроки substring если она не
                    является частью большей подстроки.
    """
    if cnt == 0:
        return string
    if mode == 'обычно':
        if cnt == 'all':
            return string.replace(substring, new_string)
        return string.replace(substring, new_string, cnt)
    if mode == 'целиком':
        result = ''
        if string[:len(substring)] == substring and not string[len(substring)].isalpha():
            string = string[len(substring):]
            result = new_string
        else:
            result += string[0]
            string = string[1:]
        while len(string):
            if len(string) < len(substring):
                result += string
                break
            else:
                try:
                    next_char = string[len(substring)]
                    if string[:len(substring)] == substring and not result[-1].isalpha() and not next_char.isalpha():
                        result += new_string
                        string = string[len(substring):]
                    else:
                        result += string[0]
                        string = string[1:]
                except IndexError:
                    if string == substring:
                        result += new_string
                        break
                    else:
                        result += string
                        break
        return result


def index_n(string: str, substring: str, n: int = 1) -> int:
    """
    Возвращает индекс n-го вхождения СЛЕВА подстроки
    substring в строку string. Если такого вхождения
    нет, возвращается -1000.
    """
    index, cnt = -1000, 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring):] == substring:
            cnt += 1
            if cnt == n:
                index = i
                break
    return index


def is_number(n: str) -> bool:
    """
    Проверяет является ли строка n числом.
    Если да возвращается True, иначе - False.
    """
    if not isinstance(n, str):
        _type = str(type(n))
        raise TypeError("'n' должен иметь тип str, а передан тип {}!".format(_type.split()[1][1:-2]))

    return all("0" <= sym <= "9" for sym in n)
