'''
在Python中实践函数式编程，最常用的几个工具:
（1）map(func, iterable)：遍历并执行func获取结果，迭代返回新结果。
（2）filter(func, iterable)：遍历并使用func测试成员，仅当结果为真时返回。
（3） lambda：定义一个一次性使用的匿名函数。
'''


users = []


def query_points(user):
    pass


# 假如你想获取所有处于活跃状态的用户积分
# 使用工具函数写法：
points = list(map(query_points, filter(lambda user: user.is_active(), users)))


# 使用列表推导式写法：
points = [query_points(user) for user in users if user.is_active]

# 相比函数式编程，使用列表推导式的代码通常更短，而且描述性更强
