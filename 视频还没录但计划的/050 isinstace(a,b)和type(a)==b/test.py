class A:
    ...


class B(A):
    ...


class C(B):
    ...


b = B()
c = C()

print(type(b))  # <class '__main__.B'>
print(type(b) == A)  # False
print(isinstance(b, A))  # True

print(type(c))  # <class '__main__.C'>
print(type(c) == A)  # False
print(type(c) == B)  # False
print(isinstance(c, A))  # True
print(isinstance(c, B))  # True

# isinstance可以识别继承
# 这只是个demo，录视频的时候可以加更多东西
