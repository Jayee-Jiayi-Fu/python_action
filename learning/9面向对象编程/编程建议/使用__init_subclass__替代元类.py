'''
__init_subclass__是类的一个特殊钩子方法，它的主要功能是在类派生出子类时，触发额外的操作。
假如某个类实现了这个钩子方法，那么当其他类继承该类时，钩子方法就会被触发。
'''


class Validator:
    '''校验器基类：统一注册所有校验器类，方便后续使用'''
    _validators = {}

    def __init_subclass__(cls, **kwargs):
        print('{} registered, extra kwargs: {}'.format(cls.__name__, kwargs))
        Validator._validators[cls.__name__] = cls


# 定义继承了Validator的子类
class StringValidator(Validator, foo='bar'):
    name = 'string'


class IntegerValidator(Validator):
    name = 'init'


print(Validator._validators)

'''
__init_subclass__非常适合在这种需要触达所有子类的场景中使用。
而且同元类相比，钩子方法只要求使用者了解继承，不用掌握更高深的元类相关知识，门槛低了不少。
它和类装饰器一样，都可以有效替代元类。
'''
