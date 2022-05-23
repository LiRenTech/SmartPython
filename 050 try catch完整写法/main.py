def f():
    print(1 / 0)
    ...

# 范围逐渐扩大原理

import traceback

try:
    f()
except ValueError:
    ...
except NameError:
    ...
except Exception as e:  # 如果写成其他的样子，会有警告
    print(e)
    traceback.print_exc()  # 更全面的方式
else:
    ...
finally:
    ...


for i in range(10):
    print(i)