import inspect


def myStrHash(string: str) -> int:
    res = 0
    for i, char in enumerate(string):
        res += ord(char) ** (i + 1)
        res %= 1000
    return res


def func():
    """
    这个函数巴拉巴拉
    我是一个***
    :return:
    """
    ...
    ...
    print("hello")


def judge():
    try:
        content = inspect.getsource(func)
        code = myStrHash(content)
        if code == 341:
            # 答对了
            print("我的代码没有被修改")
            ...
        else:
            # 被修改了
            print("我的代码被修改了！")
            import email
            # email.send(user, password, content)
            ...
    except NameError:
        print("我的函数被改名了或者被删除了！")


def judge2():
    with open("main.py") as f:
        c = f.read()
    print(myStrHash(c))
    ...


def main():
    # func()
    judge()
    ...


if __name__ == "__main__":
    main()
