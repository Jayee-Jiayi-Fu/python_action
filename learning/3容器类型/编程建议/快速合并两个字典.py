# 1. dict.update(d1,d2)
# d1的原始内容被修改
d1 = {'name': 'apple'}
d2 = {'price':10}
print(f'd1.update(d2): {d1.update(d2)}')
print(f'd1: {d1}, d2: {d2}')



# 2. 动态解包(解包过程默认进行浅拷贝操作)
# 使用**解包字典
d1 = {'name': 'apple'}
d2 = {'price':10}
d3 = {**d1, **d2}
print(f'd1: {d1}, d2: {d2}, d3: {d3}')

# 使用*解包任何可迭代对象
print(f'[1,2, *range(3)] : {[1,2, *range(3)]}')
print(f'[*d3] : { [*d3] }' )


# 字典的|运算符(获取字典并集)
# 同名键值，后者覆盖前者，运算顺序不同，会影响最终的合并结果
d1 = {'name':'apple'}
d2 = {'name':'orange', 'price':10}
print(f'd1: {d1}, d2: {d2}')
print(f' d1|d2: {d1 | d2},  d2|d1: {d2|d1}')