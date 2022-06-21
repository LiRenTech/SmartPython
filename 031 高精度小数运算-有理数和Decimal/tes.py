# -*- encoding: utf-8 -*-
"""
PyCharm tes
2022年06月20日
by littlefean
"""
import decimal
from typing import *
from decimal import *
from fractions import Fraction


def main():
    decimal.getcontext().prec = 150

    n = Fraction(1, 3)
    n2 = Fraction(3, 123)
    print(n + 6)
    print(Decimal(n.numerator) / Decimal(n.denominator))
    return None


if __name__ == "__main__":
    main()
