"""
拓扑排序的传统实现

"""


def topological_sort(graph):
    def dfs(node):
        visited[node] = True
        for child in graph[node]:
            if not visited[child]:
                dfs(child)
        result.append(node)

    # 初始化
    visited = {node: False for node in graph}
    result = []

    # 遍历图中的每个节点
    for node in graph:
        if not visited[node]:
            dfs(node)

    # 结果是逆序的，反转得到拓扑排序
    return result[::-1]


def f(graph):
    # 记录所有的入度量
    from collections import deque
    count_graph = {n: 0 for n in graph}
    for k, child_set in graph.items():
        for child in child_set:
            count_graph[child] += 1
    # 所有入度为0的节点入队列
    q = deque()
    for node, count in count_graph.items():
        if count == 0:
            q.append(node)
    res = []
    # 准备好开始队列了
    while q:
        n = q.popleft()
        res.append(n)
        child_set = graph[n]
        for child in child_set:
            count_graph[child] -= 1
            if count_graph[child] == 0:
                q.append(child)
    return res


def topological_sort_no_cycle(graph):
    # 能检测出是否有环的情况
    def dfs(node):
        visited[node] = True
        currently_visiting.add(node)

        for child in graph[node]:
            if not visited[child]:
                if dfs(child):
                    return True
            elif child in currently_visiting:
                # 如果在当前DFS路径上发现已经访问过的节点，说明存在环
                return True

        currently_visiting.remove(node)
        result.append(node)
        return False

    # 初始化
    visited = {node: False for node in graph}
    result = []
    currently_visiting = set()

    # 遍历图中的每个节点
    for node in graph:
        if not visited[node]:
            if dfs(node):
                # 如果在DFS中发现环，返回空列表表示拓扑排序不可行
                return []

    # 结果是逆序的，反转得到拓扑排序
    return result[::-1]


def main():
    # 示例用法
    graph = {
        1: {2, 3},
        2: {4},
        3: {4, 5},
        4: {5},
        5: {},
    }
    g = {
        1: {2},
        2: {3},
        3: {4},
        4: {5},
        5: {1},
    }

    # result = topological_sort_no_cycle(graph)
    # result = topological_sort(g)
    result = f(graph)
    print("Topological Sort:", result)


if __name__ == '__main__':
    main()
