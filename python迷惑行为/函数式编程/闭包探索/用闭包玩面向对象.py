def student(name, age):

    def addAge(n):
        nonlocal age
        age += n

    def say(): print(f"我叫{name}，我{age}岁")

    def obj():
        ...  # 用一个空函数对象表示实例化出来的对象
    obj.name = name
    obj.age = age
    obj.addAge = addAge
    obj.say = say
    return obj


s1 = student("小明", 18)
s2 = student("小红", 8)
s1.say()
s2.say()
s1.addAge(5)
s1.say()
s2.say()
print(s1.say.__closure__)
