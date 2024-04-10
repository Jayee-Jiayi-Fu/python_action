import wrapt
import random


def provide_number(min_num, max_num):
    """
    装饰器：随机生成一个在[min_num, max_num] 范围内的整数，
    并将其追加为函数的第一个位置参数
    """

    def wrapper(func):
        def decorated(*args, **kwargs):
            num = random.randint(min_num, max_num)
            # 将 num 追加为第一个参数，然后调用函数
            return func(num, *args, **kwargs)

        return decorated

    return wrapper


@provide_number(1, 100)
def print_random_number(num):
    print(num)


print_random_number()
print('-----------------------------')


# @provide_number装饰器的功能看上去很不错，但当我用它来修饰类方法时，就会碰上“麻烦事”：
class Foo:
    @provide_number(1, 100)
    def print_random_number(self, num):
        print(num)


Foo().print_random_number()  # 输出了类实例self对象。
# 因为类方法第一个位置参数总是当前绑定的类实例self对象


# provide_number装饰器在追加位置参数时，必须聪明地判断当前被修饰的对象是普通函数还是类方法。
# 假如被修饰的对象是类方法，那就得跳过藏在*args里的类实例变量，才能正确将num作为第一个参数注入。
# wrapt是一个第三方装饰器工具库，利用它，我们可以非常方便地改造provide_number装饰器，完美地解决这个问题。


# 基于wrapt模块实现的provide_number装饰器
def provide_number(min_num, max_num):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        # 参数含义：
        #
        # - wrapped：被装饰的函数或类方法
        # - instance：
        # - 如果被装饰者为普通类方法，则该值为类实例
        # - 如果被装饰者为 classmethod 类方法，则该值为类
        # - 如果被装饰者为类/函数/静态方法，则该值为 None
        #
        # - args：调用时的位置参数（注意没有 * 符号）
        # - kwargs：调用时的关键字参数（注意没有 ** 符号）
        #
        num = random.randint(min_num, max_num)
        # 无须关注 wrapped 是类方法还是普通函数，直接在头部追加参数
        args = (num,) + args
        return wrapped(*args, **kwargs)

    return wrapper


@provide_number(1, 100)
def print_random_number(num):
    print(num)


print_random_number()


class Foo:
    @provide_number(1, 100)
    def print_random_number(self, num):
        print(num)


Foo().print_random_number()


'''使用wrapt模块编写的装饰器，除了解决了类方法兼容问题以外，代码嵌套层级也比普通装饰器少，变得更扁平、更易读。如果你有兴趣，可以参阅wrapt模块的官方文档了解更多信息。'''
