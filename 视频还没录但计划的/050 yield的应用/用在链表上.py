class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __iter__(self):
        node = self
        while node:
            yield node
            node = node.next

    def __next__(self):
        if self is None:
            raise StopIteration
        else:
            return self.next

    def __str__(self):
        return f"<{self.val}, {self.__dict__}>"

    __repr__ = __str__


from typing import *


def main():
    head = Node(1)
    head.next = Node(5)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    for item in head:
        print(item)
    print()
    print(head)
    for item in head:
        print(item)

    t: Tuple[int, int] = 1, 5
    t: [int, int] = 1, 5
    a, b = t
    
    ...


main()
