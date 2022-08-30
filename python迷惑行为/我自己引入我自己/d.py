import d as dd


# import d as dd
# import d as ddd
# 最多只能引入一次，然后执行会执行两次

def j(n):
    return 1 if n < 1 else j(n - 1) * n


print(dd.j(3))
import d as ddd

print(ddd.j(5))
