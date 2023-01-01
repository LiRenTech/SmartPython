def Student(name, age):
    def addAge(n):
        nonlocal age
        age += n

    def say(): print(f"我叫{name}，我{age}岁")

    # def obj(): ...

    obj = lambda: ...

    obj.name = name
    obj.age = age
    obj.addAge = addAge
    obj.say = say
    return obj


s1 = Student("小明", 18)
s2 = Student("小红", 8)
s1.say()
s2.say()
s1.addAge(5)
s1.say()
s2.say()
print(s1.say.__closure__)
