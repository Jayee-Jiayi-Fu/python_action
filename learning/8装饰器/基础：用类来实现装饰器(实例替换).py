# “实例替换”装饰器
# 用类来实现装饰器时，被装饰的函数func会作为唯一的初始化参数传递到类的实例化方法__init__中。
# 同时，类的实例化结果——类实例（class instance），会作为包装对象替换原始函数。
# 通过组合不同的工具，它既能实现无参数装饰器，也能实现有参数装饰器。

import time
from functools import update_wrapper, partial

# 01．实现无参数装饰器


class DelayStart:

    def __init__(self, func):
        # ❶update_wrapper与前面的wraps一样，都是把被包装函数的元数据更新到包装者（在这里是DelayedStart实例）上
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        # ❷通过实现__call__方法，让DelayedStart的实例变得可调用，以此模拟函数的调用行为
        print(f'Wait for 1 second before starting...')
        time.sleep(1)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        # ❸为装饰器类定义额外方法，提供更多样化的接口
        print('Call without delay...')
        return self.func(*args, **kwargs)


@DelayStart
def hello():
    print('Hello world!')


print(hello)
print(hello.__name__)
print(hello())
print(hello.eager_call())
print('-------------------------------')


# 02．实现有参数装饰器
class DelayStart2:

    def __init__(self, func, *, duration=1):
        # ❶把func参数以外的其他参数都定义为“仅限关键字参数”，从而更好地区分原始函数与装饰器的其他参数
        update_wrapper(self, func)
        self.func = func
        self.duration = duration

    def __call__(self, *args, **kwargs):
        print(f'Wait for {self.duration} second before starting...')
        time.sleep(self.duration)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        print('Call without delay...')
        return self.func(*args, **kwargs)


def delayed_start(**kwargs):
    '''装饰器： 推迟某给函数的执行'''

    print(f'delayed_start **kwargs: {kwargs}')
    # ❷通过partial构建一个新的可调用对象，这个对象接收的唯一参数是待装饰函数func，因此可以用作装饰器
    return partial(DelayStart2, **kwargs)


@delayed_start(duration=2)
def hello2(name):
    print(f'Hello {name}!')
    return 'done'


print(hello2)
print(hello2.__name__)
print(hello2('Jack'))
print(hello2.eager_call('Nick'))
print('-------------------------------')
