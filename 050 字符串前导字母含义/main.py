# 可能容易枯燥，需要加点生动的栗子

b = "bbb"
a = f"abc{b}def"
a2 = f"abc{b}def{{a}}"
c = r"D:\a.txt"
c1 = "D:\\a.txt"

ab = rf"{c1}\t"
ba = fr"{c}\t"

r = r"\t\\  "   # 一旦写了r，后面就不能写东西了

"""
 \a
 \b
 \c
 \d
 \e
 \f
 \g
 \h
 \i
 \j
 \k
 \l
 \m
 \n
 \o
 \p 
 \q
 \r 
 \s 
 \t 
 \u
 \u0000
 \u331222
 \u1447
 \u9999
 \v
 \w 
 \x
 \x5555
 \x23
 \xab
 \xff
 \y
 \z
"""

# d = b"喔喔我"  #  bytes can only contain ASCII literal characters.
d = b"this is english"

print(d)
