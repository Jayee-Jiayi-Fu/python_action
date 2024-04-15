import random

# 静态方法
# 如果某个方法不需要使用当前实例里的任何内容，那可以使用@staticmethod来定义一个静态方法。


class Cat:
    def __init__(self, name):
        self.name = name

    def say(self):
        sound = self.get_sound()
        print(f'{self.name}: {sound}...')

    @staticmethod
    def get_sound():  # ➊静态方法不接收当前实例作为第一个位置参数
        repeats = random.randrange(1, 10)
        return ' '.join(['Meow'] * repeats)


# 通过示例调用
cat = Cat('Nico')
cat.say()
print(cat.get_sound())

# 通过类调用
print(Cat.get_sound())


'''
静态方法是一种与状态无关的方法，因此静态方法其实可以改写成脱离于类的外部普通函数。
选择静态方法还是普通函数，可以从以下几点来考虑：
· 如果静态方法特别通用，与类关系不大，那么把它改成普通函数可能会更好；
· 如果静态方法与类关系密切，那么用静态方法更好；
· 相比函数，静态方法有一些先天优势，比如能被子类继承和重写等。
'''
