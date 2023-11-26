from graphlib import TopologicalSorter, CycleError


def main():
    # test0()
    # test1()
    test3()
    ...


def test0():
    # 返回前驱为0的节点
    ts = TopologicalSorter({
        "D": {"B", "C"},
        "C": {"A"},
        "B": {"A"}
    })
    ts.prepare()  # 先让它准备一下，看看有没有环
    print(ts.get_ready())  # 找到没有前驱的节点


def test1():
    graph = {"D": {"B", "C"}, "C": {"A"}, "B": {"A"}}
    ts = TopologicalSorter(graph)
    c = ts.static_order()
    print(list(c)[::-1])


def test2():
    try:
        ts2 = TopologicalSorter({
            'a': {'b'},
            'b': {'c'},
            'c': {'d'},
            'd': {'a'},
        })
        print(list(ts2.static_order()))
    except CycleError:
        ...


def test3():
    # 同样的图，换一个图的生成方式，用边生成
    ts = TopologicalSorter()
    ts.add('d', 'b')
    ts.add('d', 'c')
    ts.add('b', 'a')
    ts.add('c', 'a')
    print(list(ts.static_order()))
    ...


if __name__ == "__main__":
    """
    自创编译系统检测引入是否合理
    工作流程管理
    
    在游戏项目中：
    任务系统 关卡设计 任务进度解锁 效果触发 

    """
    main()
