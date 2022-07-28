## Документация
### Немного терминологии
**Модуль** - это файл с расширением `.py`, находящийся в библиотеке.

Например, модуль `constants` - это файл `constants.py`.

---
### Модуль decorators
#### 1. Декоратор cache
Для чего: *мемоизация работы функции*.

Пример использования:
```python
from infEGE import cache

@cache
def fib(n):
    if n in {0,1}:
        return 1
    return fib(n - 1) + fib(n - 2)

fib(50)
```
Если убрать `@cache`, то вычисляться будет очень долго.

---
### Модуль constants
Для чего: *константы для использования в алгоритмах*.

Содержимое:
```python
E = 2.718281828459045
PI = 3.141592653589793
maxValue = float('inf')
minValue = float('-inf')
```
---

### Модуль algebra_logic
#### 1. Функция print_true_table
Синтаксис: **print_true_table(variables: Union[str, List[str]], expretion: str, value: Union[int, bool, 'all'] = 'all')**

Для чего: 
    
    Вывод таблицы истинности лог.функции expretion от переменных variables.

    Если value='all', выводятся все строки таблицы;

    Если value=1 или True, выводятся строки таблицы, где функция истинна;

    Если value=0 или False, выводятся строки таблицы, где функция ложна.

    В качестве лог.операций можно использовать обычные операции Python
    или такие эквиваленты:
    {"&": " and ", "|": " or ", "~": " not ", "->": "<="}.
Пример использования #1:
```python
from infEGE import print_true_table

print_true_table("xy", "x->y", 1)
```
Вывод:
```
xy F
00 1
01 1
11 1
```
**Внимание: в Python приоритет <= выше, чем and, or, not! Ставьте скобки!** 

Пример использования #2:
```python
from infEGE import print_true_table

print_true_table("xy", "x&(y|x)|y", 0)
```
Вывод:
```
xy F
00 0
```

Пример использования #3:
```python
from infEGE import print_true_table

print_true_table("xzy", "x or z and (y or not x)")
```
Вывод:
```
xzy F
000 0
001 0
010 1
011 1
100 1
101 1
110 1
111 1
```
---
### Модуль combinatorics
#### 1. Функция permutation_repeat
Синтаксис: **permutation_repeat(seq: Union[list, tuple, str], repeat: int = 1)**

Для чего: 

    Возвращает перестановки элкементов итерируемого
    обьекта seq с repeat повторениями.
Пример использования:
```python
from infEGE import permutation_repeat

for el in permutation_repeat('123', 2):
    print(el)
```
Вывод:
```
('1', '1')
('1', '2')
('1', '3')
('2', '1')
('2', '2')
('2', '3')
('3', '1')
('3', '2')
('3', '3')
```
#### 2. Функция permutations
Синтаксис: **permutations(seq: Union[list, tuple, str]):**

Для чего: 

    Возвращает перестановки элкементов итерируемого объекта seq.
Пример использования:
```python
from infEGE import permutations

for el in permutations('abc'):
    print(el)
```
Вывод:
```
abc
acb
bac
bca
cab
cba
```
---
### Модуль lists_and_other
#### 1. Функция prod
Синтаксис: **prod(seq: Iterable) -> Union[int, float]**

Для чего: 

    Возввращает произведение элементов итерируемого объекта seq.
Пример использования:
```python
from infEGE import prod

print(prod([5, 8, 6, 100, 54]))
```
Вывод:
```
1296000
```
---
### Модуль string
#### 1. Функция replacing
Синтаксис: **replacing(string: str, substring: str, new_string: str, mode: str = 'обычно', cnt: str = 'all') -> str**

Для чего: 

    Возвращает строку string с заменённой подстрокой
    substring на  подстроку new_string в количестве cnt.

    Режим "обычно":
                    замена стандартным replace

    Режим "целиком":
                    замена подстроки substring если она не
                    является частью большей подстроки.
Пример использования #1:
```python
from infEGE import replacing

print(replacing("Питон плохой тон", "тон", "нот"))
```
Вывод:
```
Пинот плохой нот
```

Пример использования #2:
```python
from infEGE import replacing

print(replacing("Питон плохой тон", "тон", "нот", cnt=1))
```
Вывод:
```
Пинот плохой тон
```

Пример использования #3:
```python
from infEGE import replacing

print(replacing("Питон плохой тон", "тон", "нот", "целиком"))
```
Вывод:
```
Питон плохой нот
```

#### 2. Функция index_n
Синтаксис: **index_n(string: str, substring: str, n: int = 1) -> int**

Для чего: 

    Возвращает индекс n-го вхождения СЛЕВА подстроки
    substring в строку string. Если такого вхождения
    нет, возвращается -1000.
Пример использования #1:
```python
from infEGE import index_n

print(index_n("01230123", "1"))
```
Вывод:
```
1
```

Пример использования #2:
```python
from infEGE import index_n

print(index_n("01230123", "1", 2))
```
Вывод:
```
5
```

Пример использования #3:
```python
from infEGE import index_n

print(index_n("01230123", "1", 3))
```
Вывод:
```
-1000
```
#### 3. Функция is_number
Синтаксис: **is_number(n: str) -> bool**

Для чего: 

    Проверяет является ли строка n числом.
    Если да возвращается True, иначе - False.
Пример использования #1:
```python
from infEGE import is_number

print(is_number("23"))
```
Вывод:
```
True
```

Пример использования #2:
```python
from infEGE import is_number

print(is_number("2n3"))
```
Вывод:
```
False
```
---
### Модуль system_count
#### 1. Функция to_base
Синтаксис: **to_base(number: Union[int, str], old_base: int = 10, new_base: int = 10) -> Union[int, str]**

Для чего: 

    Переводит число number с основанием old_base в число
    с основанием new_base.
Пример использования #1:
```python
from infEGE import to_base

print(to_base(5, new_base=2))
```
Вывод:
```
101
```
Пример использования #2:
```python
from infEGE import to_base

print(to_base(15, new_base=16))
```
Вывод:
```
F
```
Пример использования #3:
```python
from infEGE import to_base

print(to_base("FA32", old_base=17, new_base=10))
```
Вывод:
```
76638
```
Пример использования #4:
```python
from infEGE import to_base

print(to_base("FA32", old_base=17, new_base=6))
```
Вывод:
```
1350450
```
---
### Модуль mathematics
#### 1. Функция is_prime
Синтаксис: **is_prime(n: int) -> bool**

Для чего: 

    Если n - простое, то возващается True, иначе - False.
Пример использования #1:
```python
from infEGE import is_prime

print(is_prime(5))
```
Вывод:
```
True
```
Пример использования #2:
```python
from infEGE import is_prime

print(is_prime(25))
```
Вывод:
```
False
```
Пример использования #3:
```python
from infEGE import is_prime

print(is_prime(1))
```
Вывод:
```
False
```
---
#### 2. Функция is_even
Синтаксис: **is_even(n: int) -> bool**

Для чего: 

    Если n - чётно, то возващается True, иначе - False.
Пример использования #1:
```python
from infEGE import is_even

print(is_even(12))
```
Вывод:
```
True
```
Пример использования #2:
```python
from infEGE import is_even

print(is_even(25))
```
Вывод:
```
False
```
---
#### 3. Функция is_odd
Синтаксис: **is_odd(n: int) -> bool**

Для чего: 

    Если n - нечётно, то возващается True, иначе - False.
Пример использования #1:
```python
from infEGE import is_odd

print(is_odd(12))
```
Вывод:
```
False
```
Пример использования #2:
```python
from infEGE import is_odd

print(is_odd(25))
```
Вывод:
```
True
```
---
#### 4. Функция divided
Синтаксис: **divided(n: int, d: int) -> bool**

Для чего: 

    Если n делится на d, то возващается True, иначе - False.
Пример использования #1:
```python
from infEGE import divided

print(divided(12, 5))
```
Вывод:
```
False
```
Пример использования #2:
```python
from infEGE import divided

print(divided(121, 11))
```
Вывод:
```
True
```
---
#### 5. Функция not_divisible
Синтаксис: **not_divisible(n: int, d: int) -> bool**

Для чего: 

    Если n не делится на d, то возващается True, иначе - False.
Пример использования #1:
```python
from infEGE import not_divisible

print(not_divisible(12, 5))
```
Вывод:
```
True
```
Пример использования #2:
```python
from infEGE import not_divisible

print(not_divisible(121, 11))
```
Вывод:
```
False
```
---
#### 6. Функция factorial
Синтаксис: **factorial(n: int) -> int**

Для чего: 

    Возвращает n! (0! = 1)
Пример использования:
```python
from infEGE import factorial

print(factorial(6))
```
Вывод:
```
720
```
---
#### 7. Функция factorize
Синтаксис: **factorize(number: int) -> list**

Для чего: 

    Возвращает разложение числа number на простые множители в list.
Пример использования #1:
```python
from infEGE import factorize

print(factorize(1))
```
Вывод:
```
[]
```
Пример использования #2:
```python
from infEGE import factorize

print(factorize(11))
```
Вывод:
```
[11]
```
Пример использования #3:
```python
from infEGE import factorize

print(factorize(55))
```
Вывод:
```
[5, 11]
```
---
#### 8. Функция divisors
Синтаксис: **divisors(n: int) -> list**

Для чего: 

    Возвращает все натуральные делители числа n на интервале (1; n).
Пример использования #1:
```python
from infEGE import divisors

print(divisors(1))
```
Вывод:
```
[]
```
Пример использования #2:
```python
from infEGE import divisors

print(divisors(720))
```
Вывод:
```
[2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 30, 36, 40, 45, 48, 60, 72, 80, 90, 120, 144, 180, 240, 360]
```
---
#### 9. Функция fib
Синтаксис: **fib(n: int) -> int**

Для чего: 

    Возвращает n-ый член последовательности Фибоначчи. Нумерация с 0.
Пример использования #1:
```python
from infEGE import fib

print(fib(0))
```
Вывод:
```
0
```
Пример использования #2:
```python
from infEGE import fib

print(fib(1))
```
Вывод:
```
1
```
Пример использования #3:
```python
from infEGE import fib

print(fib(2))
```
Вывод:
```
1
```
Пример использования #4:
```python
from infEGE import fib

print(fib(3))
```
Вывод:
```
2
```
Пример использования #5:
```python
from infEGE import fib

print(fib(2001))
```
Вывод:
```
6835702259575806647045396549170580107055408029365524565407553367798082454408054014954534318953113802726603726769523447478238192192714526677939943338306101405105414819705664090901813637296453767095528104868264704914433529355579148731044685634135487735897954629842516947101494253575869699893400976539545740214819819151952085089538422954565146720383752121972115725761141759114990448978941370030912401573418221496592822626
```
**Примечание**: Данный алгоритм работает быстрее рекурсивного! Асимптоматика: O(N)