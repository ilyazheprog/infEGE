from typing import Union
from .exceptions import InvalidMode, ImpossibleValue

__all__ = ["replacing", "index_n", "is_number"]


def replacing(string: str, substring: str, new_string: str, mode: str = 'обычно',
              cnt: Union[int, str] = 'all') -> str:
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
    if not isinstance(string, str):
        _type = str(type(string))
        raise TypeError("'string' должен иметь тип str, а передан тип {}!".format(_type.split()[1][1:-2]))

    if not isinstance(substring, str):
        _type = str(type(substring))
        raise TypeError("'substring' должен иметь тип str, а передан тип {}!".format(_type.split()[1][1:-2]))

    if not isinstance(new_string, str):
        _type = str(type(new_string))
        raise TypeError("'new_string' должен иметь тип str, а передан тип {}!".format(_type.split()[1][1:-2]))

    if not isinstance(mode, str):
        _type = str(type(mode))
        raise TypeError("'mode' должен иметь тип str, а передан тип {}!".format(_type.split()[1][1:-2]))

    if mode not in ("обычно", "целиком"):
        raise InvalidMode("Неизвестный режим {}. Режим должен быть \"обычно\" или \"целиком\"!".format(mode))

    if cnt != "all" and isinstance(cnt, str):
        raise ImpossibleValue("'cnt' имеет тип str, но отличное от \"all\"!")

    if cnt < 0:
        raise ImpossibleValue("'cnt' < 0, но количество не может быть отрительным!")

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
    if not isinstance(string, str):
        _type = str(type(string))
        raise TypeError("'string' должен иметь тип str, а передан тип {}!".format(_type.split()[1][1:-2]))

    if not isinstance(substring, str):
        _type = str(type(substring))
        raise TypeError("'substring' должен иметь тип str, а передан тип {}!".format(_type.split()[1][1:-2]))

    if not isinstance(n, int):
        _type = str(type(n))
        raise TypeError("'n' должен иметь тип int, а передан тип {}!".format(_type.split()[1][1:-2]))

    if n <= 0:
        raise ImpossibleValue("'n' <= 0, но номер вхождения должен быть положительным!")

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
