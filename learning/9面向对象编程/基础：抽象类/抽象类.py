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


# 03. 抽象类的子类化机制
class Validator(ABC):  # ❶要定义一个抽象类，需要继承ABC类或使用abc.ABCMeta元类
    '''校验器抽象类'''
    @classmethod
    def __subclasshook__(cls, C):
        print(f'实例所属类型会作为参数传入该方法: {C}')
        '''任何提供了 validate 方法的类，都被当做 Validator 的子类'''
        # ❷C.__mro__代表C的类派生路线上的所有类
        if any('validate' in B.__dict__ for B in C.__mro__):
            return True
        return NotImplemented

    def validate(self, value):
        raise NotImplementedError


# 上面代码的重点是__subclasshook__类方法。__subclasshook__是抽象类的一个特殊方法，
# 当你使用isinstance检查对象是否属于某个抽象类时，如果后者定义了这个方法，那么该方法就会被触发，然后：
# · 实例所属类型会作为参数传入该方法（上面代码中的C参数）；
# · 如果方法返回了布尔值，该值表示实例类型是否属于抽象类的子类；
# · 如果方法返回NotImplemented，本次调用会被忽略，继续进行正常的子类判断逻辑。

# 在我编写的Validator类中，__subclasshook__方法的逻辑是：所有实现了validate方法的类都是我的子类。
# 实例所属类型会作为参数传入该方法
class StringValidator:
    def validate(self, value):
        pass


print(isinstance(StringValidator(), Validator))
