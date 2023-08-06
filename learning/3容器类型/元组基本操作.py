from collections import namedtuple

# 元组是一种有序的不可变容器类型

# 1. 定义元组
# 1.1 使用字面量语法
# 真相：“括号”不是定义元组的关键标志，“逗号”才是
t1 = (0, 1, 2)
t2 = 0, 1, 2
print(t1, t2, t1 == t2)

# 1.2 tuple(iterable)内置函数
t3 = tuple('foo')
print(t3)

# 2. 返回多个结果，其实就是返回元组
# 将函数返回值一次赋值给多个变量时，其实就是对元组做了一次解包操作
def get_rectangle():
    width = 100
    height = 20
    return width, height
result = get_rectangle()
w,h = get_rectangle()
print(result, type(result), w, h)


# 3. 没有“元组推导式”
# 括号得到的是一个生成器对象，但是属于可迭代对象，可以调佣tuple函数获得元组
results = (n* 100 for n in range(10) if n % 2 ==0)
t4 = tuple(results)
print(results, type(results), t4, type(t4))


# 4. 存放结构化数据
# 和列表不同，在同一个元组里出现不同类型的值是很常见的事情
user_info = ('piglei', 'MALE', 30, True)


# 5. 特殊的元组类型：具名元组
# 在保留普通元组功能的基础上，允许为元组的每个成员命名
# 这样你便能通过名称而不止是数字索引访问成员
# 和普通元组一样，具名元组是不可变的

# 5.1 namedtuple()函数定义
# 下面三种方式等价
Rectangle1 = namedtuple('Rectangle', 'width,height')
Rectangle2 = namedtuple('Rectangle', 'width height')
Rectangle3 = namedtuple('Rectangle', ['width','height'])
rect1 = Rectangle1(100,20)
rect2 = Rectangle2(width=200, height=30)
print(rect1, rect1[0], rect1.width)
print(rect2)

# 5.2 typing.NameTuple 和类型注解语法定义具名元组类型
# 可读性更佳
# 注意：虽然给width和height加了类型注解，但Python在执行时并不会做真正的类型校验
class Rectangle(NameTuple):
    width: int
    height: int

rect = Rectangle(100,200)

