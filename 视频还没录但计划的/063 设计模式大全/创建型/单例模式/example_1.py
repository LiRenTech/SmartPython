"""
单例模式
懒汉模式
"""


class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

    def someMethod(self):
        pass


def main():
    # Usage
    s1 = Singleton.getInstance()
    s2 = Singleton.getInstance()

    print(s1 == s2)  # True


if __name__ == '__main__':
    main()
