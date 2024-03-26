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
nums = [1, 2, 2, 4, 1]
print({n for n in nums if n < 3})


# 3. 追加新成员
new_set = set(['foo', 'foo', 'bar'])
new_set.add('apple')
print(new_set)


# 4. 不可变的集合frozenset
# 它和普通set非常像，只是少了所有的修改类方法
f_set = frozenset(['foo', 'foo', 'bar'])
try:
    f_set.add('a')
except Exception as e:
    print(f'f_set.add() 方法报错： {e}')


# 5. 集合运算：交集、并集、差集
# 所有操作都可以用两种方式来进行：方法和运算符
fruits_1 = {'apple', 'orange', 'pineapple'}
fruits_2 = {'tomato', 'orange', 'grapes', 'mango'}
print(f'交集：{fruits_1 & fruits_2}')
print(f'并集：{fruits_1 | fruits_2}')
print(f'差集（前一个集合有、后一个集合没有的东西）：{fruits_1 - fruits_2}')


# 6. 集合只能存放可哈希对象
valid_seet = {'apple', 20, ('foo')}
try:
    invalid_set = {'foo', [1, 2, 3]}
except Exception as e:
    print(f'无效集合：{e}')

# 6.1 对象的可哈希性
# 把某个对象放进集合或者作为字典的键使用时，解释器都需要对该对象进行一次哈希运算
# 调用内置函数 hash(obj)  计算哈希值，如果对象可哈希就返回一个整型结果，否则返回TypeError错误

# 不可变的内置类型都是可哈希的
# 比如str、int、tuple、frozenset等
# 对于不可变容器类型(tuple, frozenset)，仅当它的所有成员都不可变时，它自身才是可哈希的；
print(hash('string'))
print(hash(100))
print(hash((1, 2, 3)))

# 由用户定义的所有对象默认都是可哈希的


class Foo:
    pass


print(f'用户定义对象：{hash(Foo())}')

# 可变的内置类型都无法正常计算哈希值
# 比如str、int、tuple、frozenset等
# 有一定的“传染性”。比如在一个原本可哈希的元组里放入可变的列表对象后，它也会马上变得不可哈希
try:
    hash({'key': 'value'})
except TypeError as e:
    print(f'不可哈希：{e}')
try:
    hash([1, 2, 3])
except TypeError as e:
    print(f'不可哈希：{e}')
try:
    hash((1, 2, 3, ['foo']))
except TypeError as e:
    print(f'不可哈希：{e}')
