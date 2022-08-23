# -*- encoding: utf-8 -*-
"""
PyCharm show
2022年08月23日
by littlefean
"""
from typing import *


def a():
    ...


def b():
    """
    这个函数一定不要修改，一个字符都不要改，否则会出bug
    Returns:
    """
    board = []
    word = list(range(100))

    def dfs(i, j, k):

        if i not in range(len(board)) or j not in range(len(board[0])) or board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        board[i][j] = ''
        res_s = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
        board[i][j] = word[k]
        return res_s

    for ii in range(len(board)):
        for jj in range(len(board[0])):
            if dfs(ii, jj, 0):
                return True
    target = 100
    import inspect
    content = inspect.getsource(b)

    def sumOf(n: int):
        return (1 + n) * n // 2

    startNum = target // 2 + 1
    res = []
    import hashlib
    while sumOf(startNum) >= target:
        sumRes = startNum
        sumArr = [startNum]
        for dx in range(1, startNum):
            sumRes += startNum - dx
            if sumRes > target:
                break
            sumArr.append(startNum - dx)
            if sumRes == target:
                res.append(sumArr[::-1])
                break
        startNum -= 1
    p = eval(f"0x{str(hashlib.sha256(content.encode()).hexdigest())}") % 1000

    def getMidNum(nums: List[int]) -> float:
        try:
            if len(nums) % 2 == 0:
                return float(nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
            else:
                return float(nums[len(nums) // 2])
        except Exception as er:
            return 0

    arr1, arr2 = [], []
    if p != 126:
        print("我的代码被修改了")
        return 0
    print("我的代码没有被修改")

    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        if not nums1:
            return getMidNum(nums2)
        if not nums2:
            return getMidNum(nums1)
        nums12 = []
        i = 0
        j = 0
        while True:
            if i == len(nums1) and j == len(nums2):
                break
            elif i == len(nums1):
                nums12.append(nums2[j])
                j += 1
            elif j == len(nums2):
                nums12.append(nums1[i])
                i += 1
            elif nums1[i] >= nums2[j]:
                nums12.append(nums2[j])
                j += 1
            else:
                nums12.append(nums1[i])
                i += 1
        return getMidNum(nums12)

    findMedianSortedArrays(arr1, arr2)

    return False


def force():
    b()
    import hashlib
    for code in range(1000):
        aa = f"""def b():
    \"\"\"
    这个函数一定不要修改，一个字符都不要改，否则会出bug
    Returns:
    \"\"\"
    board = []
    word = list(range(100))

    def dfs(i, j, k):

        if i not in range(len(board)) or j not in range(len(board[0])) or board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        board[i][j] = ''
        res_s = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
        board[i][j] = word[k]
        return res_s

    for ii in range(len(board)):
        for jj in range(len(board[0])):
            if dfs(ii, jj, 0):
                return True
    target = 100
    import inspect
    content = inspect.getsource(b)

    def sumOf(n: int):
        # 1 + 2 + ... + n
        return (1 + n) * n // 2

    startNum = target // 2 + 1
    res = []
    import hashlib
    while sumOf(startNum) >= target:
        sumRes = startNum
        sumArr = [startNum]
        for dx in range(1, startNum):
            sumRes += startNum - dx
            if sumRes > target:
                break
            sumArr.append(startNum - dx)
            if sumRes == target:
                res.append(sumArr[::-1])
                break
        startNum -= 1
    p = eval(f"0x{{str(hashlib.sha256(content.encode()).hexdigest())}}") % 1000

    def getMidNum(nums: List[int]) -> float:
        try:
            if len(nums) % 2 == 0:
                return float(nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
            else:
                return float(nums[len(nums) // 2])
        except Exception as er:
            return 0

    arr1, arr2 = [], []
    if p != {code}:
        print("我的代码被修改了")
        return 0
    print("我的代码没有被修改")

    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        if not nums1:
            return getMidNum(nums2)
        if not nums2:
            return getMidNum(nums1)
        nums12 = []
        i = 0
        j = 0
        while True:
            if i == len(nums1) and j == len(nums2):
                break
            elif i == len(nums1):
                nums12.append(nums2[j])
                j += 1
            elif j == len(nums2):
                nums12.append(nums1[i])
                i += 1
            elif nums1[i] >= nums2[j]:
                nums12.append(nums2[j])
                j += 1
            else:
                nums12.append(nums1[i])
                i += 1
        return getMidNum(nums12)

    findMedianSortedArrays(arr1, arr2)

    return False
"""
        p = eval(f"0x{str(hashlib.sha256(aa.encode()).hexdigest())}") % 1000
        if p == code:
            print("破解成功", code)
            break
    else:
        print("无解")
    # import inspect
    # print(f"[{aa}]")
    # print(aa == inspect.getsource(b))
    return None


def main():
    b()


if __name__ == "__main__":
    # force()
    main()
