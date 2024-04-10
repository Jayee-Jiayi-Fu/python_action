import time
'''用嵌套函数来实现装饰器，接收参数总比不接收参数的装饰器代码多一层嵌套。

# 1. 接收参数的装饰器：2 层嵌套
def delayed_start(duration=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            ...
        return wrapper
    return decorator

# 2. 不接收参数的装饰器：1 层嵌套
def delayed_start(func):
    def wrapper(*args, **kwargs):
        ...
    return wrapper


'''


'''如果实现的是一个接受参数的装饰器，即便所有参数都是有默认值的可选参数，也必须在使用装饰器时加上括号：

@delayed_start(duration=2) ➊

@delayed_start() ➋


--利用仅限关键字参数，能让我们省去那对括号
'''


def delayed_start(func=None, *, duration=1):  # 把所有参数都变成提供了默认值的可选参数
    '''装饰器：在执行被装饰函数前等待一段时间
    :param duration: 需要等待的秒数
    '''

    def decorator(_func):
        def wrapper(*args, **kwargs):
            print(f'Wait for {duration} second before starting... ')
            time.sleep(duration)
            return _func(*args, **kwargs)
        return wrapper
    # 当func为None时，代表使用方提供了关键字参数，比如@delayed_start(duration=2)，此时返回接收单个函数参数的内层子装饰器decorator
    if func is None:
        return decorator
    else:
        # 当位置参数func不为None时，代表使用方没提供关键字参数，直接用了无括号的@ delayed_start调用方式，此时返回内层包装函数wrapper
        return decorator(func)


# 这样定义装饰器以后，我们可以通过多种方式来使用它：
# 1. 不提供任何参数
@delayed_start
def hello1():
    print('hello1')


# 2. 提供可选的关键字参数
@delayed_start(duration=2)
def hello2():
    print('hello2')


# 3. 提供括号调用，但不提供任何参数
@delayed_start()
def hello3():
    print('hello3')


hello1()
hello2()
hello3()
