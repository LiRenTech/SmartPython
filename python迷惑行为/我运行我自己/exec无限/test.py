import os

print(1)
with open(os.listdir()[0], encoding="utf-8") as f:
    exec(f.read())

# 被检测到了无限递归，被迫终止
