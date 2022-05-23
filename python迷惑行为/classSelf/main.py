class Mountain:
    def __init__(self):
        self.temple = Mountain()  # 无限递归了


class Human:
    def __init__(self):
        self.生孩子 = Human


h = Human()
h2 = h.生孩子().生孩子().生孩子().生孩子().生孩子()
print(h2)




