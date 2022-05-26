from collections import OrderedDict

dic = {}
o = OrderedDict()
string = "aoiwevnaekl"
for char in string:
    dic[char] = 1
    o[char] = 1

print(dic)
print(o)

dic.pop("o")
o.pop("o")

print(dic)
print(o)

# 3.7 字典和orderedDict一样有顺序了

