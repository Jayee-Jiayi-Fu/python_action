import dis
from textwrap import dedent
import timeit


# 使用内置模块 dis 模块反汇编成汇编代码
def add(x, y):
    return x + y


dis.dis(add)


# 1. 不必预计算字面量表达式
# 保留整个算式,这样做对性能没有任何影响，而且会让代码更容易阅读
def do_something(delta_seconds):
    if delta_seconds < 11 * 24 * 3600:
        return


dis.dis(do_something)


# 2. 使用特殊数字：“无穷大”
# Pythond 的最大/最小：float("inf")和float("-inf")
def sort_users_age(users):
    '''用户名按照年龄升序排序，没有提供年龄的放在最后。'''

    def key_func(name):
        age = users[name]
        return age if age is not None else float('inf')

    return sorted(users.keys(), key=key_func)


users = {
    'Tom': 19,
    'Jenny': 13,
    'Jack': None,
    'Andrew': 43
}
print(sort_users_age(users))

# 3. 改善超长字符串的可读性
# 3.1 拿括号将长字符串包起来
s = ("This is the first line of a long string,"
     "this is the second line")

# 3.2 多级缩进里出现多行字符串（标准库 textwrap）
user = {}


def main():
    if user.is_active:
        message = dedent("""\
        Welcome, today's movie list:
        - Jaw(1975)
        - The Shining(1980)
        - Saw(2044)""")


# 3.3 多级缩进里出现多行字符串
# 从右往左处理的“逆序”方法


# 4. 不要害怕字符串拼接
WORDS = ['Hello', 'string', 'performance', 'test'] * 25


def str_cat():
    """使用字符串拼接"""
    s = ''
    for word in WORDS:
        s += word
    return s


def str_join():
    """使用列表配合join生成字符串"""
    l = []
    for word in WORDS:
        l.append(word)
    return ''.join(l)


cat_spent = timeit.timeit(
    setup='from __main__ import str_cat', stmt='str_cat()')
print('cat_spent:', cat_spent)
str_join = timeit.timeit(
    setup='from __main__ import str_join', stmt='str_join()')
print('join_spent:', str_join)
