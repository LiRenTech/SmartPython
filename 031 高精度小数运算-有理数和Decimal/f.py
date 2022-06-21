import decimal

from decimal import *


def main():
    decimal.getcontext().prec = 20
    N = 100
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            f = Decimal(i) / Decimal(j)
            print(f"{i}/{j}", f)

    return None


if __name__ == "__main__":
    main()
