from sys import setrecursionlimit
setrecursionlimit(2147483647)  # c int最大值
# setrecursionlimit(2147483648)  # 超过2147483647就报错
with open(__file__, "r", encoding="u8") as f:
    exec(f.read())
# 运行结束记得看退出代码
# cmd查看方法：echo %errorlevel%
# pycharm查看方法：运行结果最后