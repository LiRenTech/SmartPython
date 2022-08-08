# 进行一些初始化操作
class System:
    p = print

    class Out:
        @staticmethod
        def println(*args):
            print(*args)

        @staticmethod
        def print(*args):
            System.p(*args, end="")

    out = Out


# 操作完毕


class JavaClass:

    @staticmethod
    def main(*args, **kwargs):
        System.out.println(1233);
        # 有点逊……

        ...


if __name__ == "__main__":
    JavaClass().main()
