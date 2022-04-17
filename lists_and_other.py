iterable = "iter"

__all__ = ["prod"]


def prod(iter: iterable) -> float:
    """
    Возввращает произведение эл-ов итер-ого объекта iter
    :param iter:
    :return:
    """
    p = 1

    for el in iter:
        if el == 0:
            return 0
        p *= el
    return p
