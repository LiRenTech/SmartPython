# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年07月13日
by littlefean
"""


def say():
    print("我是xxx")


class Human:
    def say(self, word):
        print(f"我说：{word}")


say()

h = Human()
h.say("你好")

Human.say(h, "你好")
