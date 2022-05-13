# a = [1]
# a.append(1)
b = (1,)
for i in range(10000):
    b += (1,)
print(b)
