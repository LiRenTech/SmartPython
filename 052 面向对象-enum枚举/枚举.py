# *--------------------------------
# https://www.manongdao.com/article-2068272.html

# 3.4 新加的
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

# 枚举的用途在于相当于很简洁的声明了常量
# TestEnum.AIR = 15  # 修改会报错

# 中键点击去之后还会有更多的东西
