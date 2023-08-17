# Python 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式模式。
# compile 函数根据一个模式字符串和可选的标志参数生成一个正则表达式对象。该对象拥有一系列方法用于正则表达式匹配和替换。
# re 模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串做为它们的第一个参数。
import re


# 1. re.match函数


# 2 re.search
# 扫描整个字符串并返回「第一个」成功的匹配。匹配成功返回一个匹配的对象，否则返回None。
# 语法：re.search(pattern, string, flags=0)
#       pattern	匹配的正则表达式
#       string	要匹配的字符串。
#       flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
print(f" re.search('www', 'www.runoob.com') 运行结果: {re.search('www', 'www.runoob.com')} ")
# TODO re 模块