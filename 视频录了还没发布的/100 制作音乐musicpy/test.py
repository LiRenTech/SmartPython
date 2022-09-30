# -*- encoding: utf-8 -*-
"""
PyCharm test
2022年09月28日
by littlefean

基本类：是note（音符）, chord（和弦）和scale（音阶）
"""
from typing import *

from musicpy import *

a1 = note('C', 5)
a1_ = note('C', 6)
a2 = note('D', 5)
a2_ = note('D', 6)
a3 = note('E', 5)
a4 = note('F', 5)
a5 = note('G', 5)
a6 = note('A', 5)
a7 = note('B', 5)

melody = chord([a1, a2, a3, a4, a5, a6], [1 / 4] * 6, [1 / 4] * 6)
melody2 = chord(reversed([a1, a2, a3, a4, a5, a6]), [1 / 4] * 6, [1 / 4] * 6)
# + | 是拼接
# & 是并列
play(melody & melody2, bpm=80)

