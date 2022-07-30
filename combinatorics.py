from typing import Union

from .system_count import to_base
from .exceptions import ImpossibleValue

__all__ = ["permutation_with_repeat", "permutations"]


def permutation_with_repeat(seq: Union[list, tuple, str], repeat: int = 1):
    """
    Возвращает перестановки элкементов итерируемого
    обьекта seq с repeat повторениями.
    """
    if not any(isinstance(seq, t) for t in (list, tuple, str)):
        _type = str(type(seq))
        raise TypeError("'seq' должен иметь тип list, tuple или str, а передан тип {}!".format(_type.split()[1][1:-2]))

    if not isinstance(repeat, int):
        _type = str(type(repeat))
        raise TypeError("'repeat' должен иметь тип int, а передан тип {}!".format(_type.split()[1][1:-2]))

    if repeat <= 0:
        raise ImpossibleValue("'repeat' <= 0, но число повторений должно быть положительным!")

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
    if not any(isinstance(seq, t) for t in (list, tuple, str)):
        _type = str(type(seq))
        raise TypeError("'seq' должен иметь тип list, tuple или str, а передан тип {}!".format(_type.split()[1][1:-2]))

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
