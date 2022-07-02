from collections import namedtuple

# 两种方法来给 namedtuple 定义方法名
User = namedtuple('User', ['name', 'age', 'id'])
user = User('tester', '22', '464643123')

print(user)
# User(name='tester', age='22', id='464643123')

