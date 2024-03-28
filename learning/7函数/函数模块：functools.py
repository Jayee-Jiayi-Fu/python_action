# functools
# https://docs.python.org/zh-cn/3.12/library/functools.html
# 是一个专门用来处理函数的内置模块，其中有十几个和函数相关的有用工具

# 场景：首先有一个接收许多参数的函数a，然后额外定义一个接收更少参数的函数b，通过在b内部补充一些预设参数，最后返回调用a函数的结果
# 01．functools.partial(func, *arg, **kwargs)
# · func是完成具体功能的原函数；
# · *args/**kwargs是可选位置与关键字参数，必须是原函数func所接收的合法参数。
# 返回一个新的可调用对象（callable object）——偏函数partial_obj。
# 在调用partial_obj对象时提供了额外参数，会首先将本次调用参数和构造partial_obj时的参数进行合并，然后传给原始函数func处理，

import time
import functools


def multiply(x, y):
    return x * y


def double(value):
    # 返回 multiply 函数调用结果
    return multiply(2, value)


double2 = functools.partial(multiply, 2)


# 场景：当函数执行一些耗时较长的操作，可能会导致函数执行速度慢，比如调用第三方API、进行复杂运算等。给这类慢函数加上缓存是比较常见的做法。
# 02．functools.lru_cache(maxsize)
# 可选的maxsize参数，表示当前函数最多可以保存多少个缓存结果。
# 当缓存的结果数量超过maxsize以后，程序就会基于“最近最少使用”（least recently used，LRU）算法丢掉旧缓存，释放内存。
# maxsize设置为None，函数就会保存每一个执行结果，不再剔除任何旧缓存。这时如果被缓存的内容太多，就会有占用过多内存的风险。
# 默认情况下，maxsize的值为128。

# 使用它，你可以方便地给函数加上缓存功能，同时不用修改任何函数内部代码。


def calculate_score(class_id):
    print(f'Calculating score for class: {class_id}...')
    # 模拟一些耗时很久的代码
    time.sleep(3)
    return 42


print(calculate_score(100))
print(calculate_score(100))


# 因为caculate_score()函数执行耗时较长，而且每个class_id的统计结果都是稳定的，所以我可以直接使用lru_cache()为它加上缓存：
@functools.lru_cache(maxsize=None)
def calculate_score_v2(class_id):
    print(f'Calculating score for class: {class_id}...')
    time.sleep(3)
    return 42


print(calculate_score_v2(100))
print(calculate_score_v2(100))
