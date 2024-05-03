# 元类是Python中的一种特殊对象。
# 元类控制着类的创建行为，就像普通类控制着实例的创建行为一样。
# type是Python中最基本的元类，利用type，你根本不需要手动编写class ... :代码来创建一个类——直接调用type()就行：

import random
import types
import time
Foo = type('Foo', (), {'bar': 3})
print(Foo, Foo.bar, Foo.mro())


# ❶参数分别为type(name, bases, attrs)
# 在调用type()创建类时，需要提供三个参数，它们的含义如下。

# （1） name：str，需要创建的类名
# （2） bases：Tuple[Type]，包含其他类的元组，代表类的所有基类。
# （3） attrs：Dict[str, Any]，包含所有类成员（属性、方法）的字典。


# 虽然type是最基本的元类，但在实际编程中使用它的场景其实比较少。
# 更多情况下，我们会创建一个继承type的新元类，然后在里面定制一些与创建类有关的行为。


class AutoPropertyMeta(type):  # ❶元类通常会继承基础元类type对象
    """元类：
    - 把所有类方法变成动态属性
    - 为所有实例增加创建时间属性
    """
    def __new__(cls, name, bases, attrs):  # ❷元类的__new__方法会在创建类时被调用
        for key, value in attrs.items():
            if isinstance(value, types.FunctionType) and not key.startswith('_'):
                attrs[key] = property(value)  # ❸将非私有方法转换为属性对象

        return super().__new__(cls, name, bases, attrs)  # ❹调用type()完成真正的类创建

    def __call__(cls, *args, **kwargs):  # ❺元类的__call__方法，负责创建与初始化类实例
        inst = super().__call__(*args, **kwargs)
        inst.created_at = time.time()
        return inst


# 下面的Cat类使用了AutoPropertyMeta元类：
class Cat(metaclass=AutoPropertyMeta):
    def __init__(self, name):
        self.name = name

    def sound(self):
        repeats = random.randrange(1, 10)
        return ' '.join(['Meow'] * repeats)


nico = Cat('Nico')
print(nico.sound)  # ❶sound原本是方法，但是被元类自动转换成了属性对象
print(nico.created_at)  # ❷读取由元类定义的创建时间


'''
元类很少被使用的原因，除了应用场景少以外，还在于它其实有许多“替代品”，它们是：
（1）类装饰器（见8.2.2节）；
（2）__init_subclass__钩子方法（见9.3.1节）；
（3）描述符（见12.1.3节）。
这些工具的功能虽然不如元类那么强大，但它们都比元类简单，更容易理解。日常编码时，它们可以覆盖元类的大部分使用场景。
'''
