"""
三层嵌套
"""


def f():
    a = 1

    def g():
        b = 1
        print(a)

        def h():
            print(a, b)

        return h

    return g


g1 = f()
h1 = g1()

print(g1.__closure__)
print(h1.__closure__)
