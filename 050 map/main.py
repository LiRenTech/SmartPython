# oj算法题输入
a, b = map(int, input().split())

# 自己快速写一个举例列表
list_of_ints = list(map(int, "1234567"))


# 转大写
def upper(s):
    return s.upper()


lst = list(map(upper, ['sentence', 'fragment']))
print(lst)
# ['SENTENCE', 'FRAGMENT']
