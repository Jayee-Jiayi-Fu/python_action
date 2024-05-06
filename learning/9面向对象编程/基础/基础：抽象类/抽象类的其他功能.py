from abc import ABC, abstractmethod


# 04．抽象类的其他功能
# 利用abc模块的@abstractmethod装饰器，你可以把某个方法标记为抽象方法。
# 假如抽象类的子类在继承时，没有『重写所有』抽象方法，那么它就无法被正常实例化。
class Validator(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def validate(self, value):
        raise NotImplementedError


class InvalidValidator(Validator):
    # def validate(self, value):
    #     print(value)

    pass


# 尝试实例化 InvalidValidator    报错
obj = InvalidValidator()
