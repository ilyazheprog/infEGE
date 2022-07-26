from typing import Union, List, Tuple

from system_count_and_computer_data import new_num_sys as nns


def permutation_repeat(seq: Union[List, Tuple], repeat: int = 1):
    """
    Возвращает перестановки элкементов итерировванного
    обьекта seq с repeat повторениями.
    """
    def _gen_mask():
        for v in range(len(seq) ** repeat):
            n = nns(v, new_base=len(seq))
            yield '0' * (repeat - len(n)) + n

    for m in _gen_mask():
        s = [seq[int(i)] for i in m]
        yield tuple(s)


def permutations(seq: Union[List, Tuple, str]):
    """
    Возвращает перестановки элкементов итерировванного объекта seq.
    """
    return permutation_repeat(seq, len(seq))

