from a_class import A
from factory import AFactory


def main():

    a_normal_1 = AFactory.get_normal_instance()
    # ====
    a2 = A(1, 1.3, 'world', [3, 4], {'c': 3, 'd': 4})
    # ====

    a3 = A(2, 2.3, 'python', [5, 6], {'e': 5, 'f': 6})

    AFactory.SYSTEM_PERFORMANCE = 0.5  # 模拟系统性能下降，降低创建对象的速度

    # ====
    a_normal_2 = AFactory.get_normal_instance()
    a_normal_3 = AFactory.get_normal_instance()

    AFactory.SYSTEM_PERFORMANCE = 1  # 模拟系统性能恢复，恢复创建对象的速度

    a_strange_1 = AFactory.get_strange_instance()

    # ====
    a_strange_2 = AFactory.get_strange_instance()
    print(a_normal_1, a_normal_2, a_normal_3, a_strange_1, a_strange_2)


if __name__ == '__main__':
    main()
