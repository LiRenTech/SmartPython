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

# r 了之后其他的\t\n怎么办
st = r"我我我\t她她她"

# u
"""
字符串前加 u

例：u"我是含有中文字符组成的字符串。"
加了u前缀和没有加前缀的效果相同
作用：
后面字符串以 Unicode 格式 进行编码，一般用在中文字符串前面，防止因为源码储存格式问题，导致再次使用时出现乱码。
应用：
在与工程默认编码格式不同的时候，使用此方法来避免编码的问题
"""

abb = u"这是中文"

# b是转化成二进制
# d = b"喔喔我"  #  bytes can only contain ASCII literal characters.
d = b"this is english"
print(d)
print(type(d))
bytes()

code = "我是一个东西"
print("encode:", code.encode("utf-8"))
dd = b"01101000"
print(dd)

cc = bytearray(dd)
print(cc, type(cc))
