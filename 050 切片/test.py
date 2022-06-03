class A:
    def __init__(self):
        self.arr = [i for i in range(10)]

    def __getitem__(self, item):
        if type(item) == tuple:
            for obj in item:
                print(obj)
        if type(item) is int:
            return self.arr[item]
        else:
            print(item)



