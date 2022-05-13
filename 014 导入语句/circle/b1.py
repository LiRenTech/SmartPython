from b2 import g1  # 直接报错！循环导入


def f1():
    print("f1运行了")
    ...


def f2():
    print("f2运行了")
    ...


def main():
    print("main运行了")
    # from b2 import g1  # 内部导入就没事了
    g1()
    ...


if __name__ == '__main__':
    main()
