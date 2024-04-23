# print.f = print
print_ = print


def print(*args, **kwargs):
    print_(*args, **kwargs)
    return print_


print("hello")("world")
