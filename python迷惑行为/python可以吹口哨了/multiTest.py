# -*- encoding: utf-8 -*-
"""
PyCharm multiTest
2022年11月02日
by littlefean
"""
from typing import *
from winsound import Beep
from time import sleep
from threading import Thread


def beepAndPrint(hz, time):
    CHAR = "▉"
    Beep(hz, time)
    print(f"{CHAR}" * int(hz / 100))


def main():
    # 无法实现多线程的
    # Thread(target=beepAndPrint, args=(3000, 1000)).start()
    Thread(target=beepAndPrint, args=(5000, 1000)).start()
    return None


if __name__ == "__main__":
    main()
