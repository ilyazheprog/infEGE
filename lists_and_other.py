from typing import Iterable, Union


def prod(seq: Iterable) -> Union[int, float]:
    """
    Возввращает произведение элементов итерируемого объекта seq.
    """
    p = 1

    for el in seq:
        if el == 0:
            return 0
        p *= el

    return p
