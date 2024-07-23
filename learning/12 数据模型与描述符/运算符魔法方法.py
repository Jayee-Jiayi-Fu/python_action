class Square:
    """ 正方形
    :param length: 边长
    """
    def __init__(self, length):
        self.length = length

    def __eq__(self, other):
        # 判断两个对象是否相等时，先检验 other 是否同为当前类型
        if isinstance(other, self.__class__):
            return self.length == other.length
        return False

    def __ne__(self, other):
        # “不等”运算的结果一般会直接对“等于”取反
        return not (self == other)

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.length < other.length
        # 如果不支持某种运算，可以返回 NotImplemented
        return NotImplemented

    def __le__(self, other):
        return self.__le__(other) or self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.length > other.length
        return NotImplemented

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)


# 更简单快捷的重载比较描述符的方式：使用 functools 内置模块下的装饰器 @total_ordering
# 只要先实现 __eq__方法，然后在 lt\lq\gt\ge四个方法中随意挑一个实现即可，它会自动补全剩余方法


from functools import total_ordering

@total_ordering
class Square2:
    def __init__(self, length):
        self.length = length

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.length == other.length
        return False

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.length < other.length
        return NotImplemented

x = Square(4)
y = Square(4)
print(x == y)