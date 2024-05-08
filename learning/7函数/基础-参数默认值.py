# 1. 函数默认参数
def power(x, n=2):
    r = 1
    while n > 0:
        r = x * r
        n = n - 1
    return r


print(power(5, 1), power(5), power(5, 3))


# 2. 参数陷阱： 别将可变类型作为参数默认值
# 第二次执行时，items的值不再是函数定义的空列表[]，而是变成了第一次执行后的结果['foo']
# Python函数的参数默认值只会在函数定义阶段被创建一次，之后不论再调用多少次，函数内拿到的默认值都是同一个对象
print('>>>参数陷阱： 别将可变类型作为参数默认值')


def append_value(value, items=[]):
    items.append(value)
    return items


r = append_value('foo')
print(r)
r = append_value('bar')
print(r)


# 通过函数对象的保留属性__defaults__直接读取这个默认值
# 通过__defaults__属性可以直接获取函数的参数默认值
print(f'__defaults__属性：{append_value.__defaults__}')
append_value.__defaults__[0].append('defaults')
append_value('after')
print(f'__defaults__属性：{append_value.__defaults__}')


# 较常见解决办法：用None替代可变类型默认值
def append_value(value, items=None):
    if items is None:
        items = []
    items.append(value)
    return items


# 3. 定义特殊对象来区分是否提供了默认参数
'''问题描述：
def dump_value(value, extra = None):
    if extra is None:
        无法区分 None 是不是主动传入

两种调用方式
dump_value(value)
dump_value(value, extra=None)
'''
# 最常见解决办法：定义一个特殊对象（标记变量）作为参数默认值
# object 通常不会单独使用，但是拿来做标记变量刚刚好
_not_set = object()


def dump_value(value, extra=_not_set):
    if extra is _not_set:
        # 调用方没有传递 extra 参数
        pass
