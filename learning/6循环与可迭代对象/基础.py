# Python中有两种循环方式，for 和 while

'''
for 循环
for <item> in <iterable>，配合一个可迭代对象iterable使用
'''
platforms = ['taobao', 'pdd', 'doudian', 'kuaishou']
for item in platforms:
    print(item)

print('---------------------')

'''
while 循环
while <expression>，expression表达式是循环的成立条件，为假时退出循环
'''
platforms = ['taobao', 'pdd', 'doudian', 'kuaishou']
i = 0
while i < len(platforms):
    print(platforms[i])
    i += 1

# 对于一些常见的循环任务，使用for比while要方便得多。因此在 日常编码中，for的出场频率也远比while要高得多。
