'''
“Python是一门鸭子类型的编程语言。”
也就是说，虽然Python提供了检查类型的函数：isinstance()，但是鸭子类型并不推荐你使用它。
你想调用items对象的append()方法？别拿isinstance(items, list)判断items究竟是不是列表，想调就直接调吧！
假如失败了，那就让它报错好了（参考5.1.1节）。
'''


from io import StringIO


def count_vowels(fp):
    '''统计某个文件中原因字母 aeiou 的数量'''

    # 也可以添加类型校验
    if not hasattr(fp, 'read'):
        raise TypeError('must provide a valid file object')

    VOWELS_LETTER = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for line in fp:  # ❶不做任何类型判断，直接开始遍历fp对象
        for char in line:
            if char.lower() in VOWELS_LETTER:
                count += 1
    return count


# 合法的调用方式：传入是个可读的文件
with open('small_file.txt') as fp:
    count = count_vowels(fp)
    print(count)


# 假如调用方提供的fp参数不是文件对象怎么办？答案是：不怎么办，直接报错就好。
try:
    count_vowels(100)
except TypeError as e:
    print(f'传入类型不是一个文件对象: {e}')

'''
❶新增的校验语句
不管怎样，在纯粹的鸭子类型编程风格下，不应该出现任何的isinstance类型判断语句。
鸭子类型不推荐做类型检查，因此编码者可以省去大量与之相关的烦琐工作。
鸭子类型只关注对象是否能完成某件事，而不对类型做强制要求，这大大提高了代码的灵活性。
'''

# 假如把一个StringIO对象——一种实现了read操作的类文件（file-like）对象——传入上面的count_vowels()函数，会发现该函数仍然可以正常工作：
count = count_vowels(StringIO('Hello, world!'))
print(count)


# 自定义一个实现了read方法的新类
# count_vowels()函数遵循了鸭子类型编程风格，而StringList恰好实现了它所需要的接口，因此StringList对象也可以完美适用于count_vowels函数
class StringList:
    """用于保存多个字符串的数据类，实现了read() 和可迭代接口"""

    def __init__(self, strings):
        self.strings = strings

    def read(self):
        return ''.join(self.strings)

    def __iter__(self):
        for s in self.strings:
            yield s


count = count_vowels(StringList('Hello, world!'))
print(count)


'''
鸭子类型的局限性

1. 缺乏标准。
在编写鸭子类型代码时，虽然我们不需要做严格的类型校验，但是仍然需要频繁判断对象是否支持某个行为，而这方面并没有统一的标准。
拿前面的文件类型校验来说，你可以选择调用hasattr(fp, "read")，也可以选择调用hasattr(fp,"readlines")，还可以直接写try ... except的EAFP风格代码来直接进行操作。

2. 过于隐式。
在鸭子类型编程风格下，对象的真实类型变得不再重要，取而代之的是对象所提供的接口（或者叫协议）变得非常重要。
但问题是，鸭子类型里的所有接口和协议都是隐式的，它们全藏在代码和函数的注释中。
举个例子，通过阅读count_vowels()函数的代码，你可以知道：fp文件对象需要提供read方法，也需要可迭代。
但这些规则都是隐式的、片面的。这意味着你虽然通过读代码了解了大概，但是仍然无法回答这个问题：“究竟是哪些接口定义了文件对象？”。
在鸭子类型里，所有的接口和协议零碎地分布在代码的各个角落，最终虚拟地活在编码者的大脑中。


综合考虑了鸭子类型的种种特点后，你会发现，虽然这非常有效和实用，但有时也会让人觉得过于灵活、缺少规范。
尤其是在规模较大的Python项目中，如果代码大量使用了鸭子类型，编码者就需要理解很多隐式的接口与规则，很容易不堪重负。

幸运的是，除了鸭子类型以外，Python还为类型系统提供了许多有效的补充，
比如类型注解与静态检查（mypy）、抽象类（abstract class）等。
'''

