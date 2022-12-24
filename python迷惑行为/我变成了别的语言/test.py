from typing import Set
import operator as op

var = {}


class MyCode:
    # def __init__(self):
    #
    index = 0

    def __hash__(self):
        MyCode.index += 1
        return MyCode.index

    def do(self):
        ...


class SetValue(MyCode):
    """预处理语句"""

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def do(self):
        var[self.name] = self.value

    def __str__(self):
        return "<SetValue>"


class GetValue(MyCode):
    def __init__(self, name):
        self.name = name

    def do(self):
        return var[self.name]


class ChangeValue(MyCode):
    def __init__(self, name, dv, op):
        self.name = name
        self.dv = dv
        self.op = op

    def do(self):
        var[self.name] = self.op(var[self.name], self.dv)


class Op(MyCode):
    def __init__(self, name, operator, value):
        self.name = name
        self.operator = operator
        self.value = value

    def do(self):
        return self.operator(var[self.name], self.value)


class Judge(MyCode):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def do(self):
        return var[self.name] == self.value

    def __str__(self):
        return "<Judge>"


class If(MyCode):
    def __init__(self, *args, **kwargs):
        if len(args) == 4:  # if (condition) {} else {}
            self.condition: Judge = args[0]
            self.doCode: Set[MyCode] = args[1]
            self.elseDo: Set[MyCode] = args[3]
        elif len(args) == 2:
            self.condition: Judge = args[0]
            self.doCode: Set[MyCode] = args[1]
            self.elseDo: Set[MyCode] = set()

    def do(self):
        if self.condition.do():
            for code in self.doCode:
                code.do()  # bug
        elif self.elseDo:
            for code in self.elseDo:
                code.do()

    def __str__(self):
        return "<IF>"


class Cmp(MyCode):

    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def do(self):
        leftVal, rightVal = self.left, self.right
        if isinstance(self.left, MyCode):
            leftVal = self.left.do()
        if isinstance(self.right, MyCode):
            rightVal = self.right.do()
        return self.operator(leftVal, rightVal)


class For(MyCode):
    def __init__(self, initContent, judgeContent, loopContent, loopCode):
        self.initContent = initContent
        self.judgeContent = judgeContent
        self.loopContent = loopContent
        self.loopCode: Set[MyCode] = loopCode

    def do(self):
        self.initContent.do()
        while self.judgeContent.do():
            for code in self.loopCode:
                code.do()
            self.loopContent.do()

    ...


class Print(MyCode):
    def __init__(self, string):
        self.string = string

    def do(self):
        if isinstance(self.string, str):
            print(self.string)
        elif isinstance(self.string, MyCode):
            print(self.string.do())


class NameSpace:
    def __init__(self, *args):
        self.arr = args

    def run(self):
        for code in self.arr:
            code.do()


#
# ns = NameSpace(
#     SetValue("a", 1),
#     If(
#         Judge("a", 1),
#         {
#             For(SetValue("i", 0), Cmp("i", op.lt, 5), ChangeValue("i", 1, op.add), {
#                 ChangeValue("a", 10, op.add)
#             }),
#         }
#     ),
# )

# 打印出0~1000内左右的偶数
ns = NameSpace(
    For(SetValue("x", 0), Cmp(GetValue("x"), op.lt, 1000), ChangeValue("x", 1, op.add), {
        If(Cmp(Op("x", op.mod, 2), op.eq, 0), {
            Print(GetValue("x"))
        })
    })
)


def main():
    from collections import Counter, defaultdict
    words = """abc bca acb
apple pplea
cat""".split()

    # {sortedStr: [words]}
    d = defaultdict(list)
    for word in words: d["".join(sorted(word))].append(word)
    print(d)
    # print(a, dict(a))
    (print(arr) for arr in d.values() if len(arr) >= 3)


    # print(Counter("".join(sorted(item)) for item in words).most_common(3))

    # dic = defaultdict(int)
    # for word in words:
    #     dic["".join(sorted(word))] += 1

    ns.run()
    # print(type(scope))
    # for cc in scope:
    #     print(cc)
    #     print(type(cc))
    #     print(dir(cc))
    #     cc.do()
    #
    print(var)


if __name__ == "__main__":
    main()
