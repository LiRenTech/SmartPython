def f():
    a = [[], []]

    def g():
        a[0].append(111)
        print(a)
        print(id(a[0]), id(a[1]))

    return g


g1 = f()
g2 = f()

g1()
g1()
g1()
g2()
g2()
