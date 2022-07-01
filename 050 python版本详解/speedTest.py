# -*- encoding: utf-8 -*-
"""
PyCharm speedTest
版本测速
2022年06月29日
by littlefean
"""

import itertools
import sys

from time import perf_counter


# def f(lst: list[list[int]]):
#     ...

def timer(func):
    def newFunc():
        t = perf_counter()
        func()
        print(func.__name__, perf_counter() - t)

    return newFunc


def main():
    emptyFor()
    # 3.7
    # 1.6828802999999999
    # 1.735408

    # 3.11
    # 1.4134954000037396
    # 1.3960148000041954

    listTest()
    # 3.11
    # 0.9712022000021534
    # 0.9548473999893758
    # 0.9484349999984261

    # 3.7
    # 1.0333601

    productFor()
    # 3.11
    # 2.212857599995914
    # 2.673356600003899
    # 2.194184400010272
    # 2.7879372000024887

    # 3.7
    # 2.395192
    # 2.4420126
    # 2.4203775999999997
    # 5.2006172

    printTest()
    # 3.7
    # 1.6321515999999998
    # 1.4306335000000001
    # 1.6832107
    # 1.7317879
    # 1.0067806
    # 1.8272867
    # 1.483294

    # 3.11
    # 1.723072399996454
    # 1.9306287000072189
    # 1.9591853999882005
    # 1.4846825000131503
    # 0.5886464999930467
    # 0.42677869999897666
    # 1.999874400004046

    calc()
    # 3.7
    # 3.6664478
    # 3.6410346999999996
    # 3.6233836999999998
    # 3.6288223

    # 1.3706708999816328
    # 1.1503395000181627
    # 1.1331392000138294
    # 1.1240714000014123

    dfsFunc()
    # 3.7
    # 1.9043898000000001
    # 1.9369355
    # 1.9150192
    # 1.9128319
    # 1.923235

    # 3.11
    # 2.577784699999029
    # 1.282115599984536
    # 1.2773713000060525
    # 1.2911645999993198
    # 1.2865357999980915

    setTest()
    # 3.7
    # 4.6198683
    # 4.6485655
    # 4.6901226000000005
    # 4.629058700000001
    # 4.7230945

    # 3.11
    # 2.2246587999979965
    # 2.2061018999957014
    # 2.192767400003504
    # 2.203320500004338
    # 2.1936418999976013

    reverseTest()
    # 3.7
    # 2.6382522
    # 2.5829316
    # 2.5782402
    # 2.6094505
    # 2.551619

    # 3.11
    # 2.245820599986473
    # 2.2741419000085443
    # 2.2513421999756247
    # 2.2408414999954402
    # 2.2172509000229184

    sortTest()
    # 3.7
    # 1.2123722000000001
    # 1.1551908
    # 1.1573968000000001
    # 1.1542121
    # 1.1693824

    # 3.11
    # 0.6882882000063546
    # 0.6899049000057857
    # 0.6877942999999505
    # 0.6850930999789853
    # 0.6769336000143085

    listPopTest()
    # 3.7
    # 3.4707942999999997
    # 3.5536094
    # 3.4691651
    # 3.5131624
    # 3.5188726999999997

    # 3.11
    # 3.916764499997953
    # 3.8133682000043336
    # 3.7966824999894015
    # 3.804633099993225
    # 3.805749700026354

    evalTest()
    # 3.7
    # 2.5596767999999996
    # 2.622131
    # 2.6327789
    # 2.8545758
    # 2.6526701

    # 3.11
    # 1.7143439000064973
    # 1.4512415000062902
    # 1.4074542000016663
    # 2.0764737999998033
    # 1.398413699993398
    print(sys.version)
    ...


@timer
def listTest():
    print([[0] * 10000 for _ in range(1000)])


@timer
def emptyFor():
    for i in range(10000):
        for j in range(10000):
            ...

    return None


@timer
def productFor():
    for _, _, _, _ in itertools.product(range(100), range(110), range(100), range(100)):
        ...


@timer
def printTest():
    for i in range(100000):
        print(i)


@timer
def calc():
    res = 0
    for i in range(10000000):
        res += i ** 2
        res %= 100000007
    print(res)


@timer
def dfsFunc():
    def fab(n):
        return 1 if n in [1, 2] else fab(n - 1) + fab(n - 2)

    fab(35)


@timer
def setTest():
    from random import randint
    count = 0
    s = {randint(0, 10000000) for _ in range(10000)}
    for _ in range(5000000):
        n = randint(0, 10000000)
        if n in s:
            count += 1
    print(count)


@timer
def reverseTest():
    arr = list(range(1_0000_0000))
    arr.reverse()


@timer
def sortTest():
    from random import randint
    arr = [randint(1, 100000000) for _ in range(100_0000)]
    arr.sort()


@timer
def listPopTest():
    arr = [0] * 20_0000
    while arr:
        arr.pop(0)
    ...


@timer
def evalTest():
    from random import randint, choice
    for _ in range(1000):
        string = str(randint(1, 100))
        for _ in range(1000):
            string += choice("+-*/") + str(randint(1, 100))

        eval(string)


if __name__ == "__main__":
    main()
