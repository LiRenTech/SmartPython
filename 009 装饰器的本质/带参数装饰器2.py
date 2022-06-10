import time


def timer(time_type):
    """
    带参数的选择器
    timer() 加小括号调用结束之后，本身会变成一个不带参数的装饰器（小机器人）
    然后这个装饰器再对函数进行装饰
    """
    print(time_type)
    if time_type == "min":
        def robot(func):
            print("func的名字是：", func.__name__)

            def inner(*args, **kwargs):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                res = end - start
                print('时间结果是：', res)

            return inner
    else:
        def robot(func):
            print("func的名字是：", func.__name__)

            def inner(*args, **kwargs):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                res = end - start
                print('时间结果是：', res)

            return inner
    return robot


@timer('min')
def foo(a, b, c):
    print('in foo', a, b, c)


foo('a', 'bb', 'ccc')
