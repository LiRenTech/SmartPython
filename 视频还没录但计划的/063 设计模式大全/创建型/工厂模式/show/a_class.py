from typing import Dict, List


class A:
    CURRENT_YEAR = 2021

    def __init__(self,
                 a: int,
                 b: float,
                 c: str,
                 d: List[int],
                 e: Dict[str, int]
                 ):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        print(self.CURRENT_YEAR)

    def __str__(self):
        return f"A(a={self.a}, b={self.b}, c={self.c}, d={self.d}, e={self.e})"

    __repr__ = __str__

    def compute(self):
        return self.a + self.b + len(self.c) + sum(self.d) + sum(self.e.values())

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d and self.e == other.e

    def __hash__(self):
        return hash((self.a, self.b, self.c, tuple(self.d), tuple(self.e.items())))

    def __lt__(self, other):
        return self.a < other.a

    def __gt__(self, other):
        return self.a > other.a

    def __le__(self, other):
        return self.a <= other.a

    def __ge__(self, other):
        return self.a >= other.a

    def __ne__(self, other):
        return self.a != other.a

    def __bool__(self):
        return bool(self.a)

    pass
