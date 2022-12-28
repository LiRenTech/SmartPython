def f1():
    a = 15
    if a == 15:
        if a == 177:
            if a == 166:
                if a == 157:
                    if a == 1577:
                        if a == 1571:
                            if a == 1579:
                                print("VVV")
                            else:
                                print("BBB")
                        else:
                            print("AA")
                    else:
                        print("b")
                else:
                    print("c")
            else:
                print("d")
        else:
            print("e")
    else:
        print("f")


# py有个梗，拿尺子比着屏幕
# pycharm还算贴心，有竖线，以及自动显示
# 但是有人他就是不满意，他就是喜欢大括号，甚至因为这个能和别人打起来
# 我们可以魔改一下python，给他加上大括号


def f2():
    a = 15
    if (a == 15):
        {print(a)}
    else:
        {
            print("no")
        }

# 这样就可以了
# 解释 小括号是怎么回事，大括号是怎么回事
# import ast
# 美观打印一下发现是set

# 于是这样就有缺陷了，大括号里只能写函数调用语句，
# 不能赋值语句和其他循环判断语句
# 所以我们可以自己定义语句
