def extend(*extend_cls_list):
    def decorator(cls_function):
        def new_function(*args, **kwargs):
            if len(extend_cls_list) == 0:
                return cls_function(lambda: ..., *args, **kwargs)
            else:
                super_obj = lambda: ...
                for extend_cls in extend_cls_list:
                    current_super_obj = extend_cls(*args, **kwargs)
                    for key, value in current_super_obj.__dict__.items():
                        if not key.startswith('__'):
                            setattr(super_obj, key, value)
                return cls_function(super_obj, *args, **kwargs)

        return new_function

    return decorator


@extend()
def Animal(self, *args, **kwargs):
    self.name = kwargs.get('name', 'Unknown')

    def to_string():
        return f"I am {self.name}"

    self.to_string = to_string
    return self


@extend()
def Runner(self, *args, **kwargs):
    self.speed = kwargs.get('speed', 0)
    return self


@extend(Animal, Runner)
def Dog(self, *args, **kwargs):
    self.age = kwargs.get('age', 0)

    self.super_to_string = self.to_string  # 保存父类的to_string方法

    def to_string():
        print(self.super_to_string())
        return f"I am {self.name}, I am {self.age} years old, and I run at {self.speed} km/h."

    self.to_string = to_string

    return self


dog = Dog(name='Rufus', age=3, speed=10)
print(dog.to_string())
