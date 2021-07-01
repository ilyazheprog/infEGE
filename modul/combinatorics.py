from .system_count_and_computer_data import new_num_sys as nns


def permutation_repeat(vars, k):
    masks = []
    res = []
    for v in range(len(vars) ** k):
        n = nns(v, new_base=len(vars))
        masks += ['0' * (k - len(n)) + n]
    if type(vars) == str:
        for m in masks:
            s = ''
            for i in m:
                s += ' ' + vars[int(i)]
            res.append(tuple(map(str, s.split())))
    
    if type(vars) == list:
        for m in masks:
            s = []
            for i in m:
                s += [vars[int(i)]]
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