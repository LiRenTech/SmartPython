import math

arr = [
    float("inf"),
    float("-inf"),
    -float("inf"),
    -----------------------------float("inf"),

    # 大小写随便玩
    float("INF"),
    float("Inf"),
    float("iNf"),
    float("inF"),
    # float("Infity"),
    type(float("inf")),  # float 类型
]

print(math.inf)
print(type(math.inf))
print(float("INF") == math.inf)
print(float("INF") is math.inf)
print(id(float("INF")), id(math.inf))

arr = [math.inf, math.inf, float("INF"), float("inF"), float("INF")]

print("----")
for obj in arr:
    print("\t", id(obj))
print("----")
# math库里的对象都是一个地址，但是float直接生成出来的都是不一样的
# 想节省内存的话，可能用math库里的更好
# 如果只是简单用到一两个，可以不用import math库，直接写float

# 关于无穷的一些运算
print(float("INF") == float("INF") + 1)

arr = [1, 2, 4, 7, 2, 6, 2, 5]
res = float("-INF")
for i, n in enumerate(arr):
    if n > res:
        res = n
print(res)

