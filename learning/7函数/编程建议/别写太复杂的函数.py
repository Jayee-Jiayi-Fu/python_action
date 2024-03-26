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
