'''类（class）
1. 是面向对象编程里最基本的概念之一。
2. 在一个类中，状态和行为可以被很好地封装在一起，因此它天生适合用来实现有状态对象。
'''

'''实现一个“会轮换屏蔽字符的马赛克「对象」
这个方案最终依赖的CycleMosaic().generate，并非一个有状态的函数，而是一个有状态的实例方法。
但无论是函数还是实例方法，它们都是“可调用对象”的一种，都可以作为re.sub()函数的repl参数使用。
'''




import re
class CyclicMosaic:
    _chars = ['*', 'x']

    def __init__(self):
        self._char_index = 0

    def generate(self, matchobj):
        char = self._chars[self._char_index]
        length = len(matchobj.group())
        self._char_index = (self._char_index + 1) % len(self._chars)
        return length * char


def mosaic_string(s):
    return re.sub(r'\d+', CyclicMosaic().generate, s)


print(mosaic_string('商店共1002000个苹果，小明以2221元每斤的价格买走了122个'))
print(mosaic_string('商店共1002000个苹果，小明以2221元每斤的价格买走了122个'))


'''三种实现有状态函数的方式，这三种方式各有优缺点，总结如下：
基于全局变量：
· 学习成本最低，最容易理解；
· 会增加模块级的全局状态，封装性和可维护性最差。
基于函数闭包：
· 学习成本适中，可读性较好；
· 适合用来实现变量较少，较简单的有状态函数。
创建类来封装状态：
· 学习成本较高；
· 当变量较多、行为较复杂时，类代码比闭包代码更易读，也更容易维护。

在日常编码中，如果你需要实现有状态的函数，应该尽量避免使用全局变量，闭包或类才是更好的选择。'''
