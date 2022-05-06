from itertools import combinations
from .combinatorics import permutation_repeat as pr

def FanoFunc( letters_for_encode, direct='Any',  **codes):
    funcs = []
    if direct == True:
        funcs.append(lambda c: all(x != y[:len(x)] for x, y in combinations(sorted(c.values(), key=len), 2)))
    elif direct == False:
        funcs.append(lambda c: all(x != y[-len(x):] for x, y in combinations(sorted(c.values(), key=len), 2)))
    else:
        funcs.append(lambda c: all(x != y[:len(x)] for x, y in combinations(sorted(c.values(), key=len), 2)))
        funcs.append(lambda c: all(x != y[-len(x):] for x, y in combinations(sorted(c.values(), key=len), 2)))

    alphabet = codes.copy()
    for l in letters_for_encode:
        codes[l] = "-"
    used_codes =[]
    def get_code(letter, num_l):
        for i in range(1, 8):
            for ci in pr('01', repeat=i):
                (t:=codes.copy())[letter]=(cc:=''.join(ci))
                if any(f(t) for f in funcs) and (cc not in used_codes):
                    if num_l==0: used_codes.append(cc)
                    return cc

        else:
            raise EncodingWarning(f'Для алфавита {alphabet} невозможно найти ветки одновременно для {", ".join(letters_for_encode)}')
        return "-"

    while codes[letters_for_encode[-1]]=="-":
        for i, let in enumerate(letters_for_encode):
             codes[let]=get_code(let, i)

    return codes
