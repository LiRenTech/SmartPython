from translation import trans

with open("a.pycn", encoding="utf-8") as f:
    content = f.read()
content = trans(content)

with open("chinese.py", encoding="utf-8") as f:
    content = f.read() + content

# print(content)
exec(content)
