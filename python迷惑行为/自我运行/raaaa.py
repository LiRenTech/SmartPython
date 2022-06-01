import os

exec("""
a = 12
b = 13
print(a + b)
""")
print(__file__)
print(__file__.split("/"))
lst = __file__.split("/")[:-1]
print(lst)
print("/".join(lst))
print(os.listdir("/".join(lst)))
for item in os.listdir("/".join(lst)):
    print(item)
    with open(item, encoding="utf-8") as f:
        exec(f.read())

# 被检测到了无限递归，被迫终止
