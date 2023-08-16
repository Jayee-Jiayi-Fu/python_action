# with关键字
# 在代码中开辟一段由它管理的上下文，并控制程序在进入和退出这段上下文时的行为。


# 文件操作时，with上下文所附加的主要行为就是：进入时打开某个文件并返回文件对象，退出时关闭该文件对象。
import random

try:
    with open('foo.txt') as fp:
        content = fp.read()
except FileNotFoundError:
    pass


# 并非所有对象都能像open('foo.txt')一样配合with使用，只有满足上下文管理器（context manager）协议的对象才行
# 实现一个简单的上下文管理器
class DummyContext:
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        # __enter__会在进入管理器时被调用，同事可以返回结果
        # 这个结果可以通过 as 关键字被调用方获取
        print('calling __enter__()...')
        return f'{self.name}-{random.random()}'
    def __exit__(self, exc_type, exc_val, exc_tb):
        # __exit__ 会在退出管理器时被调用
        print('calling __exit__()...')
        return False

with DummyContext('foo') as name:
    print(f'Name: {name}')


# 作用1：替代finally语句清理资源
# 编写try语句时，finally关键字经常用来做一些资源清理类工作
# 如果使用上下文管理器，这类资源回收代码可以变得更简单，只要在__exit__里增加需要的回收语句
class create_conn_obj:
    '''创建链接对象，并在退出上下文时自动关闭'''
    def __init__(self, host, port, timeout=None):
        self.conn = create_conn(host, port, timeout =timeout)
    def __enter__(self):
        return self.conn
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        return False
# 使用,会自动关闭的连接对象
with create_conn_obj(host, port, timeout=None) as conn:
    try:
        conn.send_text('Hello world!')
    except Exception as e:
        print(f'Unable to use connection: {e}')



# 作用2: 用于忽略异常
# __exit__接收三个参数：exc_type、exc_value和traceback。
# 在代码执行时，假如with管辖的上下文内没有抛出任何异常，那么当解释器触发__exit__方法时，上面的三个参数值都是None；
# 但如果有异常抛出，这三个参数就会变成该异常的具体内容:
#       （1） exc_type：异常的类型。
#       （2） exc_value：异常对象。
#       （3） traceback：错误的堆栈对象。
# 程序的行为取决于__exit__方法的返回值：
#       如果__exit__返回了True，那么这个异常就会被当前的with语句压制住，不再继续抛出，达到“忽略异常”的效果；
#       如果__exit__返回了False，那这个异常就会被正常抛出，交由调用方处理。
# 如果在真实项目中要忽略某类异常，可以直接使用标准库模块contextlib里的suppress函数，它提供了现成的“忽略异常”功能。
class ignore_closed:
   '''忽略已关闭的连接'''
   def __enter__(self):
       pass
   def __exit__(self, exc_type, exc_val, exc_tb):
       if exc_type == AlreadyClosedError:
           return True
       return False
# 当你想忽略AlreadyClosedError异常时
with ignore_closed():
    close_conn(conn)



# 3. 使用contextmanager装饰器（日常工作更推荐）
# 位于内置模块contextlib下，它可以把任何一个「生成器函数」直接转换为一个上下文管理器。
# 以yield关键字为界，yield前的逻辑会在进入管理器时执行（类似于__enter__），yield后的逻辑会在退出管理器时执行（类似于__exit__）
# 如果要在上下文管理器内处理异常，必须用try语句块包裹yield语句
from contextlib import contextmanager

@contextmanager
def create_conn_obj(hot, port, timeout=None):
    '''创建连接对象，并在退出上下文时自动关闭'''
    conn = create_conn(host, port, timeout=None)
    try:
        yield conn
    finally:
        conn.close()