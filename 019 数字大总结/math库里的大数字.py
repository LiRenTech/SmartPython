# import mpmath  # 这个是一个第三方库了，先不管了
import math
import cmath

print(math.e)

print(math.nan, type(math.nan))
print(math.nan + 5)
print(math.nan + math.nan)
# print(math.nan + "???")  # 不能这样
# print("???" + math.nan)
# print(f"({math.nan})")


# math和cmath区别

print(dir(math))
print(dir(cmath))
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 ^ s2)  # 两者不同的
print(s1 - s2)  # s1有，s2没有的
print(s2 - s1)  # s2有，s1没有的

cmathSet = set(dir(cmath))
mathSet = set(dir(math))
print("cmath 独有的", cmathSet - mathSet)
print("math 独有的", mathSet - cmathSet)

# cmath 里含有虚数  'nanj', 'infj'
print(cmath.polar(1 + 1j))

# 向上取整，向下取整可以int。

print(math.gcd(6, 3))  # 3.9 里变成了不定长参数类型了
print(math.hypot(3, 4))  # 勾股定理函数
print(math.log(5, 5))
print(math.log(5, 25))
print(math.log(25, 5))
print(math.log(125, 5))  # 3.0000000000000004  稍微有点误差
print(math.log10(1000))  # 3.0
# print(math.log10(-1))

print(math.log2(8))  # 3
print(math.log1p(math.e - 1))  # 以e为底，传入的参数自动+1了

# 可以比较sqrt和**0.5谁更快
print(math.sqrt(16) == 16 ** 0.5)
# e ** x 和 exp 谁快
print(math.e ** 5 == math.exp(5))

print(math.degrees(math.pi))  # 转角度  写前端的时候经常写 30deg,90deg 所以deg是转角度
print(math.radians(30))  # 转弧度

math.cosh(3)  # 悬链线

