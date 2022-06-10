import builtins
from collections import ChainMap


# https://blog.csdn.net/langb2014/article/details/100122209
def collection_test2():
    a = {"name": 15555}
    b = {"age": 24}
    c = {"wife": "qian"}
    lookUp = ChainMap(a, b, c)
    print(lookUp)

    print(lookUp['age'])  # 相当于字典合并
    print(lookUp.maps)  # 视图？？
    lookUp.update({"age": 25})
    print(lookUp)
    b['age'] = 26
    print(lookUp)
    print(type(lookUp.maps))
    lookUp.maps[0]['age'] = 20
    lookUp.maps[1]['age'] = 22
    print(lookUp)
    print("-----------")
    d = {"name": "leng"}
    e = {"name": "123"}
    cm = ChainMap(d, e)
    print(cm)
    print(cm['name'])


collection_test2()
