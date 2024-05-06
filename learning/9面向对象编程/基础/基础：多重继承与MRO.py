class A:
    def say(self):
        print('A')


class B(A):
    pass


class C(A):
    def say(self):
        print('C')


class D(B, C):
    pass


D().say()  # C


# 在解决多重继承的方法优先级问题时，
# Python使用了一种名为MRO（method resolution order）的算法。该算法会遍历类的所有基类，并将它们按优先级从高到低排好序。


# 调用类的mro()方法，你可以看到按MRO算法排好序的基类列表：
print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# ❶这里面的<class 'object'>是每个Python类的默认基类

# 当你调用子类的某个方法时，Python会按照上面的MRO列表从前往后寻找这个方法，
# 假如某个类实现了这个方法，就直接返回。这就是前面的D().say()定位到了C类的原因，因为在D的MRO列表中，C排在A的前面。


# MRO 与super()
# 基于MRO算法的基类优先级列表，不光定义了类方法的找寻顺序，还影响了另一个常见的内置函数：super()。
# 在许多人的印象中，super()是一个用来调用父类方法的工具函数。但这么说并不准确，super()使用的其实不是当前类的父类，而是它在MRO链条里的上一个类。
class AA:
    def __init__(self):
        print("I'm AA")
        super().__init__()


class BB(AA):
    def __init__(self):
        print("I'm BB")
        super().__init__()


class CC(AA):
    def __init__(self):
        print("I'm CC")
        super().__init__()


class DD(BB, CC):
    pass


print(DD.mro())
DD()


# Python里的多重继承是一个相当复杂的特性，尤其在配合super()时。在实际项目里，你应该非常谨慎地对待多重继承
# 大多数情况下，你需要的并不是多重继承，而也许只是一个更准确的抽象模型，在该模型下，最普通的继承关系就能完美解决问题。
