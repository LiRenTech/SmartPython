# def f(item):
#     del item
#     return f
#
#
# f(f)(f)

# error
def g(a):
    del g
    # g(a)
    return a

# 所有起到缩进作用的语句
# g(g)(g)

# a = [1, 2, 3]
# f(a)
# print(a)  # 无影响
#
# obj = object()
# help(obj)
