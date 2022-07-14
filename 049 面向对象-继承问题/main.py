# -*- encoding: utf-8 -*-
"""
PyCharm main
2022年07月07日
by littlefean
"""
from typing import *


class A:
    ...


class B(A):
    ...


def main():
    # 为什么需要继承
    # 当发现一个类A和一个类B有公共的属性或者方法的时候，
    # 就可以把这公共的部分摘出来，写成一个更具有抽象意义的类
    # 然后就相当于简写代码了，也更方便维护，修改的时候不用修改两个地方了。
    # 怪物打建筑，建筑攻击怪物，怪物和建筑都有面积，位置，速度，血量，他们就可以抽象出来
    # 提出公共部分叫圆形实体类

    # 如何查看继承的类
    print(B.__bases__)
    print(A.__bases__)

    # int float 都是继承自 object类

    # object 和 type 的区别
    # object 类被 type 实例化
    # type 继承自 object

    # 带两个头下划线的不能继承，这是私有

    # 受保护的应用场景
    # 私有的应用场景

    B.age = 15
    # 如果A类已经有了age属性，这个age属性其实不是改父类的，是给自己类新加了一个属性

    # 查看继承链条顺序
    print(B.mro())
    print(B.__mro__)
    import inspect
    print(inspect.getmro(B))

    # 看这个顺序的意义：
    # 资源覆盖重写，类属性，类方法 看调用的是哪一个

    # 但是要注意cls 和self 方法的问题
    class C1:
        @classmethod
        def test(cls):
            print(cls)

    class C2(C1):
        ...

    c = C2()
    c.test()  # 虽然那个方法写在C1里，但是却是C2 的
    # 解释：谁在调用这个test方法，传递过来的cls就是谁
    # 实例方法 self也是一样，谁调用这个方法，传过来的self就是谁

    # 资源的累加，就相当于画集合圈


    return None


def think():
    # 单继承链、多继承链、菱形继承

    # 可以举例继承的例子：

    # 怪物，炮塔，继承自圆形实体类

    ...


if __name__ == "__main__":
    main()
