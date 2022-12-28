from sys import setrecursionlimit
setrecursionlimit(2147483647)  # c int最大值
# setrecursionlimit(2147483648)  # 超过2147483647就报错
def func():
    exec(func.__code__)
func()