import _ctypes


class SetList:
    def __init__(self):
        self.lst = []
        self.dic = {}

    def add(self, val):
        if val in self.dic:
            return
        self.dic[val] = len(self.lst)
        self.lst.append(val)

    def __iter__(self):
        """

        :return:
        """
        """
        for item in self.lst:
            yield item
        """
        # 以上代码直接简化
        yield from self.lst

    def __contains__(self, item):
        return item in self.dic

    def remove(self, item):
        if item not in self.dic:
            return
        delIndex = self.dic[item]
        self.dic.pop(item)  # 删除dic里的数据
        popRes = self.lst[delIndex]
        self.lst[delIndex] = self.lst[-1]
        self.dic[self.lst[-1]] = delIndex
        self.lst.pop()
        return popRes

    def __str__(self):
        res = "<"
        for i, item in enumerate(self.lst):
            res += str(item)
            if i != len(self.lst) - 1:
                res += ", "
        return f"{res}>"

    __repr__ = __str__


sl = SetList()
print(sl)

sl.add(13)
sl.add(15)
sl.add(14)
print(sl)
sl.remove(15)
print(sl)
sl.remove(14)
print(sl)
sl.remove(13)
print(sl)
