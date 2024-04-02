# 递归（recursion）
# 是指函数在执行时依赖调用自身来完成工作，是一种非常有用的编程技巧。
# 在实现一些特定算法时，使用递归的代码更符合人们的思维习惯，有着天然的优势。


# 比如计算斐波那契数列（Fibonacci sequence）函数
from functools import lru_cache
import sys


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# 获取数列的前10位成员
print([fib(i) for i in range(10)])


# 局限：当需要计算的数字很大时，上面的fib(n)函数在执行时会形成一个非常深的嵌套调用栈，当它的深度超过一定限制后，函数就会抛出RecursionError异常
try:
    fib(1000)
except RecursionError as e:
    print(f'error: 递归异常 {e}')


# 最大递归深度限制由Python在语言层面上设置，你可以通过下面的命令查看和修改这个限制
sys.getrecursionlimit()
sys.setrecursionlimit(11)


'''
在编程语言领域，为了避免递归导致调用栈过深，占用过多资源，不少编程语言使用一种被称为尾调用优化（tail call optimization）的技术。
这种技术能将fib()函数里的递归优化成循环，以此避免嵌套层级过深，提升性能。

但Python没有这种技术。因此在使用递归时，你必须对函数的输入数据规模时刻保持警惕，
确保它所触发的递归深度，一定远远低于sys.getrecursionlimit()的最大限制。
'''


# 仅针对上面的fib()函数进行优化：
# 第一个点就是fib()函数会触发太多重复计算，它的算法时间复杂度是O(2^n)。
# 因此，只要用@lru_cache给它加上缓存，就可以极大地提升性能
# 不过，添加@lru_cache也仅仅能提升它的效率，如果输入数字过大，函数执行时还是会超过最大递归深度限制。
@lru_cache
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# 对于任何递归代码来说，一劳永逸的办法是将其改写成循环
# 新函数不会因为输入数字过大而触发递归深度报错，并且它的算法时间复杂度也远比旧函数低，执行效率更高
def fib_loop(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


# Python里的递归因为缺少语言层面的优化，局限性较大。
# 当你想用递归来实现某个算法时，请先琢磨琢磨是否能用循环来改写。如果答案是肯定的，那就改成循环吧

# 但能被简单重写为循环的递归代码毕竟是少数。
# 假如递归确实能带来许多方便，当你决意要使用它时，请务必注意不要超过最大递归深度限制。
