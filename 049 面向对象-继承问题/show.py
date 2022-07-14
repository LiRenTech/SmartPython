# -*- encoding: utf-8 -*-
"""
PyCharm show
2022年07月12日
by littlefean
"""
from typing import *


class Person:
    def __init__(self, name, gender, age, birthday):
        self.name: str = name
        self.gender: str = gender
        self.age: int = age
        self.birthday = birthday

    def test(self):
        # if date == self.birthday:
        #     self.age += 1
        ...

    def say(self):
        print(f"大家好我是一个人， 我的名字叫{self.name}")


class Student(Person):
    def __init__(self, score, class_, name, gender, age, birthday):
        super().__init__(name, gender, age, birthday)
        self._score: int = score
        self.class_: int = class_

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    def say(self):
        print(f"大家好我是学生， 我的名字叫{self.name}")


class Staff(Person):
    _MIN_SALARY = 4000

    def __init__(self, name, gender, age, birthday, baseSalary):
        super().__init__(name, gender, age, birthday)
        self._salary = baseSalary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = max(value, self.__class__._MIN_SALARY)


class Teacher(Staff):

    def __init__(self, class_list, salary, name, gender, age, birthday):
        super().__init__(name, gender, age, birthday, salary)
        self.class_list: list = class_list

    def say(self):
        print(f"大家好我是老师， 我的名字叫{self.name}")


class Guard(Staff):
    def __init__(self, salary, name, gender, age, birthday):
        super().__init__(name, gender, age, birthday, salary)
        self._dutyRecordSheet = []

    def showSheet(self):
        print(self._dutyRecordSheet)

    def sheetAppend(self, item):
        self._dutyRecordSheet.append(item)

    def say(self):
        print(f"大家好我是老师， 我的名字叫{self.name}")


def main():
    return None


if __name__ == "__main__":
    main()
