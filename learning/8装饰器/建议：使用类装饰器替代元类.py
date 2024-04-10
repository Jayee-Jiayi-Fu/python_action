'''
Python中的元类（metaclass）是一种特殊的类。就像类可以控制实例的创建过程一样，元类可以控制类的创建过程
'''


# 利用元类统一注册所有Validator类：
_validators = {}


class ValidatorMeta(type):
    '''元类：统一注册所有校验器类，方便后续使用'''

    def __new__(cls, name, bases, attrs):
        ret = super().__new__(cls, name, bases, attrs)
        _validators[attrs['name']] = ret
        return ret


class StringValidator(metaclass=ValidatorMeta):
    name = 'string'


class IntegerValidator(metaclass=ValidatorMeta):
    name = 'int'


print(f'查看注册结果: {_validators}')


'''
虽然元类的功能很强大，但它的学习与理解成本非常高。
其实，对于实现上面这种常见需求，并不是非使用元类不可，使用类装饰器也能非常方便地完成同样的工作。

类装饰器的工作原理与普通装饰器类似。下面的代码就用类装饰器实现了ValidatorMeta元类的功能：

'''
_validators2 = {}


def register(cls):
    _validators2[cls.name] = cls
    return cls


@register
class StringValidator2:
    name = 'string'


@register
class IntegerValidator2:
    name = 'int'


print(f'查看注册结果2: {_validators2}')


'''
相比元类，使用类装饰器的代码要容易理解得多。
除了上面的注册功能以外，你还可以用类装饰器完成许多实用的事情，比如实现单例设计模式、自动为类追加方法，等等。
虽然类装饰器并不能覆盖元类的所有功能，但在许多场景下，类装饰器可能比元类更合适，
因为它不光写起来容易，理解起来也更简单。像广为人知的标准库模块dataclasses里的@ dataclass就选择了类装饰器，而不是元类。
'''
