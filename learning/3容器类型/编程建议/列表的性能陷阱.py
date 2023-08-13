# 性能陷阱1：
# .append()往尾部追加
# .insert()在任意位置插入
# 各种常见数据结构似乎都可以用列表来实现，比如先进先出的队列、先进后出的堆栈
# 虽然列表支持各种操作，但其中某些操作可能没你想得那么快

def list_append():
    l = []
    for i in range(5000):
        l.append(i)

def list_insert():
    l = []
    for i in range(5000):
        l.insert(0, i)


import timeit

# 默认执行一万次
# insert耗时明显更多，因为Python在实现列表时，底层使用了数组（array）数据结构
# 尾部追加的时间复杂度为O（1）
# 中间插入的平均时间复杂度是O(n)
append_spent = timeit.timeit(setup= 'from __main__ import list_append',
                             stmt = 'list_append()',
                             number=1000)
insert_spent = timeit.timeit(setup= 'from __main__ import list_insert',
                             stmt = 'list_insert()',
                             number=1000)
print(f'append_spent = {append_spent}') # 3.0439501919972827
print(f'insert_spent = {insert_spent}') # 43.12222222299897


# collections.deque类型来替代列表
# deque底层使用了双端队列，无论在头部还是尾部追加成员，时间复杂度都是O（1）
from collections import deque
def list_append():
    l = deque()
    for i in range(5000):
        l.append(i)

def list_insert():
    l = deque()
    for i in range(5000):
        l.insert(0, i)

append_spent = timeit.timeit(setup= 'from __main__ import list_append',
                             stmt = 'list_append()',
                             number=1000)
insert_spent = timeit.timeit(setup= 'from __main__ import list_insert',
                             stmt = 'list_insert()',
                             number=1000)
print(f'append_spent = {append_spent}') # 0.3133413780014962
print(f'insert_spent = {insert_spent}') # 0.5124621610011673



# 性能陷阱2：判断“成员是否存在”（进行in判断）的耗时问题
# 因为列表在底层使用了数组结构，所以要判断某个成员是否存在，唯一的办法是从前往后遍历所有成员，执行该操作的时间复杂度是O(n)
# 建议：把目标容器转换成集合类型，作为查找时的索引使用，因为其底层使用了哈希表数据结构，时间复杂度是O(1)
VALID_NAMES = ['piglei', 'raymond', ' bojack', 'caroline']
VALID_NAME_SET = set(VALID_NAMES)
def validate_name(name):
    if name not in VALID_NAME_SET:
        raise ValueError(f'{name} is not a valid name!')



