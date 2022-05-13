import time


def timer(time_type):
    print(time_type)

    def outer(func):
        print("func的名字是：", func.__name__)

        def inner(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            res = end - start
            print('时间结果是：', res)

        return inner

    return outer


@timer('min')  # foo = timer(foo)
# @outer
def foo(a, b, c):
    print('in foo', a, b, c)


foo('woniu', 'gfifigf', '79846543635')
