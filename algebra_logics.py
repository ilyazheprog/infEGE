from .combinatorics import permutation_repeat
from .work_with_string import replacing


def printTrueTable(vars, expretion: str, value='all'):
    """
    Вывод таблицы истинности лог.функции expretion от переменных vars.

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

    print(vars, 'F')
    for el in permutation_repeat('01', len(vars)):
        copyexp = expretion
        for varib, rep in zip(vars, el):
            copyexp = replacing(copyexp, varib, rep, 'целиком')
        if int(eval(copyexp)) == value:
            print(*el, ' ', value, sep='')
        if value == 'all':
            print(*el, ' ', int(eval(copyexp)), sep='')
