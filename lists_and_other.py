from typing import Union


def prod(seq: Union[list, tuple, set]) -> Union[int, float]:
    """
    Возввращает произведение элементов итерируемого объекта seq.
    """
    if not any(isinstance(seq, t) for t in (list, tuple, set)):
        _type = str(type(seq))
        raise TypeError("'seq' должен иметь тип list, tuple или set, а передан тип {}!".format(_type.split()[1][1:-2]))

    p = 1

    for el in seq:
        if not any(isinstance(el, t) for t in (int, float)):
            _type = str(type(el))
            raise TypeError(
                            "'seq' содержит не поддерживаемый тип {}!".format(_type.split()[1][1:-2]))
        if el == 0:
            return 0
        p *= el

    return p
