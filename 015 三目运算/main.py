"""
三目运算符是什么意思？
这个目又叫元，就是变量的个数

一目运算符，又叫一元运算，只参与一个数字，或者表达式
not(...)  3! = 6

二元运算符
__ 运算符 __
a + b

三目运算符，
__ 运算符 __ 运算符 __
三目运算符有两个符号组成，这两个符号把整个一行分成了三个部分，这三个部分里写你想要写的东西

如果你是一个数学家，你可以发明四目运算符了
__ 运算符 __ 运算符 __ 运算符 __

"""

a = 15

# if a == 15:
#     print("yes")
# else:
#     print("no")


# 以下两个写法哪个才是正确的？
a == 15 if print("yes1") else print("no1")

print("yes2") if a == 15 else print("no2")

# 原理解释
# if None:
#     print("111")
# else:
#     print("222")
#
# print(bool(None))

# if print("in if"):
#     print("111")
# else:
#     print("222")

# 可以简化成一行，但是没必要，看着不舒服
# if a < 100: print(122)
# for 也可以简化成一行
# for i in range(10): print(i)

# 注意： 和js写法是不一样的
"""
var age = 15;
console.log(age<18 ? '未成年' : '成年');
js.json 里的判断条件是在左边，中间是成立条件，右边是不成立条件
区别对比：
python中间是条件，左边挨着if的时成立，else的时不成立，这个从单词角度就很好记忆
js.json、C语言，java、C++、php里的写法都一样符号也都一样，唯独python不一样。
约？可：爬

如果你最开始学的不是python，你可能就会好奇感觉自己三目运算符总是写不对
于是就不想用python写三目运算符了。

顺便补充一句。Go语言没有三目运算符，他们觉得可读性很低，没必要炫技术。
如果python是你第一个学习的语言，那么你一定要区别清楚这个三目运算符

学习三目运算符的意义：
1 别人这样写你能看懂
2 看懂一些源码，第三方库
3 可以多一种写代码的方式，抄作业不容易被看成雷同代码
4 想发挥一行代码炫技的极简精神，就要熟练掌握这个
"""

# 带返回值
# b = print(111) if True else print(222)
# print(b)
# b = print(111) if False else print(222)
# print(b)
#
# age = 15
# res = "可以进入" if age >= 18 else "不可以进入"
# print(res)

# 嵌套写法
score = 83
if score in range(101):
    if score < 60:
        print("不合格")
    else:
        print("合格")
else:
    print("成绩错误")

# ... if score in range(101) else ...

# ... if score in range(101) else print("成绩错误")

print("不合格") if score < 60 else print("合格") if score in range(101) else print("成绩错误")

# 如果你看到你的队友和你合作项目写了这样的代码，立刻把它的代码改成普通写法，并告诉他不要炫技

# if  elif  else 多分支可以简化成一行吗?
name = "xxx"

if not name:
    print("空")
elif name == "张三":
    print("找到人了")
else:
    print("没找到")

# print("空") if name == "" elif print("找到人了") else print("没找到")
# 这成了四目运算符了，没有这样的写法

# 小应用，让一个函数只有一半的几率区执行它

from random import random


def do():
    ...


if random() < 0.5:
    do()

# if random(): do()  # 这样写pycharm会有小警告，让强迫症的你不舒服
# do () if random() < 0.5 else pass   # 不能写pass，要换成点点点，
# 以前的视频里有讲过pass和点点点的区别，不知道的可以去看一下我以前的视频
do() if random() < 0.5 else ...
