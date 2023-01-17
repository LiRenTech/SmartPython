"""
关于关键字的探索
"""
a = 1


def f():
    a = 2

    def g():
        a = 3

        def h():
            a = 4

            def I():
                nonlocal a
                a = 5
                print(a)

                def J():
                    a = 6
                    print("....")

                return J

            return I

        return h

    return g


# f()()()()()
# f.__call__().__call__().__call__().__call__().__call__()

for i in range(5):
    # f = f.__call__()
    f = f()

print(a)