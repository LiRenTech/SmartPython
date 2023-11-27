class Calculator:
    def __init__(self):
        self._value = 0

    def __getattr__(self, item):
        return self

    def __truediv__(self, other):
        return self

    def __floordiv__(self, other):
        return self


https = www = index = Calculator()

https//www.littlefean.com/index.html
