import random


# 类方法
# 可以通过类名调用的方法称为类方法

class Duck:
    def __init__(self, color):
        self.color = color

    def quack(self):
        print(f"Hi, I'm a {self.color} duck!")

    # 用@classmethod装饰器定义一种特殊的方法：类方法（class method），它属于类但是无须实例化也可调用。
    @classmethod
    def creat_random(cls):  # ❶普通方法接收类实例（self）作为参数，但类方法的第一个参数是类本身，通常使用名字cls
        color = random.choice(['yellow', 'green', 'red'])
        return cls(color=color)


# 调用方法需要先创建一个类实例。
duck = Duck('yellow')
duck.quack()
# 直接通过类调用会报错
try:
    Duck.quack()
except TypeError as e:
    print(e)  # Duck.quack() missing 1 required positional argument: 'self'


# 类可以直接调用类方法
duck = Duck.creat_random()
duck.quack()

# 也可以通过实例来调用类方法，效果一样
duck2 = duck.creat_random()
print(duck2)
