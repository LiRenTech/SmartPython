"""
闭包函数访问可变数据类型测试

"""


def f():
    arr = []
    f.n += 1

    def visit():
        print(arr, id(arr))

    def push(v):
        for i in range(f.n):
            arr.append(v)

    return visit, push


f.n = 0

v1, p1 = f()
v2, p2 = f()

p1(12)
p2(10)
v1()
v2()
p1(12)
p2(10)
v1()
v2()
