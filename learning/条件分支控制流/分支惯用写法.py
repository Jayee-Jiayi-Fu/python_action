# 严格说来Python只有一种条件分支语法——if/elif/else

# 1. 不要显式地和布尔值做比较
# 绝大多数情况下，在分支判断语句里写== True都没有必要
# 除非确实想让分支仅当值是True时才执行


# 2. 省略零值判断
# 当某个对象出现在if分支里时，解释器会进行“真值测试”--调用bool()函数获取它的布尔值
# 计算布尔值时，每类对象都有着各自的规则
print(f'bool(0): {bool(0)}')
print(f'bool(123): {bool(123)}')
print(f'bool([]): {bool([])}, bool([1,2,3]): {bool([1,2,3])}')
# 条件判断时，可以省略值的判断，但这样写其实隐晦地放宽了分支判断的成立条件
# 请时刻注意，不要因为过度追求简写而引入其他逻辑问题。

# 除整型外，其他内置类型的布尔值规则如下：
# · 布尔值为假：None、0、False、[]、()、{}、set()、frozenset()，等等。
# · 布尔值为真：非0的数值、True，非空的序列、元组、字典，用户定义的类和实例，等等。



# 3， 把否定逻辑移入表达式内
# 用not关键字来表达“否定”含义
'''不要这样写：
if not number < 10:
    ...
if not current_user is None:
    ...
if not index == 1:
    ...
'''
# 把否定逻辑移入表达式内，更容易阅读
'''推荐这样写：
if number >= 10:
    ...
if current_user is not None:
    ...
if index  != 1:
    ...
'''


# 4. 尽可能让三元表达式保持简单
# 浓缩版的条件分支——三元表达式
# 不要盲目追求用一个表达式来表达过于复杂的逻辑。有
#  平淡普通的分支语句远远胜过花哨复杂的三元表达式
'''
true_value if <expression> else false_value

language = 'Python' if you.favor('dynamic') else 'golang'
'''

# 5.

