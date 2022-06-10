import ctypes
import sys

__STD_OUTPUT_HANDLE = -11
__std_out_handle = ctypes.windll.kernel32.GetStdHandle(__STD_OUTPUT_HANDLE)
BLUE = 0x09  # blue.  9
GREEN = 0x0a  # green. 10
RED = 0x0c  # red.     11
YELLOW = 0x0e  # yellow.


def setColor(color):
    return ctypes.windll.kernel32.SetConsoleTextAttribute(__std_out_handle, color)


# setColor(__FOREGROUND_RED | __FOREGROUND_GREEN | __FOREGROUND_BLUE)  # 白色  | 是位运算中的或运算
setColor(RED)
sys.stdout.write("sdjflksadjlf" + '\n')
setColor(GREEN)
sys.stdout.write("mess" + '\n')
setColor(BLUE)
sys.stdout.write("mess" + '\n')
setColor(BLUE | YELLOW)
sys.stdout.write("mess" + '\n')


input()