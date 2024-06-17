def extend(extend_cls):
    def decorator(cls_function):
        def new_function(*args, **kwargs):
            if extend_cls is not None:
                super_obj = extend_cls(*args, **kwargs)
                return cls_function(super_obj, *args, **kwargs)
            else:
                return cls_function(lambda: ..., *args, **kwargs)

        return new_function

    return decorator


@extend(None)
def Animal(self, *args, **kwargs):
    self.name = kwargs.get('name', 'Unknown')

    def to_string():
        return f"I am {self.name}"

    self.to_string = to_string
    return self


@extend(Animal)
def Dog(self, *args, **kwargs):
    self.age = kwargs.get('age', 0)

    self.super_to_string = self.to_string  # 保存父类的to_string方法

    def to_string():
        print(self.super_to_string())
        return f"I am {self.name}, I am {self.age} years old"

    self.to_string = to_string

    return self


dog = Dog(name='Rufus', age=3)
print(dog.to_string())
