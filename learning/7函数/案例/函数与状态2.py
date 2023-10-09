'''
要求1. 有一段文字，里面包含各类数字，比如数量、价格等，编写一段代码把文字里的所有数字都用星号替代，实现脱敏的效果。
要求2. 进一步修改函数，保留每个被替换数字的原始长度，比如100应该被替换成***

原始文本：商店共100个苹果，小明以12元每斤的价格买走了8个。
目标文本：商店共*个苹果，小明以*元每斤的价格买走了*个。
'''

'''匹配到数据的话，使⽤group⽅法来提取数据。
以使用group(num) 或 groups() 获取匹配表达式。
    group()用来提出分组截获的字符串，group() 同group（0）就是匹配正则表达式整体结果，
    group(1) 列出第一个括号匹配部分，group(2) 列出第二个括号匹配部分，
    没有匹配成功的，re.search()返回None。
'''

import re

def mosaic_matchobj(matchobj):
    '''将匹配到的模式替换为等长型号字符串'''
    length = len(matchobj.group())
    return '*'*length

def mosaic_string(s):
    '''用等长的 * 替代输入字符串里所有的连续数字'''
    return re.sub(r'\d+', mosaic_matchobj, s)

s = mosaic_string('商店共1000个苹果，小明以12元每斤的价格买走了8个')
print(s)