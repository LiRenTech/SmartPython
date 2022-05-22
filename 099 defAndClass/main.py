import self


def f():
    def g():
        def h():
            ...


class A:
    class B:
        class C:
            class D:
                class E:
                    ...


class AB:
    def __init__(self):
        self.name = None

    def f1(self):
        self.name = 1

        class BA:
            def f2(self):
                ...


def func():
    class Q:
        def f2(self):
            class P:
                ...
