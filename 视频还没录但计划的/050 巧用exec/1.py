"""
exec的docstring：
               ↓↓↓↓↓↓↓↓↓注意这里的类型           ↓↓↓↓↓↓↓↓↓↓↓↓↓↓全局变量                   ↓↓↓↓↓↓↓↓↓本地变量（或者说是内部变量）
exec(__source: ReadableBuffer | str | CodeType, __globals: dict[str, Any] | None = ..., __locals: Mapping[str, object] | None = ..., /) -> None
Execute the given source in the context of globals and locals.

The source may be a string representing one or more Python statements or a code object as returned by compile(). The globals must be a dictionary and locals can be any mapping, defaulting to the current globals and locals. If only globals is given, locals defaults to it.
"""

from pathlib import Path

# 用法1
print("返回值：", exec("print('hello from string 1')"))  # 正确
# print(
#     "返回值：",
#     exec(
#         """
#         print('hello from string 2')
#         """
#     ),
# )  # 缩进错误
print(
    "返回值：",
    exec(
        """
print('hello from string 3')
        """
    ),
)  # 正确

print("----------")

# 用法2
# 看1.png！！！！！！
print("返回值：", exec("print('hello from stringio')".encode("utf-8")))
with open((Path(__file__).parent / "testfile.py").as_posix(), "rb") as f:
    print("返回值：", exec(f.read()))  # 这个不是str！！！！

print("----------")

# 用法3
def func():
    print("hello from code object")
print("返回值：", exec(func.__code__))
