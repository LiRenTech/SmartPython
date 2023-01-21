def extend(sup_class):
    """模拟类继承 的装饰器语法"""

    def robot(sub_class):
        print("=====extends")
        for k, v in sup_class.__dict__.items():
            print(k, v)
        print("=====")
        return sub_class

    return robot


def new(obj):
    return obj


def Person(name: str, age: int):

    def this():
        this.name = name
        this.age = age

    this()
    return this


# p = new(Person("aaa", 12))
p = Person("aaa", 12)
print("closure::", p.__closure__)
for item in p.__closure__:
    print(item, item.cell_contents)


@extend(Person)
def Student(name: str, age: int, number: int, this=lambda: ...):
    this.name = name
    this.age = age
    this.age = age
    this.number = number

    return this


def f(a: int, b: int, c: int, d: int = 1):
    ...


# for item in dir(f):
#     print(item)
print("---")
print(f.__annotations__)
print(f.__qualname__)  # 如果有类继承的话，会多上点
print(f.__name__)
