from .combinatorics import permutation_repeat


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
