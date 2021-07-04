def replacing(s, sub, ns, mode='обычно', count='all'):
    if count == 0:
        return s
    if mode == 'обычно':
        if count == 'all':
            return s.replace(sub, ns)
        return s.replace(sub, ns, count)
    if mode == 'целиком':
        goodchars = ' ,./!;:?()-@#$%&\'\\\"*'
        result = ''
        if s[:len(sub)] == sub and s[len(sub)] in goodchars:
            s = s[len(sub):]
            result = ns
        else:
            result += s[0]
            s = s[1:]
        while (len(s)):
            if len(s) < len(sub):
                result += s
                break
            else:
                try:
                    l = s[len(sub)]
                    if s[:len(sub)] == sub and result[-1] in goodchars and l in goodchars:
                        result += ns
                        s = s[len(sub):]
                    else:
                        result += s[0]
                        s = s[1:]
                except IndexError:
                    if s == sub:
                        result += ns
                        break
                    else:
                        result += s
                        break
        return result


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


def is_number(n):
    for i in range(len(n)):
        if not (ord('0') <= ord(n[i]) <= ord('9')):
            return False
    else:
        return True
