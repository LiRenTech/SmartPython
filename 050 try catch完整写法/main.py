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


# heapq内置库代码
# Short-cut for n==1 is to use max()
#     if n == 1:
#         it = iter(iterable)
#         sentinel = object()
#         if key is None:
#             result = max(it, default=sentinel)
#         else:
#             result = max(it, default=sentinel, key=key)
#         return [] if result is sentinel else [result]
#
#     # When n>=size, it's faster to use sorted()
#     try:
#         size = len(iterable)
#     except (TypeError, AttributeError):
#         pass