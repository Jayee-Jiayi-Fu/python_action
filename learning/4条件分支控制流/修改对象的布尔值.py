# 某个对象用于分支判断时，解释器会对它进行“真值测试”，计算出它的布尔值
# 默认情况下，所有用户自定义的类和类实例的计算结果都是True
class Foo():
    pass


print(f'bool(Foo): {bool(Foo)}')


class UserCollection():
    def __init__(self, users):
        self.items = users


users1 = []
users2 = [1, 2]
print(f'users1 = [], bool(UserCollection(users1)): { bool(UserCollection(users1)) }')
print(f'users2 = [1, 2], bool(UserCollection(users2)): { bool(UserCollection(users2)) }')


# 1. 修改__len__
# 为类定义__len__魔法方法，实际上就是为它实现了Python世界的长度协议
# Python在计算这类对象的布尔值时，会受len(users)的结果影响
class UserCollection_len():
    def __init__(self, users):
        self.items = users

    def __len__(self):
        return len(self.items)


users1 = []
users2 = [1, 2]
print(f'users1 = [], bool(UserCollection_len(users1)): { bool(UserCollection_len(users1)) }')
print(f'users2 = [1, 2], bool(UserCollection_len(users2)): { bool(UserCollection_len(users2)) }')


# 2. 修改 __bool__
# 为对象定义__bool__方法后，对它进行布尔值运算会直接返回该方法的调用结果
# 同时定义了__len__和__bool__两个方法，解释器会优先使用__bool__方法的执行结果
class UserCollection_bool():
    def __init__(self, users):
        self.items = users

    def __len__(self):
        return len(self.items)

    def __bool__(self):
        return False


users1 = []
users2 = [1, 2]
print(f'users1 = [], bool(UserCollection_bool(users1)): { bool(UserCollection_bool(users1)) }')
print(f'users2 = [1, 2], bool(UserCollection_bool(users2)): { bool(UserCollection_bool(users2)) }')
