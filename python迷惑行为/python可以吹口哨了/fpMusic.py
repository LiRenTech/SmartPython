# encoding:utf-8-*-
"""
蜂鸣音乐
2020年8月21日
此内容过于久远
https://www.bilibili.com/video/BV1Ph411k7i5
by littlefean
"""
from winsound import Beep
from time import sleep
from random import randint


def beepAndPrint(hz, time):
    CHAR = "▉"
    Beep(hz, time)
    print(f"{CHAR}" * int(hz / 100))


def fpMusic():
    """富婆之歌"""

    def w1():
        beepAndPrint(3000, 200)
        beepAndPrint(2600, 200)
        beepAndPrint(2200, 500)
        beepAndPrint(2200, 500)
        beepAndPrint(2200, 500)

    def w2():
        beepAndPrint(1500, 200)
        beepAndPrint(1600, 200)
        beepAndPrint(1800, 200)
        beepAndPrint(2000, 200)
        beepAndPrint(1800, 200)
        beepAndPrint(1600, 200)
        beepAndPrint(1800, 200)

    def w3():
        beepAndPrint(2300, 200)
        beepAndPrint(2600, 200)
        beepAndPrint(3000, 500)
        beepAndPrint(3000, 500)
        beepAndPrint(3000, 500)

    def w4():
        beepAndPrint(2300, 200)
        beepAndPrint(2600, 200)
        beepAndPrint(3000, 200)
        beepAndPrint(2600, 200)
        beepAndPrint(2600, 200)
        beepAndPrint(2300, 200)
        beepAndPrint(2600, 200)

    def w5():
        beepAndPrint(2300, 200)
        beepAndPrint(2600, 200)
        beepAndPrint(3000, 800)
        sleep(0.4)
        beepAndPrint(2600, 800)
        sleep(0.2)
        beepAndPrint(2300, 800)

    sleep(0.6)
    w1()
    sleep(0.1)
    w2()
    sleep(0.6)
    w3()
    sleep(0.1)
    w4()
    sleep(0.6)
    w1()
    sleep(0.1)
    w2()
    sleep(0.6)
    w5()


def sviMusic():
    """苏维埃进行曲 未完工"""
    beepAndPrint(500, 300)
    beepAndPrint(500, 300)
    beepAndPrint(400, 100)
    beepAndPrint(500, 200)
    beepAndPrint(300, 600)

    beepAndPrint(500, 100)
    beepAndPrint(600, 200)
    sleep(0.3)
    beepAndPrint(600, 300)
    beepAndPrint(550, 100)
    beepAndPrint(600, 200)

    sleep(1)

    beepAndPrint(600, 300)
    beepAndPrint(600, 300)
    beepAndPrint(650, 100)
    beepAndPrint(700, 200)
    beepAndPrint(600, 300)
    sleep(0.3)
    beepAndPrint(700, 100)
    beepAndPrint(750, 200)
    sleep(0.3)
    beepAndPrint(750, 300)
    beepAndPrint(700, 100)
    beepAndPrint(750, 200)

    sleep(1)

    beepAndPrint(750, 300)
    beepAndPrint(750, 300)
    beepAndPrint(700, 100)
    beepAndPrint(750, 200)
    beepAndPrint(600, 300)
    sleep(0.3)
    beepAndPrint(700, 100)
    beepAndPrint(750, 200)
    beepAndPrint(800, 300)
    beepAndPrint(800, 300)
    beepAndPrint(700, 100)
    beepAndPrint(650, 200)

    sleep(1)


def happyBirthdayMusic():
    """生日快乐歌"""
    beepAndPrint(2000, 250)
    beepAndPrint(2000, 250)
    beepAndPrint(2200, 500)
    beepAndPrint(2000, 500)
    beepAndPrint(2800, 500)
    beepAndPrint(2650, 500)
    sleep(0.5)
    beepAndPrint(2000, 250)
    beepAndPrint(2000, 250)
    beepAndPrint(2200, 500)
    beepAndPrint(2000, 500)
    beepAndPrint(3200, 500)
    beepAndPrint(2750, 500)
    sleep(0.5)
    beepAndPrint(2000, 250)
    beepAndPrint(2000, 250)
    beepAndPrint(3500, 500)
    beepAndPrint(2800, 500)
    beepAndPrint(2420, 500)
    beepAndPrint(2220, 500)
    beepAndPrint(2020, 500)
    sleep(0.5)
    beepAndPrint(3390, 200)
    beepAndPrint(3420, 200)
    beepAndPrint(3320, 500)
    beepAndPrint(2400, 600)
    beepAndPrint(2680, 500)
    beepAndPrint(2480, 500)
    sleep(0.5)


def pvzMenuMusic():
    """植物大战僵尸"""
    beepAndPrint(2200, 273)
    beepAndPrint(2250, 266)
    beepAndPrint(2100, 300)
    beepAndPrint(2340, 300)
    beepAndPrint(1870, 338)
    beepAndPrint(1450, 372)
    sleep(0.5)
    beepAndPrint(2100, 300)
    beepAndPrint(1450, 300)
    sleep(0.41)
    beepAndPrint(2850, 300)
    beepAndPrint(1600, 300)
    sleep(0.5)
    beepAndPrint(1780, 268)
    beepAndPrint(1810, 273)
    beepAndPrint(1700, 273)
    beepAndPrint(2050, 273)
    beepAndPrint(1690, 242)
    beepAndPrint(1200, 395)
    sleep(0.464)
    beepAndPrint(1500, 300)
    beepAndPrint(1200, 300)
    sleep(0.41)
    beepAndPrint(2750, 300)
    beepAndPrint(1450, 300)
    sleep(0.5)
    pass


def pvzMenuMusic_D():
    """植物大战僵尸"""
    beepAndPrint(120, 273)
    beepAndPrint(130, 266)
    beepAndPrint(120, 300)
    beepAndPrint(130, 300)
    beepAndPrint(100, 338)
    beepAndPrint(85, 372)
    sleep(0.5)
    beepAndPrint(110, 300)
    beepAndPrint(85, 300)
    sleep(0.41)
    beepAndPrint(130, 300)
    beepAndPrint(90, 300)
    sleep(0.5)
    beepAndPrint(108, 268)
    beepAndPrint(111, 273)
    beepAndPrint(108, 273)
    beepAndPrint(111, 273)
    beepAndPrint(94, 242)
    beepAndPrint(82, 395)
    sleep(0.464)
    beepAndPrint(90, 300)
    beepAndPrint(83, 300)
    sleep(0.41)
    beepAndPrint(132, 300)
    beepAndPrint(85, 300)
    sleep(0.5)
    pass


def ka_nong():
    """卡农未完工"""
    beepAndPrint(1000, 400)
    beepAndPrint(1200, 400)
    beepAndPrint(1400, 400)
    beepAndPrint(1200, 400)
    beepAndPrint(1600, 400)
    sleep(0.5)
    beepAndPrint(1500, 400)
    beepAndPrint(1400, 400)
    sleep(0.5)
    beepAndPrint(1600, 400)
    beepAndPrint(1200, 400)


def randomMusic():
    beepAndPrint(randint(1000, 4000), randint(100, 100))
    beepAndPrint(randint(500, 2000), randint(100, 100))


if __name__ == '__main__':
    while True:
        fpMusic()
        sviMusic()
        happyBirthdayMusic()
        randomMusic()
        pvzMenuMusic()
        ka_nong()
