from collections.abc import Iterable
from functools import reduce

print(isinstance([], Iterable))
print(isinstance(1, Iterable))


# map & reduce
# =================
l1 = list(map(str, [1, 2, 3, 5]))
print(l1)


def add(x, y):
    return x + y


l2 = reduce(add, [1, 3, 5, 7, 9])
print(l2)


def appendStr(str1, str2):
    return str(str1) + str(str2)


l3 = reduce(appendStr, [1, 2, 3, 4, 5, 6])
print(l3)


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2num(str):
    return reduce(lambda x, y: x*10+y, map(char2num, str))


l4 = str2num('13579')
print(l4)


def normalize(s):
    return s[0].upper() + s[1:].lower()


L5 = ['adam', 'LISA', 'barT']
L6 = list(map(normalize, L5))
print(L6)

# filter
# =====================


def is_odd(n):
    return n % 2 == 1


l7 = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(l7)


def not_empty(s):
    return s and s.strip()


l8 = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(l8)

# sorted
# =====================
l9 = sorted([36, 5, -12, 9, -21], key=abs)
print(l9)
