from .combinatorics import permutation_repeat
from .work_with_string import replacing

def printTrueTable(vars, expretion, value='all'):
    d = permutation_repeat('01', len(vars))
    print(vars, 'F')
    for el in d:
        copyexp = expretion
        for varib, rep in zip(vars, el):
            copyexp = replacing(copyexp, varib, rep, 'целиком')
        if int(eval(copyexp))==value:
            print(*el, ' ', value, sep='')
        if value=='all':
            print(*el, ' ', int(eval(copyexp)), sep='')
