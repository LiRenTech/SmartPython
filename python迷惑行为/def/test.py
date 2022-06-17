# def f(item):
#     del item
#     return f
#
#
# f(f)(f)

# error
def g(a):
    del g
    return a


# g(g)(g)

# a = [1, 2, 3]
# f(a)
# print(a)  # 无影响
#
# obj = object()
# help(obj)