from typing import *


def main():
    num2Task = {
        1: {
            "name": "构思",
            "details": ...,
        },
        2: {
            "name": "拍视频",
            "details": ...,
        },
        3: {
            "name": "找素材",
            "details": ...,
        },
        4: {
            "name": "剪辑",
            "details": ...,
        },
        5: {
            "name": "发b站",
            "details": ...,
        },
    }
    graph = {
        1: {2, 3},
        2: {4},
        3: {4},
        4: {5},
        5: {},
    }
    graph = {
        1: {2},
        2: {3},
        3: {1},
    }
    arr = f(graph)
    if len(arr) < len(graph):
        print("cycle")
    print()


def f(graph: Dict[int, Set[int]]) -> List[int]:
    from collections import deque

    count_dict = {n: 0 for n in graph}
    for node, child_set in graph.items():
        for child in child_set:
            count_dict[child] += 1

    q = deque()
    for node, count in count_dict.items():
        if count == 0:
            q.append(node)

    res = []
    while q:
        n = q.popleft()
        res.append(n)
        child_set = graph[n]
        for child in child_set:
            count_dict[child] -= 1
            if count_dict[child] == 0:
                q.append(child)
    return res


if __name__ == '__main__':
    main()
