def Person(name: str, age: int):
    def this():
        ...

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        return self

    this = __init__(this, name, age)

    def say():
        print(f"大家好我叫{this.name},我{this.age}岁了")

    def show():
        print(f"xxx")

    this.say = say
    this.show = show
    return this


def Student(name: str, age: int, class_: int):
    def this():
        ...

    def __init__(self, name: str, age: int, class_: int):
        self = Person(name, age)
        self.class_ = class_
        return self

    this = __init__(this, name, age, class_)

    def say():
        print(f"大家好我叫{this.name},我{this.age}岁了,我在{this.class_}班")

    this.say = say
    return this


p = Person("sb", 18)
# print(p)
p.say()

s = Student("mnb", 12, 1)
s.say()
s.show()
