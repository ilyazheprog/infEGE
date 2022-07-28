from typing import Union
from exceptions import InvalidBase

__all__ = ["to_base"]


def __validate(num, ob, nb) -> None:
    if not any(isinstance(num, t) for t in (int, str)):
        _type_num = str(type(num))
        raise TypeError("'number' должен иметь тип int или str, а передан тип {}!".format(_type_num.split()[1][1:-2]))
    if not isinstance(ob, int):
        _type_old_base = str(type(ob))
        raise TypeError("'old_base' должен иметь тип int, а передан тип {}!".format(_type_old_base.split()[1][1:-2]))
    if not isinstance(nb, int):
        _type_new_base = str(type(nb))
        raise TypeError("'new_base' должен иметь тип int, а передан тип {}!".format(_type_new_base.split()[1][1:-2]))


def to_base(number: Union[int, str], old_base: int = 10, new_base: int = 10) -> Union[int, str]:
    """
    Переводит число number с основанием old_base в число с основанием new_base.
    """
    __validate(number, old_base, new_base)
    if old_base == new_base:
        return number
    elif not (2 <= old_base <= 36) or not (2 <= new_base <= 36):
        raise InvalidBase("Невозможно перевести, т.к., old_base и new_base должны быть от 2 до 36")
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
        return to_base(to_base(number, old_base), 10, new_base)

to_base(number=22, old_base=[0], new_base=1)