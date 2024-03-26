# bisect是Python内置的二分算法模块
# 它有一个同名函数bisect，可以用来在有序列表里做二分查找：
import bisect


# 明确的有序分界点
# 注意：用来做二分查找的容器必须是已经排好序的
breakpoints = (6, 7, 8, 8.5)

# bisect 函数会返回值在列表中的位置
print(f'bisect.bisect(breakpoints, 1) : {bisect.bisect(breakpoints, 1)}')
print(f'bisect.bisect(breakpoints, 7.7) : {bisect.bisect(breakpoints, 7.7)}')
print(f'bisect.bisect(breakpoints, 10) : {bisect.bisect(breakpoints, 10)}')
