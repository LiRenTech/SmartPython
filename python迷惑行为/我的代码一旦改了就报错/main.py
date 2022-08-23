"""
我们在和队友合作的时候，我写了一个函数，然而我希望自己的函数里面的内容，每一个字符
都不能被修改，如何做到不能让它被修改呢？
如果检测方法只能在这个函数里面呢？===>非常难以解决

"""
import hashlib


def a():
    aa = "sdfassdfsdfa"
    print(eval(f"0x{str(hashlib.sha256(aa.encode()).hexdigest())}") % 1000)


def func():
    import inspect
    content = inspect.getsource(func)
    code = sum(ord(char) ** (i + 1) for i, char in enumerate(content)) % 1000

    if code == 401:
        # 答对了 恭喜你
        print("我的代码没有被修改")
    else:
        # 被修改了
        print("我的代码被修改了！")
    print("hello")


def force():
    """
    把函数代码粘贴到a多行字符串中，在需要检测的地方写code。
    暴力计算出这个字符串应该等于多少
    :return:
    """

    def myStrHash(string: str) -> int:
        """
        自定义实现的将字符串转化成哈希值的做法
        把每一个char = str[i]转换成 char的标号 的 i+1次方 累加
        返回的是一个小整数，压缩在1000之内
        """
        res = sum(ord(char) ** (i + 1) for i, char in enumerate(string))
        return res % 1000

    for code in range(1000):

        a = f"""def func():
    import inspect
    content = inspect.getsource(func)
    code = sum(ord(char) ** (i + 1) for i, char in enumerate(content)) % 1000

    if code == {code}:
        # 答对了 恭喜你
        print("我的代码没有被修改")
    else:
        # 被修改了
        print("我的代码被修改了！")
    print("hello")"""
        c = myStrHash(a)
        print(code, c)
        if c == code:
            print("破解了", code)
            break
    ...


def main():
    func()
    # force()
    # func()
    ...


if __name__ == "__main__":
    main()
