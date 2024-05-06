# Python语言内部大量使用了字典类型

class Duck:
    def __init__(self, name):

        self.name = name
        self._color = 'yellow'
        self.__age = '1'

    def walk(self):
        print('duck walking')


duck = Duck('Tom')

# ❶实例的__dict__里，保存着当前实例的所有数据
print(f'duck.__dick__: {duck.__dict__}')

# ❷类的__dict__里，保存着类的文档、方法等所有数据
print(f'Duck.__dick__: {Duck.__dict__}')


print('------------------------')


# 在绝大多数情况下，__dict__字典对于我们来说是内部实现细节，并不需要手动操作它。
# 但在有些场景下，使用__dict__可以帮我们巧妙地完成一些特定任务。
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, name, value):
        if name == 'age' and value < 0:
            print('年龄不能少于0')
            value = 0
        super().__setattr__(name, value)


# 比如，你有一份包含Person类数据的字典{'name': ..., 'age': ...}。
p1 = Person('Kim', 30)
d1 = {'name': 'Kimy', 'age': -30}

# 现在你想把这份字典里的数据直接赋值到某个Person实例上。
# 最简单的做法是通过遍历字典来设置属性：
for key, value in d1.items():
    setattr(p1, key, value)
print(f'通过遍历赋值得到的 p1：{p1.__dict__}')


# 但除此之外，其实也可以直接修改实例的__dict__属性来快速达到目的：p.__dict__.update(d)。
p2 = Person('Kim', 30)
d2 = {'name': 'Kimy', 'age': -30}
p2.__dict__.update(d2)
print(f'通过调用__dict__.update 方法得到的 p2：{p2.__dict__}')

# 修改实例的__dict__与循环调用setattr()方法这两个操作并不完全等价，因为类的属性设置行为可以通过定义__setattr__魔法方法修改。
# 虽然普通的属性赋值会被__setattr__限制，但如果你直接操作实例的__dict__字典，就可以无视这个限制：
