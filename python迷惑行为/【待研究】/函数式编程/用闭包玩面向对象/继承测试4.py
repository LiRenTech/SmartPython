import inspect


def extends(super_class):
    def decorator(child_class):

        def new_class(*args, **kwargs):

            if super_class is not None:
                print(args)
                super_object = super_class(*args, **kwargs)
                return child_class(super_object, *args, **kwargs)
            else:
                # bug
                return child_class(lambda: ..., *args, **kwargs)

        new_class.__name__ = child_class.__name__
        new_class.__doc__ = child_class.__doc__

        return new_class

    return decorator


@extends(None)
def Animal(self, name: str):
    self.name = name

    def to_string():
        return f"I am {self.name}"

    self.to_string = to_string
    return self


print(Animal("dog").to_string())


@extends(Animal)  # 太麻烦了
def Fish(self, name: str, color: str):
    self.name = name
    self.color = color

    def to_string():
        return f"I am {self.name}, and my color is {self.color}"

    self.to_string = to_string
    return self


print(Fish("goldfish", "gold").to_string())
