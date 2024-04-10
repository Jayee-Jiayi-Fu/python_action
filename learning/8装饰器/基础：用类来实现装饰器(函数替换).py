import time
from functools import wraps

# 某个对象是否能通过装饰器（@decorator）的形式使用只有一条判断标准，那就是decorator是不是一个可调用的对象
# 函数自然是可调用对象，除此之外，类同样也是可调用对象
# 如果一个类实现了__call__魔法方法，那么它的实例也会变成可调用对象
# 使用callable()内置函数可以判断某个对象是否可调用


class Foo:
    # ❶__call__魔法方法是用来实现可调用对象的关键方法
    def __call__(self, name):
        print(f'Hello, {name}')


# ❷调用类实例时，可以像调用普通函数一样提供额外参数
foo = Foo()
print(f'foo is callable: {callable(foo)}, foo("foo"):')
foo('foo')


# 如果按装饰器用于替换原函数的对象类型来分类，
# 类实现的装饰器可分为两种，一种是“函数替换”，另一种是“实例替换”。

# 函数替换装饰器
# 虽然是基于类实现的，但用来替换原函数的对象仍然是个普通的包装函数。这种技术最适合用来实现接收参数的装饰器。
class timer:
    '''装饰器：打印函数耗时

    :param print_args:是否打印方法名和参数，默认 False
    '''

    def __init__(self, print_args):
        self.print_args = print_args  # 通过类实现的装饰器，把原本的两次函数调用替换成了类和类实例的调用。

    def __call__(self, func):

        @wraps(func)
        def decorated(*args, **kwargs):

            st = time.perf_counter()
            ret = func(*args, **kwargs)

            if self.print_args:
                print(f'"{ func.__name__}", args: {args}, kwargs: {kwargs}')

            print('time cost: {}'.format(time.perf_counter() - st))

            return ret

        # 虽然装饰器是用类实现的，但最终用来替换原函数的对象，仍然是一个处在__call__方法里的闭包函数decorated。
        return decorated


# 虽然“函数替换”装饰器的代码更简单，但它和普通装饰器并没有本质区别
