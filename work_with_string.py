def replacing(string: str, substring: str, new_string: str, mode: str = 'обычно', count: str = 'all') -> str:
    """
    Возвращает строку string с заменённой подстрокой
    substring на  подстроку new_string в количестве
    count.
    Режим "обычно":
                    замена стандартным replace
    Режим "целиком":
                    замена подстроки substring если она не
                    является частью большей подстроки
    :param string:
    :param substring:
    :param new_string:
    :param mode:
    :param count:
    :return result:
    """
    if count == 0:
        return string
    if mode == 'обычно':
        if count == 'all':
            return string.replace(substring, new_string)
        return string.replace(substring, new_string, count)
    if mode == 'целиком':
        goodchars = ' ,./!;:?()<=-@#$%&\'\\\"*'
        result = ''
        if string[:len(substring)] == substring and string[len(substring)] in goodchars:
            string = string[len(substring):]
            result = new_string
        else:
            result += string[0]
            string = string[1:]
        while (len(string)):
            if len(string) < len(substring):
                result += string
                break
            else:
                try:
                    next_char = string[len(substring)]
                    if string[:len(substring)] == substring and result[-1] in goodchars and next_char in goodchars:
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


def is_number(n: str)->bool:
    """
    Проверяет является ли строка n числом.
    Если да возвращается True, иначе - False
    :param n:
    :return: bool
    """
    for i in range(len(n)):
        if not (ord('0') <= ord(n[i]) <= ord('9')):
            return False
    return True

