"""
传统的抽象工厂模式

抽象工厂模式是一种创建型设计模式，
它提供一个创建一系列相关或相互依赖对象的接口，
而无需指定它们具体的类。

在抽象工厂模式中，
一个工厂接口负责创建相关对象，
而子类则负责实现这些对象的创建。


北京工厂、上海工厂、广州工厂等，
这些所有的工厂都统一写一个接口，这个工厂的接口就是抽象工厂。
抽象工厂不能说是生产工厂的工厂，而是工厂的统一规定，工厂的接口。

抽象工厂模式的选择是基于工厂模式的类写法来的。

1 工厂方法写在类本身中
2 工厂方法单独写在一个类中（工厂类）
3 工厂类被统一成一个接口（抽象工厂类）
"""


class AbstractFactory(object):
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()


class AbstractProductA(object):
    pass


class ConcreteProductA1(AbstractProductA):
    pass


class ConcreteProductA2(AbstractProductA):
    pass


class AbstractProductB(object):
    pass


class ConcreteProductB1(AbstractProductB):
    pass


class ConcreteProductB2(AbstractProductB):
    pass
