from typing import List


class Animal:
    def __init__(self, name):
        self.name = name


class Basketball:
    def __init__(self, name):
        self.name = name


class Car:
    def __init__(self, name):
        self.name = name


class Desk:
    def __init__(self, name):
        self.name = name


from abc import ABC, ABCMeta, abstractmethod


class Factory(ABC):
    FactoryLocation: List[int] = [100, 100]
    FactoryName: str = "Factory"

    @abstractmethod
    def test(self):
        pass

    FactoryCommentList: List[str] = []


class FactoryChina(Factory):
    FactoryLocation: List[int] = [100, 100]
    FactoryName: str = "China"
    FactoryCommentList: List[str] = []

    @staticmethod
    def get_animal(name):
        return Animal(name)

    @staticmethod
    def get_ball(name):
        return Basketball(name)

    def test(self):
        print(self)


class FactoryUSA(Factory):
    FactoryLocation: List[int, int] = [500, 200]
    FactoryName: str = "USA"
    FactoryCommentList: List[str] = []

    @staticmethod
    def get_car(name):
        return Car(name)

    @staticmethod
    def get_desk(name):
        return Desk(name)

    def test(self):
        print(self)


def main():
    a1 = FactoryChina.get_animal("dog")
    b1 = FactoryChina.get_ball("basketball")
    c1 = FactoryUSA.get_car("BMW")
    d1 = FactoryUSA.get_desk("desk")
    print(a1.name, b1.name, c1.name, d1.name)
