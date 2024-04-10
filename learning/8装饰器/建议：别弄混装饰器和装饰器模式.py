'''
事实上，《设计模式》一书中的“装饰器模式”与Python里的“装饰器”截然不同。装饰器模式属于面向对象领域。
实现装饰器模式，需要具备以下关键要素：
· 设计一个统一的接口；
· 编写多个符合该接口的装饰器类，每个类只实现一个简单的功能；
· 通过组合的方式嵌套使用这些装饰器类；
· 通过类和类之间的层层包装来实现复杂的功能。
'''


class Numbers:
    """一个包含多个数字的简单类"""

    def __init__(self, numbers):
        self.numbers = numbers

    def get(self):
        return self.numbers


class EvenOnlyDecorator:
    """装饰器类：过滤所有偶数"""

    def __init__(self, decorated):
        self.decorated = decorated

    def get(self):
        return [num for num in self.decorated.get() if num % 2 == 0]


class GreaterThanDecorator:
    """装饰器类：过滤大于某个数的数"""

    def __init__(self, decorated, min_value):
        self.decorated = decorated
        self.min_value = min_value

    def get(self):
        return [num for num in self.decorated.get() if num > self.min_value]


obj = Numbers([42, 12, 13, 17, 18, 41, 32])
even_obj = EvenOnlyDecorator(obj)
gt_obj = GreaterThanDecorator(even_obj, min_value=30)
print(gt_obj.get())

# 装饰器模式和Python里的装饰器毫不相干。如果硬要找一点儿联系，它俩可能都和“包装”有关——一个包装函数，另一个包装类。
