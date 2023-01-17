a = 155


def f():
    global a
    print(a)
    a += 1


print(f.__closure__)
