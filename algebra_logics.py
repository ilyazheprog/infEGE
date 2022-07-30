from typing import Union

from .combinatorics import permutation_with_repeat
from .string import replacing
from .exceptions import ImpossibleValue


def print_true_table(variables: str, expretion: str, value: Union[int, bool, 'all'] = 'all') -> None:
    """
    Вывод таблицы истинности лог.функции expretion от переменных variables.

    Если value='all', выводятся все строки таблицы;

    Если value=1 или True, выводятся строки таблицы, где функция истинна;

    Если value=0 или False, выводятся строки таблицы, где функция ложна.

    В качестве лог.операций можно использовать обычные операции Python
    или такие эквиваленты:
    {"&": " and ", "|": " or ", "~": " not ", "->": "<="}
    """
    if not isinstance(variables, str):
        _type = str(type(variables))
        raise TypeError("'variables' должен иметь тип str, а передан тип {}!".format(_type.split()[1][1:-2]))

    if not isinstance(expretion, str):
        _type = str(type(expretion))
        raise TypeError("'expretion' должен иметь тип str, а передан тип {}!".format(_type.split()[1][1:-2]))

    if not any(isinstance(value, t) for t in (int, bool, str)):
        _type = str(type(value))
        raise TypeError("'value' должен иметь тип int, bool или str, а передан тип {}!".format(_type.split()[1][1:-2]))

    if isinstance(value, str) and value != "all":
        raise ImpossibleValue("Неизвестное {}. Возможно, Вы имели в виду \"all\"!".format(value))

    operations = {"&": " and ", "|": " or ", "~": " not ", "->": "<="}

    for new, old in operations.items():
        expretion = expretion.replace(new, old)

    print(variables, 'F')

    for row in permutation_with_repeat('01', len(variables)):
        copy_exp = expretion

        for old, new in zip(variables, row):
            copy_exp = replacing(copy_exp, old, new, 'целиком')

        if (result := int(eval(copy_exp))) == value:
            print(*row, ' ', value, sep='')

        if value == 'all':
            print(*row, ' ', result, sep='')
