# -*- encoding: utf-8 -*-
"""
PyCharm main
2022年05月26日
by littlefean
"""
from typing import *
from dataclasses import dataclass


@dataclass
class Card:
    rank: str
    suit: str


card = Card("Q", "hearts")
print(card == card)
# True

print(card.rank)
# 'Q'
print(card)
Card(rank='Q', suit="hearts")


def main():
    return None


if __name__ == "__main__":
    main()
