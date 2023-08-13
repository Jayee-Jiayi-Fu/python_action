# 集合去重有一个很大的缺点：得到的结果会丢失集合内成员原有的顺序（使用的哈希表结构）
nums = [10,2,3,21,10,3]
print(f'nums: {nums}')
print(f'去重但是丢失了顺序， set(nums): { set(nums) }')



'''有序字典OrderedDict
OrderedDict同时满足两个条件：
    （1）它的键是有序的；
    （2）它的键绝对不会重复。
因此，只要根据列表构建一个字典，字典的所有键就是有序去重的结果：
'''
from collections import OrderedDict
nums = [10,2,3,21,10,3]
ordered_nums = OrderedDict.fromkeys(nums).keys()
print(f'nums: {nums}')
print(f'OrderedDict 顺序不变，ordered_nums: { ordered_nums }')


