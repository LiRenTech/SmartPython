class M1(type):
    ...


class M2(type):
    ...


class C1(metaclass=M1):
    ...


class C2(metaclass=M2):
    ...


class S(C1, C2):
    ...


print(type(S))
