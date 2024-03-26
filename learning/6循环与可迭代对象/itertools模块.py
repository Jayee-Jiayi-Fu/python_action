'''
itertools是一个和迭代器有关的标准库模块，其中包含许多用来处理可迭代对象的工具函数
01．使用product()扁平化多层嵌套循环
02. 使用islice()实现循环内隔行处理
03．使用takewhile()替代break语句
04. chain()函数可以扁平化双层嵌套循环
05. 用zip_longest()函数可以同时遍历多个对象
'''

'''
01．使用product()扁平化多层嵌套循环
product()接收多个可迭代对象作为参数，然后根据它们的笛卡儿积不断生成结果
'''
from itertools import islice
from itertools import product
list1 = [1, 2]
list2 = [3, 4]
list3 = [5, 6]
print(list(product(list1, list2, list3)))


def find_twelve(num_list1, num_list2, num_list3):
    """从3 个数字列表中，寻找是否存在和为 12 的3 个数"""
    for num1 in num_list1:
        for num2 in num_list2:
            for num3 in num_list3:
                if num1 + num2 + num3 == 12:
                    return num1, num2, num3


def find_twelve_v2(num_list1, num_list2, num_list3):
    """从3 个数字列表中，寻找是否存在和为 12 的3 个数"""
    for nums in list(product(num_list1, num_list2, num_list3)):
        if sum(nums) == 12:
            return nums


print(find_twelve(list1, list2, list3))
print(find_twelve_v2(list1, list2, list3))


'''
02 使用islice()实现循环内隔行处理
islice(seq, start, end, step)函数和数组切片操作（list[start:stop:step]）接收的参数几乎完全一致。如果需要在循环内部实现隔行处理，只要设置第三个参数step（递进步长）的值为2即可：
'''


def parse_titles(filename):
    """从隔行数据文件中读取 Reddit 主题名称"""
    with open(filename, 'r') as fp:
        for i, line in enumerate(fp):
            # 跳过无意义的--- 分隔符
            if i % 2 == 0:
                yield line.strip()


def parse_titles_v2(filename):
    """从隔行数据文件中读取 Reddit 主题名称"""
    with open(filename, 'r') as fp:
        for line in islice(fp, 0, None, 2):
            yield line.strip()


'''
03．使用takewhile()替代break语句
需要在每次开始执行循环体代码时，决定是否需要提前结束循环

takewhile(predicate, iterable)
会在迭代第二个参数iterable的过程中，不断使用当前值作为参数调用predicate()函数，
并对返回结果进行真值测试，如果为True，则返回当前值并继续迭代，否则立即中断本次迭代。
'''

'''
for user in users:
    # 当第一个不合格的用户出现后，不再进行后面的处理
    if not is_qualified(user):
        break
    # 进行处理……
'''

'''
from itertools import takewhile
for user in takewhile(is_qualified, users):
    # 进行处理……
'''
