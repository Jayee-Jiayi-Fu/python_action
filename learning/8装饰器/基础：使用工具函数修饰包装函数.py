'''
在装饰器包装目标函数的过程中，常会出现一些副作用，其中一种是丢失函数元数据
——函数的所有元数据都变成了装饰器的内层包装函数decorated的值


另一个更大的问题，如果装饰器中要为原始函数增加额外属性（或函数）也会丢失
'''

from functools import wraps
import random
import time


def timer1(func):
    def decorated(*args, **kwargs):
        st = time.perf_counter()
        ret = func(*args, **kwargs)
        print('time cost: {} seconds'.format(time.perf_counter() - st))
        return ret

    return decorated


@timer1
def random_sleep1():
    time.sleep(random.random)


print(random_sleep1.__name__)
print('--------------------------------------------------------')


def timer2(func):
    def decorated(*args, **kwargs):
        st = time.perf_counter()
        ret = func(*args, **kwargs)
        print('time cost: {} seconds'.format(time.perf_counter() - st))
        return ret

    return decorated


def calls_counter2(func):
    '''装饰器：记录函数被调用了多少次

    使用 func.print_counter() 可以打印统计到的信息
    '''
    counter = 0

    def decorated(*args, **kwargs):
        nonlocal counter
        counter += 1
        return func(*args, **kwargs)

    def print_counter():
        print(f'Counter: {counter}')

    decorated.print_counter = print_counter
    return decorated


@timer2
@calls_counter2
def random_sleep2():
    time.sleep(random.random())


try:
    random_sleep2()
    random_sleep2.print_counter()
except AttributeError as e:
    '''
    报警原因：
    ❶首先，由calls_counter对函数进行包装，此时的random_sleep变成了新的包装函数，包含print_counter属性
    ❷使用timer包装后，random_sleep变成了timer提供的包装函数，原包装函数额外的print_counter属性被自然地丢掉了
    '''
    print(e)

print('--------------------------------------------------------')


def timer3(func):
    '''
    functools模块下的wraps()函数
    用于在装饰器内包装函数时，保留原始函数的额外属性
    wraps()首先会基于原函数func来更新包装函数decorated的名称、文档等内置属性，之后会将func的所有额外属性赋值到decorated上
    '''
    @wraps(func)
    def decorated(*args, **kwargs):
        st = time.perf_counter()
        ret = func(*args, **kwargs)
        print('time cost: {} seconds'.format(time.perf_counter() - st))
        return ret

    return decorated


def calls_counter3(func):
    '''装饰器：记录函数被调用了多少次

    使用 func.print_counter() 可以打印统计到的信息
    '''
    counter = 0

    @wraps(func)
    def decorated(*args, **kwargs):
        nonlocal counter
        counter += 1
        return func(*args, **kwargs)

    def print_counter():
        print(f'Counter: {counter}')

    decorated.print_counter = print_counter
    return decorated


@timer3
@calls_counter3
def random_sleep3():
    '''随机睡眠一小会儿'''
    time.sleep(random.random())


print(random_sleep3.__name__, random_sleep3.__doc__)
random_sleep3()
random_sleep3.print_counter()


# 在编写装饰器时，切记使用@functools.wraps()来修饰包装函数。
