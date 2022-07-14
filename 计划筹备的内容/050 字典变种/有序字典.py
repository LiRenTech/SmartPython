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


# from sortedContainers import SortedDict
# 2022年5月28日 看力扣杯困难题发现的   这他娘的是第三方库



