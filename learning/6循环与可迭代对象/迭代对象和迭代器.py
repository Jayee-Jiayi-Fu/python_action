'''
目标：弄明白"迭代"是怎么回事
两个重要的内置函数：iter()和next()
'''


'''
1. iter(), 调用iter()会尝试返回一个迭代器对象
- 列表类型的迭代器对象——list_iterator
- 字符串类型的迭代器对象——str_iterator
- 对不可迭代的类型执行iter()会抛出TypeError异常
'''
print(iter([1, 2, 3]))  # <list_iterator object at 0x10db681c0>
print(iter('str'))  # <str_iterator object at 0x1071181c0>
# print( iter(1))        #TypeError: 'int' object is not iterable


'''
迭代器（iterator）一种帮助迭代其他对象的对象。
迭代器最鲜明的特征是：不断对它执行next()函数会返回下一次迭代结果。
当迭代器没有更多值可以返回时，便会抛出StopIteration异常
'''
l = [33, 55, 6]
iter_l = iter(l)
print(next(iter_l))  # 33
print(next(iter_l))  # 55
print(next(iter_l))  # 6
# print(next(iter_l)) # StopIteration


'''
迭代器还有一个重要的特点：对迭代器执行iter()函数，尝试获取迭代器的迭代器对象时，返回的结果一定是迭代器本身
'''
print('iter(iter_l) is iter_l ==>', iter(iter_l) is iter_l)


''''
使用for循环遍历某个可迭代对象时，其实是先调用了iter()拿到它的迭代器，然后不断地用next()从迭代器中获取值
'''
names = ['foo', 'bar', 'foobar']
for name in names:
    print(name)


# 等同于
iter_names = iter(names)
while True:
    try:
        name = next(iter_names)
        print(name)
    except StopIteration:
        break
