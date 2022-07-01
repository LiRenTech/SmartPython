

# 可能容易枯燥，需要加点生动的栗子

# 字符串前面加个字母有什么意思

b = "bbb"
# f
a = f"abc{b}def"
a2 = f"abc{b}def{{a}}"

# r
c = r"D:\a.txt"
c1 = "D:\\a.txt"

# rf一起写，顺序无所谓
ab = rf"{c1}\t"
ba = fr"{c}\t"

# b是转化成二进制
# d = b"喔喔我"  #  bytes can only contain ASCII literal characters.
d = b"this is english"
print(d)
print(type(d))
bytes()
