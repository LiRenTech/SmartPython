def nbDeco(oldDeco):
    def newDeco(func):
        return oldDeco(oldDeco(func))

    return newDeco


# nbDeco = nbDeco(nbDeco)
# nbDeco = nbDeco(nbDeco(nbDeco))
nbDeco = nbDeco(nbDeco(nbDeco(nbDeco)))


@nbDeco
def deco(func):
    def newFunc():
        print("=")
        func()

    return newFunc


@deco
def f0():
    print("hello")


f0()
# pycharm中选中输出的=号然后按 ctrl F ，可以查看有多少个=号，进而获悉有多少层
