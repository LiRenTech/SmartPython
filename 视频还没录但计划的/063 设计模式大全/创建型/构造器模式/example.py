class Person:
    def __init__(self, name, age, hair_color=None, height=None, weight=None, address=None):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.height = height
        self.weight = weight
        self.address = address


class PersonBuilder:
    def __init__(self):
        self.person = Person(None, None)

    def with_name(self, name):
        self.person.name = name
        return self

    def with_age(self, age):
        self.person.age = age
        return self

    def build(self):
        return self.person


"""
好处：
参数太多的时候可以分步骤构建，顺序可能可以换，（但实际上py有默认参数，可以不用这么麻烦）
参数太多可以把几个捏在一起放在一个构造过程函数里
"""
builder = PersonBuilder()
person = builder.with_name("John").with_age(30).build()
