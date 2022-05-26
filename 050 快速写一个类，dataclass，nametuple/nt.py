from collections import namedtuple

# 两种方法来给 namedtuple 定义方法名
User = namedtuple('User', ['name', 'age', 'id'])
user = User('tester', '22', '464643123')

print(user)
# User(name='tester', age='22', id='464643123')

# *--------------------------------
# https://www.manongdao.com/article-2068272.html
from enum import IntEnum

NAME, AGE, SEX, EMAIL = range(4)
s = ('jim', 16, 'male', 'jim8721 @ gmail.com')


class StudentEnum(IntEnum):
    NAME = 0
    AGE = 1
    SEX = 2
    EMAIL = 3


print(StudentEnum.NAME)
print(s[StudentEnum.NAME])
isinstance(StudentEnum.NAME, int)
