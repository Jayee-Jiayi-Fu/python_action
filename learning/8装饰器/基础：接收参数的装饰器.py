import time
import random


'''
❶先进行一次调用，传入装饰器参数，获得第一层内嵌函数decorator
❷进行第二次调用，获取第二层内嵌函数wrapper
'''


def timer(print_args=False):
    '''装饰器：打印函数耗时

    :param print_args: 是否打印方法名和参数，默认为False
    '''
    def decorator(func):
        def wrapper(*args, **kwargs):
            st = time.perf_counter()
            ret = func(*args, **kwargs)

            if print_args:
                print(f'"{func.__name__}", args: {args}, kwargs: {kwargs}')
            print('time cost: {} seconds'.format(time.perf_counter() - st))

            return ret
        return wrapper
    return decorator


@timer(print_args=True)
def random_sleep():
    '''当其他函数应用了timer装饰器后，包装函数decorated会作为装饰器的返回值，完全替换被装饰的原始函数func。'''
    time.sleep(random.random())


random_sleep()
