"""
and 链条会拿到第一个 bool(?) == False 的，如果没有False，就拿到最后一个值
潜台词：遇到 False就不用再看了，肯定废辣！

or 链条会拿到第一个  bool(?) == True 的，如果没有True，就拿到最后一个值
潜台词：遇到 True 就不用再看了，肯定稳辣！

优先级
not > and > or

用途：找到第一个转换后不是False的，用or链条
value = a or b or c or d or default_value

and用法：
result = x > y and "x太小" or "x很好"

value = a and b and c and d
这样的赋值语句将给 value 赋予 a、b、c 和 d 中第一个为假的值（或者最后一个为真的值）。

例如你想挑选第一个空数组并添加东西
select_arr = arr1 and arr2 and arr3 and default_arr

"""


def main():
    f5()
    pass


def f1():
    a = [12, 41, 4]
    b = 114
    c = 0
    d = None
    e = False

    res = a and b and c and d and e
    print(res)


def f2():
    a = [1]
    b = [2, 4, 6]
    c = [4445]
    d = [444]
    print(a and b and c and d)
    pass


def f3():
    a = []
    b = [2, 4, 6]
    c = []
    d = [444]
    print(a or b or c or d)


def f4():
    a = []
    b = help
    c = None
    d = ()
    print(a or b or c or d)


def f5():
    # 优先级测试 and or
    def g1():
        print(1)

    def g2():
        print(2)

    def g3():
        print(3)

    g1() and g2() or g3()

    # [g1() and g2()] or g3()

    # g1() and [g2() or g3()]

    pass


if __name__ == '__main__':
    main()
