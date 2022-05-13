# s1 = {1, 2, 3}
# s2 = s1
#
# s1.add(1000)
# print(s1, s2)  # no


# s1 = {1, 2, 3}
# s2 = s1[:]  # No!
# s1.add(1000)
# print(s1, s2)


# s1 = {1, 2, 3}
# s2 = s1.copy()
# s1.add(1000)
# print(s1, s2)

# s1 = {1, [1, 2, 3], 3}  # 集合里面的类型都是不可变的，所以不用担心拷贝的问题，只用浅拷贝就行
s1 = {1, (1, 2, 3), 3}
s2 = s1.copy()
s1.remove((1, 2, 3))
print(s1, s2)

from copy import deepcopy
