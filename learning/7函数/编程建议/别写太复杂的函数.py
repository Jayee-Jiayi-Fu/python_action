import bisect

'''
复杂函数的两个判断面：
1. 长度
    如果超过65行，很大概率代表函数已经过于复杂，请考虑将它拆分为多个小而简单的子函数（类）吧
2. 圈复杂度
    “圈复杂度”是由Thomas J. McCabe在1976年提出的用于评估函数复杂度的指标。
    它的值是一个正整数，代表程序内线性独立路径的数量。圈复杂度的值越大，表示程序可能的执行路径就越多，逻辑就越复杂。
    如果某个函数的圈复杂度超过10，就代表它已经太复杂了，代码编写者应该想办法简化。优化写法或者拆分成子函数都是不错的选择。
    通过radon工具计算一个函数的圈复杂度
'''


'''下面函数圈复杂度
> radon cc complex_func.py -s
complex_func.py
    F 1:0 rank - A （5）
'''


def rank(self):
    rating_num = float(self.rating)
    if rating_num >= 8.5:
        return 'S'
    elif rating_num >= 8:
        return 'A'
    elif rating_num >= 7:
        return 'B'
    elif rating_num >= 6:
        return 'C'
    else:
        return 'D'


'''使用bisect模块重构后的rank()函数后，圈复杂度
radon cc complex_func.py -s
complex_func.py
    F 1:0 rank - A （1）
'''


def rank2(self):
    breakpoints = (6, 7, 8, 8.5)
    grades = ('D', 'C', 'B', 'A', 'S')
    index = bisect.bisect(breakpoints, float(self.rating))
    return grades[index]


'''
新函数的圈复杂度从5降至1。1是一个非常理想化的值，
如果一个函数的圈复杂度为1，就代表这个函数只有一条主路径，没有任何其他执行路径，这样的函数通常来说都十分简单、容易维护。
通常会将这种检查配置到开发或部署流程中自动执行
'''
