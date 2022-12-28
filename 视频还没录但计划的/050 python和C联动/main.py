"""

C文件编译成 so文件
gcc -fPIC -shared c文件路径 -o 文件名.so
"""

from ctypes import CDLL

CDLL("")