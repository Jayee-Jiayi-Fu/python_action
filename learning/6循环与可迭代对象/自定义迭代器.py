'''
自定义迭代器
编写一个和range()类似的迭代器对象Range7，它可以返回某个范围内所有可被7整除或包含7的整数。
'''


class Range7:
    """生成某个范围内可被 7 整除或包含 7 的整数
    :param start: 开始数字
    :param end: 结束数字
    """

    def __init__(self, start, end):
        self.start = start
        self.end = end
        # 使用current 保存当前所处的位置
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            # 当已经到达边界时，抛出异常终止迭代
            if self.current >= self.end:
                raise StopIteration
            if self.num_is_valid(self.current):
                ret = self.current
                self.current += 1
                return ret
            self.current += 1

    def num_is_valid(self, num):
        """判断数字是否满足要求"""
        if num == 0:
            return False
        return num % 7 == 0 or '7' in str(num)


r = Range7(0, 20)
print('执行第一次', tuple(r))
# 第二次用tuple()转换成元组，只能得到一个空元组，因为每个Range7对象都只有唯一的current属性
print('执行第二次', tuple(r))

'''
重要：区分「迭代器」和「可迭代对象」
「迭代器」是可迭代对象的一种。
    - 它最常出现的场景是在迭代其他对象时，作为一种介质或工具对象存在
    - 就像调用iter([])时返回的list_iterator。
    - 每个迭代器都对应一次完整的迭代过程，因此它自身必须保存与当前迭代相关的状态——迭代位置（就像Range7里面的current属性）。

「可迭代对象」的定义则宽泛许多。
    - 判断一个对象obj是否可迭代的唯一标准，就是调用iter(obj)，然后看结果是不是一个迭代器。
    - 因此，可迭代对象只需要实现__iter__方法，不一定得实现__next__方法。
'''


# 如果想让Range7对象在每次迭代时都返回完整结果，我们必须把现在的代码拆成两部分：可迭代类型Range7和迭代器类型Range7Iterator
class Range77:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return Range77Iteror(self)


class Range77Iteror:
    def __init__(self, range_obj: Range77):
        self.range_obj = range_obj
        self.current = range_obj.start

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.current >= self.range_obj.end:
                raise StopIteration
            if self.num_is_valid(self.current):
                ret = self.current
                self.current += 1
                return ret
            self.current += 1

    def num_is_valid(self, num):
        if num == 0:
            return False
        return num % 7 == 0 or '7' in str(num)


r = Range77(0, 20)
print('Range77 执行第一次', tuple(r))
print('Range77 执行第二次', tuple(r))

'''
最后，总结一下迭代器与可迭代对象的区别：
· 可迭代对象不一定是迭代器，但迭代器一定是可迭代对象；
· 对可迭代对象使用iter()会返回迭代器，迭代器则会返回其自身；
· 每个迭代器的被迭代过程是一次性的，可迭代对象则不一定；
· 可迭代对象只需要实现__iter__方法，而迭代器要额外实现__next__方法。
'''


'''
可迭代对象与__getitem__
除了__iter__和__next__方法外，还有一个魔法方法也和可迭代对象密切相关：__getitem__。
如果一个类型没有定义__iter__，但是定义了__getitem__方法，那么Python也会认为它是可迭代的。
在遍历它时，解释器会不断使用数字索引值(0, 1, 2, …)来调用__getitem__方法获得返回值，直到抛出IndexError为止。
但__getitem__可遍历的这个特点不属于目前主流的迭代器协议，更多是对旧版本的一种兼容行为，所以本章不做过多阐述。
'''
