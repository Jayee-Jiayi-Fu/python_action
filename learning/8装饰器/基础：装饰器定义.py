# Python的装饰器仅仅是一颗语法糖
# 装饰器并不提供任何独特的功能，它只是在函数定义语句上方，直接添加用来修改函数行为的装饰器

# 假如没有装饰器，我们也可以在完成函数定义后，手动做一次包装和重新赋值。

# 但正是因为装饰器提供的这一丁点儿好处，“通过包装函数来修改函数”这件事变得简单和自然起来


'''
装饰器是一种通过包装目标函数来修改其行为的特殊高阶函数，
绝大多数装饰器是利用函数的闭包原理实现的。
'''

import time
import random


def timer(func):
    '''装饰器:打印函数耗时'''

    '''
    在写装饰器时，我一般把decorated叫作“包装函数”。
    这些包装函数通常接收任意数目的可变参数(*args, **kwargs)，主要通过调用原始函数func来完成工作。
    在包装函数内部，常会增加一些额外步骤，比如打印信息、修改参数等。
    '''
    def decorated(*args, **kwargs):
        st = time.perf_counter()
        ret = func(*args, **kwargs)
        print('time cost: {} seconds'.format(time.perf_counter() - st))
        return ret

    return decorated


@timer
def random_sleep():
    '''当其他函数应用了timer装饰器后，包装函数decorated会作为装饰器的返回值，完全替换被装饰的原始函数func。'''
    time.sleep(random.random())


random_sleep()
