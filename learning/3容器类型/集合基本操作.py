# 集合是一种无序的可变容器类型，它最大的特点就是成员不能重复。

# 1. 创建集合
# 集合最重要的两个特征——去重与无序
fruits = {'apple', 'orange', 'apple', 'pineapple'}
print(fruits)

# 初始化一个空集合，只能调用set()方法，因为{}表示的是一个空字典，而不是一个空集合
empty_set = set()
print(type(empty_set))
print(type({}))


# 2. 推导式语法
nums = [1,2,2,4,1]
print({n for n in nums if n < 3})


# 3. 追加新成员
new_set = set(['foo', 'foo', 'bar'])
new_set.add('apple')
print(new_set)


# 4. 不可变的集合frozenset

