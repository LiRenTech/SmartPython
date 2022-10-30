# -*- encoding: utf-8 -*-
"""
PyCharm main
2022年10月23日
by littlefean
"""
from typing import *
from itertools import *


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        for x, y in zip_longest(word1, word2):
            if x:
                ans.append(x)
            if y:
                ans.append(y)
        return ''.join(ans)


class Solution2:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = ""
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            string += word1[i]
            i += 1
            string += word2[j]
            j += 1
        while i < len(word1):
            string += word1[i]
            i += 1
        while j < len(word2):
            string += word2[j]
            j += 1
        return string


def main():
    return None


if __name__ == "__main__":
    main()
