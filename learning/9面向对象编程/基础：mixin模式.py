# Mixin是一种把额外功能“混入”某个类的技术。
# 有些编程语言（比如Ruby）为Mixin模式提供了原生支持，而在Python中，我们可以用多重继承来实现Mixin模式。

# 要实现Mixin模式，你需要先定义一个Mixin类
# ❶Mixin类名常以“Mixin”结尾，这算是一种不成文的约定
# 相比普通类，Mixin类有一些鲜明的特征:
# 	Mixin类通常很简单，只实现一两个功能，所以很多时候为了实现某个复杂功能，一个类常常会同时混入多个Mixin类。
# 	另外，大多数Mixin类不能单独使用，它们只有在被混入其他类时才能发挥最大作用。
class InfoDumperMixin:

    '''Mixin: 输出当前示例信息'''

    def dump_info(self):
        d = self.__dict__
        print('Number of members: {}'.format(len(d)))
        print('Details:')
        for key, value in d.items():
            print(f'- {key}: {value}')


# 使用InfoDumperMixin
class Person(InfoDumperMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('Jayee', '31')
p.dump_info()


# 虽然Python中的Mixin模式基于多重继承实现，但令Mixin区别于普通多重继承的最大原因在于：Mixin是一种有约束的多重继承。
# 在Mixin模式下，虽然某个类会同时继承多个基类，但里面最多只会有一个基类表示真实的继承关系，剩下的都是用于混入功能的Mixin类。
# 这条约束大大降低了多重继承的潜在危害性。许多流行的Web开发框架使用了Mixin模式，比如Django、DRF[插图]等。
# 不过，虽然Mixin是一种行之有效的编程模式，但不假思索地使用它仍然可能会带来麻烦。
# 有时，人们使用Mixin模式的初衷，只是想对糟糕的模型设计做一些廉价的弥补，而这只会把原本糟糕的设计变得更糟。
# 假如你想使用Mixin模式，需要精心设计Mixin类的职责，让它们和普通类有所区分，这样才能让Mixin模式发挥最大的潜力。
