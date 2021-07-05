from EasyUse.system_count_and_computer_data import new_num_sys as nns


def permutation_repeat(iter, repeat):
    '''
    Возвращает перестановки итерировванного
    обьекта iter с repeat повторениями
    :param iter:
    :param repeat:
    :return: tuple
    '''
    masks = []
    res = []
    for v in range(len(iter) ** repeat):
        n = nns(v, new_base=len(iter))
        masks += ['0' * (repeat - len(n)) + n]
    if type(iter) == str:
        for m in masks:
            s = ''
            for i in m:
                s += ' ' + iter[int(i)]
            res.append(tuple(map(str, s.split())))
    
    if type(iter) == list:
        for m in masks:
            s = []
            for i in m:
                s += [iter[int(i)]]
            res.append(tuple(s))
    return tuple(res)

def permutations(lst):
    
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1:]
        for p in permutations(remLst):
            l.append([m] + p)
    return l