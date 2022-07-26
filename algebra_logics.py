from typing import Union, List

from .combinatorics import permutation_repeat
from .string import replacing


def print_true_table(variables: Union[str, List[str]], expretion: str, value='all'):
    """
    Вывод таблицы истинности лог.функции expretion от переменных variables.

    Если value='all', выводятся все строки таблицы;

    Если value=1 или True, выводятся строки таблицы, где функция истинна;

    Если value=0 или False, выводятся строки таблицы, где функция ложна.

    В качестве лог.операций можно использовать обычные операции Python
    или такие эквиваленты:
    {"&": " and ", "|": " or ", "~": " not ", "->": "<="}
    """
    operations = {"&": " and ", "|": " or ", "~": " not ", "->": "<="}

    for new, old in operations.items():
        expretion = expretion.replace(new, old)

    print(variables, 'F')

    for row in permutation_repeat('01', len(variables)):
        copy_exp = expretion

        for old, new in zip(variables, row):
            copy_exp = replacing(copy_exp, old, new, 'целиком')

        if (result := int(eval(copy_exp))) == value:
            print(*row, ' ', value, sep='')

        if value == 'all':
            print(*row, ' ', result, sep='')
