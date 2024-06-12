"""
工厂模式举例

1. 直接写在类的静态方法中
"""


class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @staticmethod
    def get_zero() -> 'Vector':
        # 目的：简化参数，可以直接通过类名调用静态方法
        return Vector(0, 0)

    @staticmethod
    def get_random() -> 'Vector':
        # 目的：简化参数，可以直接通过类名调用静态方法
        import random
        return Vector(random.randint(0, 100), random.randint(0, 100))

    pass
