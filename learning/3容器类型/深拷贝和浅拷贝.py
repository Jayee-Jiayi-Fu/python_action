import copy

# 想让两个变量的修改操作互不影响，就需要拷贝变量所指向的可变对象

# 1. 浅拷贝
# 1.1 最通用，使用copy模块下的copy()方法
nums = [1, 2, 3, 4]
nums_copy = copy.copy(nums)
nums[2] = 30
print(f'nums: {nums}')
print(f'nums_copy: {nums_copy}')

# 1.2 持推导式的类型，用推导式也可以产生一个浅拷贝对象
d = {'foo': 1}
d2 = {key: value for key, value in d.items()}
d['foo'] = 2
print(f'd: {d}')
print(f'd2: {d2}')

# 1.3 使用各容器类型的内置构造函数
d3 = dict(d.items())
nums_copy2 = list(nums)

# 1.4 支持切片操作的容器类型——比如列表、元组，对其进行全切片
nums_copy3 = nums[:]

# 1..5 有些类型自身就提供了浅拷贝方法
nums_copy4 = nums.copy()
d4 = d.copy()


# 2. 深拷贝
# 对于一些层层嵌套的复杂数据来说，浅拷贝仍然无法解决嵌套对象被修改的问题
items = [1, ['foo', 'bar'], 2, 3]
items_copy = copy.copy(items)
items_copy[1].append('kim')
print(f'items: {items} \nitems_copy:{ items_copy}')

# 用copy.deepcopy()函数来进行深拷贝
# 深拷贝会遍历并拷贝items里的所有内容——包括它所嵌套的子列表
items_deep = copy.deepcopy(items)
items_deep[1].append('Joke')
print(f'items: {items} \nitems_deep:{ items_deep}')
