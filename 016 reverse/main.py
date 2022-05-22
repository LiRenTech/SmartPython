"""reverse"""

string = "abcde"
print(string[::-1])
print(string)

string = reversed(string)
print(string)  # 不是字符串了，是一个对象了
for char in string:
    print(char, end=",")
print()

arr = [1, 2, 3, 4, 5]

print(arr[::-1])
print("A:", arr)
arr.reverse()
print("B:", arr)
res = arr.__reversed__()  # reversed(...)
print(res)
print("C:", arr)
res = reversed(arr)
print(res)

# apply

array = [3, 1, 4, 1, 5, 9, 2, 6]
for n in reversed(array):
    print(n, end=" ")
print()
print(array)

for i, n in enumerate(reversed(array)):
    print(f"{i, n}", end=" ")
print()

for i, n in reversed(list(enumerate(array))):  # 内外翻转
    print(f"{i, n}", end=" ")
print()
