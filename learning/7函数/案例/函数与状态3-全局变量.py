import re

'''
要求1. 有一段文字，里面包含各类数字，比如数量、价格等，编写一段代码把文字里的所有数字都用星号替代，实现脱敏的效果。
要求2. 进一步修改函数，保留每个被替换数字的原始长度，比如100应该被替换成***
要求3. 请在替换数字时加入一些更有趣的逻辑——全部使用星号*来替换，显得有些单调，如果能轮换使用*和x两种符号就好了。

原始文本：商店共100个苹果，小明以12元每斤的价格买走了8个。
目标文本：商店共***个苹果，小明以xx元每斤的价格买走了*个。
'''


'''方法1：全局变量记录状态
用全局变量保存状态，其实是写代码时最应该避开的事情之一

这种方式封装性特别差，代码里的mosaic_global_var()函数不是一个完整可用的对象，必须配合一个模块级状态_mosaic_char_index使用

其次，这种方式非常脆弱。如果多个模块在不同线程里，同时导入并使用mosaic_global_var()函数，
整个字符轮换的逻辑就会乱掉，因为多个调用方共享同一个全局标记变量_mosaic_char_index

最后，现在的函数提供的调用结果甚至都不稳定。如果连续调用函数，会出现 * 和 x 给不同数字脱敏的情况
'''
_mosaic_char_index = 0


def mosaic_global_var(matchobj):
    '''用global关键字声明一个全局变量'''
    global _mosaic_char_index

    mosaic_chars = ['*', "x"]
    char = mosaic_chars[_mosaic_char_index]

    # 递增马赛克字符索引值
    _mosaic_char_index = (_mosaic_char_index + 1) % len(mosaic_chars)

    '''将匹配到的模式替换为等长型号字符串'''
    print(f'matchobj.group():{matchobj.group()}')
    length = len(matchobj.group())
    return char * length


def mosaic_string(s):
    '''用等长的 * 替代输入字符串里所有的连续数字'''
    return re.sub(r'\d+', mosaic_global_var, s)


s = '商店共1000个苹果，小明以12元每斤的价格买走了8个'
print('1', mosaic_string(s))  # 商店共****个苹果，小明以xx元每斤的价格买走了*个
print('2', mosaic_string(s))
