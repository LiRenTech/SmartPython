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
                a = 5

                def J():
                    a = 6
                    print("....")
                    return f

                return J

            return I

        return h

    return g


# f()()()()()
# f.__call__().__call__().__call__().__call__().__call__()

for i in range(5):
    # f = f.__call__()
    f = f()
