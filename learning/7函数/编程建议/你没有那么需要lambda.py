'''
Python中有一类特殊的函数：匿名函数。
用lambda关键字来快速定义一个匿名函数，比如lambda x, y: x + y。
'''

# 常见场景1：作为sorted()函数的排序参数使用
from operator import itemgetter
ll = []
sorted(ll, key=lambda item: item.score)

# 常见场景2：做一些简单的操作运算，比如通过key获取字典值、通过属性名获取对象值，等等
sorted(ll, key=lambda obj: obj['name'])


# 于这种进行简单操作的匿名函数，用operator模块里的函数来替代。
# 比如使用operator.itemgetter()就可以直接实现“获取某个key的值”操作：
# 调用itemgetter('name')会生成一个新函数,使用obj参数调用新函数，效果等同于表达式obj['name']
itemgetter('name')({'name': 'foo'})
# 改写成
sorted(ll, itemgetter('name'))


# 除了itemgetter()以外，operator模块里还有许多有用的函数，它们都可以用来替代简单的操作运算类匿名函数，
# 比如add()、attrgetter()等，
# 详细列表可以查询官方文档： https://docs.python.org/zh-cn/3.12/library/operator.html


# Python中的lambda函数只是一颗简单的语法糖。
# 它的许多使用场景，要么本身就不存在，要么更适合用operator模块来满足。lambda并非无可替代
