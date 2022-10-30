def nbDeco(oldDeco):
    def newDeco(func):
        return oldDeco(oldDeco(func))

    return newDeco


nbDeco = nbDeco(nbDeco)  # nbDeco {x2} => {{x2}{x2}}
nbDeco = nbDeco(nbDeco)  # nbDeco {{{x2}{x2}}} => {{{{x2}{x2}}}{{{x2}{x2}}}}{{{{x2}{x2}}}{{{x2}{x2}}}}
# nbDeco = nbDeco(nbDeco)


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
