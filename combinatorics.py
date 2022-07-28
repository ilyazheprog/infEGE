from typing import Union

from .system_count import to_base


def permutation_repeat(seq: Union[list, tuple, str], repeat: int = 1):
    """
    Возвращает перестановки элкементов итерируемого
    обьекта seq с repeat повторениями.
    """
    def _gen_mask():
        for v in range(len(seq) ** repeat):
            n = to_base(v, new_base=len(seq))
            yield '0' * (repeat - len(n)) + n

    for m in _gen_mask():
        s = [seq[int(i)] for i in m]
        yield tuple(s)


def permutations(seq: Union[list, tuple, str]):
    """
    Возвращает перестановки элкементов итерируемого объекта seq.
    """
    if len(seq) == 0:
        return []
    if len(seq) == 1:
        return [seq]

    lst = []

    for i in range(len(seq)):
        m = seq[i]
        remLst = seq[:i] + seq[i + 1:]
        for p in permutations(remLst):
            lst.append(m + p)
    return lst
