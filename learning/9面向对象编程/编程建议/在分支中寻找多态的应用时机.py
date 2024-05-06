'''
多态（polymorphism）是面向对象编程的基本概念之一。
它表示同一个方法调用，在运行时会因为对象类型的不同，产生不同效果。
比如animal.bark()这段代码，在animal是Cat类型时会发出“喵喵”叫，在animal是Dog类型时则发出“汪汪”叫。
'''

import OutputType


class FancyLogger:
    """日志类：支持向文件、Redis、ES 等服务输出日志"""

    _redis_max_length = 1024

    def __init__(self, output_type=OutputType.FILE):
        self.output_type = output_type
        ...

    def log(self, message):
        """打印日志"""
        if self.output_type == OutputType.FILE:
            ...
        elif self.output_type == OutputType.REDIS:
            ...
        elif self.output_type == OutputType.ES:
            ...
        else:
            raise TypeError('output type invalid')

    def pre_process(self, message):
        """预处理日志"""
        # Redis 对日志最大长度有限制，需要进行裁剪
        if self.output_type == OutputType.REDIS:
            return message[: self._redis_max_length]


'''
上面这段代码就是一个典型的应该使用多态的例子。
FancyLogger类在日志输出类型不同时，需要有不同的行为。
因此，我们完全可以为“输出日志”行为建模一个新的类型：LogWriter，然后把每个类型的不同逻辑封装到各自的Writer类中。
对于现有的三种类型，我们可以创建下面的Writer类：
'''


class FileWriter:
    def write(self, message):
        ...


class RedisWriter:
    max_length = 1024

    def write(self, message):
        message = self._pre_process(message)
        ...

    def _pre_process(self, message):
        # Redis 对日志最大长度有限制，需要进行裁剪
        return message[: self.max_length]


class EsWriter:

    def write(self, message):
        ...

# 注意：这些Writer类都没有继承任何基类，因为在Python中多态并不需要使用继承。如果你觉得这样不好，也可以选择创建一个LogWriter抽象基类
# 基于这些不同的Writer类，FancyLogger可以简化成下面这样：


class FancyLogger:
    """日志类：支持向文件、Redis、ES 等服务输出日志"""

    def __init__(self, output_writer=None):
        self._writer = output_writer or FileWriter()
        ...

    def log(self, message):
        self._writer.write(message)


'''
新代码利用多态特性，完全消除了原来的条件判断语句。另外你会发现，新代码的扩展性也远比旧代码好。     
多态思想驱使我们更积极地寻找有效的抽象，以此隔离各个模块，让它们之间通过规范的接口来通信。模块因此变得更容易扩展，代码也变得更好理解了。
'''
