dic = {}
lst = []

dic[1] = lst
lst.append(dic)

print(dic)
print(lst)

print("-" * 100)

t = ()
print(t)
t += t

print(t)

t = (..., )
print(t)
t += t

print(t)