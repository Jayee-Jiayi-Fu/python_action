# 用于判断对象类型的isinstance()函数在鸭子世界里完全没有用武之地。
# 但是，自从抽象类出现以后，isinstance()函数的地位发生了一些微妙的变化

# 01. sinstance()的典型工作模式
from abc import ABC
from collections.abc import Iterable


class Validator:
    '''校验器基类，校验不同种类的数据是否符合要求'''

    def validate(self, value):
        raise NotImplementedError


class NumberValidator(Validator):
    '''是继承了Valdiator的校验器子类,校验输入值是否是合法数字'''

    def validate(self, value):
        pass


# 利用isinstance()函数，我们可以判断对象是否属于特定类型
print(isinstance(NumberValidator(), NumberValidator))  # True
# isinstance()函数能理解类之间的继承关系，因此子类的实例同样可以通过基类的校验
print(isinstance(NumberValidator(), Validator))  # True
print(isinstance('foo', Validator))  # False


# 02. 校验对象是否是iterable类型
class ThreeFactory:
    '''在被迭代时，不断返回3
    :param repeat：重复次数
    '''

    def __init__(self, repeat):
        self.repeat = repeat

    def __iter__(self):
        for _ in range(self.repeat):
            yield 3


obj = ThreeFactory(6)
for i in obj:
    print(i)

# 虽然ThreeFactory没有继承Iterable类，但当我们用isinstance()检查它是否属于Iterable类型时，结果却是True，
# 这正是受了抽象类的特殊子类化机制的影响。
print(isinstance(obj, Iterable))  # True


