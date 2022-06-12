from random import random

a = 1
import sys
sys.setrecursionlimit(1000000)


def f():
    global a
    a *= 2
    print(a)
    return f if random() < 0.00001 else f()


f()