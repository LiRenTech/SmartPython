import random
from typing import *

class MyRandom(random.Random):
    def __init__(self, x: Any = ...):
        super().__init__(x)

    def random(self, *args, **kwargs):
        print("调用了random")
        return super().random(*args, **kwargs)

    def randint(self, *args, **kwargs):
        """
        randint就是randrange
        原始定义：
        def randint(self, a, b):
            return self.randrange(a, b+1)
        """
        print("调用了randint")
        return super().randint(*args, **kwargs)

    def randrange(self, *args, **kwargs):
        print("调用了randrange")
        return super().randrange(*args, **kwargs)

myrandom = MyRandom()

# 所有有关随机的方法都会调用random，最终调用_randbelow
# randint其实就是randrange
print("randint")
myrandom.randint(1, 10)
print("randrange")
myrandom.randrange(10)
print("choice")
myrandom.choice((1, 2, 3))
