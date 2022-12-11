import os
import threading
import time
import inspect

import ctypes


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        # raise ValueError("invalid thread id")
        # 线程已经结束了
        return
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


def main():
    cStr = """
    #include <stdio.h>
    // 123123
    int main() {
        printf("123456\\n");
    }
    
    """

    cFileName = "cFile"
    exeFileName = "exeFile"
    timeLimit = 4  # s

    # 生成C文件

    with open(f"{cFileName}.c", "w", encoding="utf-8") as f:
        f.write(cStr)

    # gcc编译指令
    # gcc w.c     -o    main
    # 固定 文件名  固定   生成exe的目标前缀

    # 编译C文件
    res1 = os.system(f"gcc {cFileName}.c -o {exeFileName}")

    # 删除C文件
    os.remove(f"{cFileName}.c")
    if res1 == 0:
        # 编译成功

        def f():
            return os.system(f"{exeFileName}.exe")

        userThread = threading.Thread(target=f)

        res = userThread.start()
        time.sleep(timeLimit)
        stop_thread(userThread)

        # ========
        os.remove(f"{exeFileName}.exe")
    else:

        ...


if __name__ == "__main__":
    main()
