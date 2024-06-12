"""
工厂模式 - 单独写一个工厂类的情况举例
"""
from abc import ABCMeta, abstractmethod


class ResultType(metaclass=ABCMeta):
    VALUE = 0

    @abstractmethod
    def f(self):
        pass

    pass


class A(ResultType):
    VALUE = 1

    def f(self):
        pass


class B(ResultType):
    VALUE = 2

    def f(self):
        pass


class C(ResultType):
    VALUE = 3

    def f(self):
        pass


class Factory:

    @staticmethod
    def create_object(type_name):
        """
        但是这种情况可以直接被一个全局函数代替，不需要单独写一个工厂类
        """
        if type_name == 'A':
            return A()
        elif type_name == 'B':
            return B()
        elif type_name == 'C':
            return C()
        else:
            raise ValueError('Invalid type name')

    COUNT = 0

    @classmethod
    def create_object_by_score(cls, score: int) -> ResultType:
        """
        但是如果需要记录创建对象的次数，可以用类方法来实现
        这种情况的使用场景还有可能有：
        1. 记录创建对象的次数
        2. 在创建对象时，会对其他环境产生依赖或者修改全局状态，可以用工厂模式来封装这些操作
        """
        cls.COUNT += 1
        if score >= 80:
            return A()
        elif score >= 60:
            return B()
        elif score >= 40:
            return C()
        else:
            raise ValueError('Invalid type name')


def main():
    obj1 = Factory.create_object('A')
    obj2 = Factory.create_object('B')
    obj3 = Factory.create_object('C')
    print(obj1, obj2, obj3)


if __name__ == '__main__':
    main()
