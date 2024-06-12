from abc import ABCMeta, abstractmethod
from typing import Dict


class SingletonMeta(type):
    _instances: Dict[type, object] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    pass


class MyABC(metaclass=ABCMeta):
    @abstractmethod
    def f(self):
        pass


class MyClassA(Singleton, MyABC):
    def f(self):
        print('A')


class MyClassB(Singleton, MyABC):
    def f(self):
        print('B')


def main():
    s1 = Singleton()
    s2 = Singleton()
    print(id(s1), id(s2))  # 打印两个对象的id，可以看到它们是同一个对象
    a1 = MyClassA()
    a2 = MyClassA()
    b1 = MyClassB()
    b2 = MyClassB()
    a1.f()  # A
    a2.f()  # A
    b1.f()  # B
    b2.f()  # B


if __name__ == '__main__':
    main()
