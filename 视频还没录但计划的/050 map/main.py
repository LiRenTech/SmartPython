# oj算法题输入
a, b = map(int, input().split())
# a, b = map(int, ["15", "20"])
# a, b = int("15"), int("20")
# 自己快速写一个举例列表
list_of_ints = list(map(int, "13 15 45 84 23 21".split()))

print(list_of_ints)

map(pow, [1, 2, 3, 4])


# 转大写
def upper(s):
    return s.upper()


lst = list(map(upper, ['sentence', 'fragment']))
lst = list(map(str.upper, ['sentence', 'fragment']))
print(lst)
# ['SENTENCE', 'FRAGMENT']
