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


class TestEnum(IntEnum):
    AIR = 0
    DIRT = 1
    ROCK = 2
    GRASS = "3"  # 没有起到检查的作用
