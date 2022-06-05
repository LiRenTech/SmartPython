from random import random


def f():
    return f if random() < 0.5 else g()


def g():
    return f() if random() < 0.5 else g


print(f()()()()()())
print(f()()()()()())
print(f()()()()()())
print(f()()()()()())
print(f()()()()()())

