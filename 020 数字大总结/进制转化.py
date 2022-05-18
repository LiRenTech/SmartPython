# 进制转化问题
print(bin(6666))
print(oct(555))
print(hex(15453))

# 十进制 decimal
import decimal

# print(int("0b111"))  # bug

print(decimal.Decimal(0b111))

# 加不加前缀都可以的
print(int("0b111", 2))
print(int("111", 2))

# print(int("1121", 2))  # 非法，报错了

print(int("111", 3))  # 任意进制
print(int("111", 4))  # 任意进制
