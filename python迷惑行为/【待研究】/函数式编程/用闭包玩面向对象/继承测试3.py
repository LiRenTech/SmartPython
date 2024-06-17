from copy import deepcopy


def Person(name: str, age: int):
    # 定义this对象，不能用object(), 否则会报错
    this = lambda: ...

    def toString():
        return f"Person(name={this.name}, age={this.age}, defaultValue={this.defaultValue})"

    def sayHello():
        print(f"Hello, my name is {this.name} and I am {this.age} years old., my default value is {this.defaultValue}")

    # 给this对象添加属性
    this.name = name
    this.age = age
    this.defaultValue = 100
    # 给this对象添加方法
    this.toString = toString
    this.sayHello = sayHello
    # 返回this对象
    return this


p1 = Person("Alice", 25)
print(p1)
print(p1.toString())
print(p1.age, p1.name)
print(p1.toString.__closure__)


# 单继承
def Worker(name: str, age: int, salary: int):
    this = Person(name, age)

    def work():
        print(
            f"I am a worker, my name is {this.name}, I am {this.age} years old, and my salary is {this.salary}, my default value is {this.defaultValue}")

    this.salary = salary
    this.defaultValue = 200
    this.work = work
    return this


w1 = Worker("Bob", 30, 5000)
w1.sayHello()
print(w1.toString())


def SuperWorker(name: str, age: int, salary: int, bonus: int):
    super = Worker(name, age, salary)
    this = deepcopy(super)
    print(id(super), id(this))

    def work():
        this.super.work()
        print(
            f"I am a super worker, my name is {this.name}, I am {this.age} years old, and my salary is {this.salary}, my bonus is {this.bonus}, my default value is {this.defaultValue}")

    this.super = super
    this.bonus = bonus
    this.work = work
    return this


sw1 = SuperWorker("Charlie", 35, 7000, 1000)

