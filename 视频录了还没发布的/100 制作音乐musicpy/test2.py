# -*- encoding: utf-8 -*-
from musicpy import *
from typing import *

a1 = note("C", 5)
a2 = note("D", 5)
a3 = note("E", 5)
a4 = note("F", 5)
a5 = note("G", 5)
a6 = note("A", 5)
a7 = note("B", 5)
a1_ = note("C", 6)
a2_ = note("D", 6)


def stringToList(string: str) -> List[note]:
    res = []
    for s in string.split():
        if len(s) == 1:
            res.append(eval(f"a{s}"))
        else:
            res.append(eval(f"a{s[0]}_"))
    return res


n = 1 / 4
nd = 1 / 4 + 1 / 8
_ = 1 / 8
notList = stringToList("5 1. 7 2. 1. 5 3 6 6 4 6 2. 1. 7 6 5 4 3")
durList = [n] + [nd, _, _, _, _, _, ] + [nd, _, n + _, _] + [nd, _, _, _, _, _, ] + [n * 3]
print(len(notList), len(durList))
play(chord(notList, durList, durList), bpm=120)
