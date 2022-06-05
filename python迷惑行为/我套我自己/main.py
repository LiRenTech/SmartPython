arr = []
arr.append(arr)
print(arr)

a = []
b = []
a.append(b)
b.append(a)

print(a)

a1 = ["a1"]
a2 = ["a2"]
a3 = ["a3"]
a1.append(a3)
a2.append(a1)
a3.append(a2)
print(a1)
print(a2)
print(a3)
