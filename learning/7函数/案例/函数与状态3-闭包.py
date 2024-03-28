
import re

'''闭包：
1. 一种允许函数访问已执行完成的其他函数里的私有变量的技术
2. 是为函数增加状态的另一种方式
3. 相比全局变量，使用闭包最大的特点就是封装性要好得多
'''

'''闭包示例
def counter():
    value = 0
    def _counter():
        # nonlocal 用于标注变量来自上层作用域，如果不标明，内层函数无法直接修改外层函数变量
        nonlocal value
        value += 1
        return value
    return _counter
c = counter()
print(c(),c(),c())
'''

'''使用闭包的有状态替换函数'''


def make_cyclic_mosic():
    char_index = 0
    mosaic_chars = ['*', 'x']

    def _make_cyclic_mosic(matchobj):
        nonlocal char_index
        length = len(matchobj.group())
        char = mosaic_chars[char_index]

        # 递增马赛克字符索引值
        char_index = (char_index + 1) % len(mosaic_chars)

        return length * char

    return _make_cyclic_mosic


def mosaic_string(s):
    return re.sub(r'\d+', make_cyclic_mosic(), s)


print(mosaic_string('商店共1000个苹果，小明以12元每斤的价格买走了8个'))
print(mosaic_string('商店共1000个苹果，小明以12元每斤的价格买走了8个'))
