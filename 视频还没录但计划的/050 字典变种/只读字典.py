from types import MappingProxyType

mpt = MappingProxyType({2: 1, 4: 5})
print(mpt)

# mpt[1000000] = 1000  # 尝试修改添加，编辑器已经开始警告了
#
# mpt[1000000] = 1000  # 尝试修改添加，编辑器已经开始警告了

print(mpt)

# 这有什么用呢？？

print(mpt[2])  # 保留了查询的功能


# 字典key套字典？

# a = {
#     mpt: 123
# }
# print(a)
# s = {mpt}
# 套个der啊，不能套


class M:
    count = 0

    def __init__(self):
        self.name = 15


print(type(M.__dict__))
# 类的属性就是一种映射代理类型
print(type(M().__dict__))
