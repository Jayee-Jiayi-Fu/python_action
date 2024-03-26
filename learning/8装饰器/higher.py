# 返回函数
# ===========
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n

        return ax
    return sum


f = lazy_sum(1, 3, 5, 7, 9)
# print(f())


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


f1, f2, f3 = count()
# print(f1(),f2(),f3())


def inc():
    x = 0

    def fn():
        nonlocal x
        x = x + 1
        return x
    return fn


f4 = inc()
# print(f4())
# print(f4())

# 匿名函数
# ==========
l1 = list(map(lambda x: x*x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(l1)


# 装饰器
# ========
# 定义装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
# 使用装饰器


@log
def now():
    print('2022/1/23')


now()
print(now.__name__)


def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log2('execute')
def now2():
    print('2022/1/24')


now2()
print(now2.__name__)
