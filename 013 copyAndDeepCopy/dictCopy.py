# a = {'a': 2, 'b': 3}
#
# b = a
# b['a'] += 1
# print(a, b)

# a = {'a': 2, 'b': 3}
#
# b = a.copy()
# b['a'] += 1
# print(a, b)

# a = {'a': [1, 1, 2, 3], 'b': [2, 2, 4, 5]}
#
# b = a.copy()
# b['a'].append(999)
# print(a, b)  # 遭了

from copy import deepcopy

a = {'a': [1, 1, 2, 3], 'b': [2, 2, 4, 5]}
b = deepcopy(a)
b['a'].append(999)
print(a, b)
