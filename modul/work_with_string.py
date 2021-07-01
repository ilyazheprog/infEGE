
def index_n(substring: str, string: str, n: int = 1) -> int:
    """
    Возвращает n-ое вхождение СЛЕВА подстроки
    substring в строку string. Если такого вхождения
    нет, возвращается -1000
    :param n:
    :param string:
    :param substring:
    :return: int
    """
    index, count = -1000, 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring):] == substring:
            count += 1
            if count == n:
                index = i
                break
    return index


def count(substring: str, string: str) -> int:
    """
    Возвращает количество вхождений подстроки
    substring в строку string
    :param substring:
    :param string:
    :return: int
    """
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring):] == substring:
            count += 1
    return count