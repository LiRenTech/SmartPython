


def f(x):  # 是否是3的倍数
    if x % 3 == 0:
        return True
    else:
        return False  # 写的稍微臭了点


print(list(filter(f, [1, 6, 89, 345, 12])))
from itertools import filterfalse
print(list(filterfalse(lambda x: not x % 3, [1, 6, 89, 345, 12])))

from itertools import compress

