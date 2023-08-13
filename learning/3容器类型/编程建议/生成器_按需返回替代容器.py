# Python 2 range()会会一次性返回所有数字，若长度很大，非常耗时
# Python 3，range()不再返回列表，而是返回一个类型为range的惰性计算对象,只有在迭代range对象时，它才会不断生成新的数字

# 生成器
# 生成器（generator）是Python里的一种特殊的数据类型。
# 它是一个不断给调用方“生成”内容的类型。
# 定义一个生成器，需要用到生成器函数与yield关键字
# yield和return的最大不同之处在于:
#       return的返回是一次性的，使用它会直接中断整个函数执行
#       yield可以逐步给调用方生成结果
def generate_even(max_number):
    for i in range(0, max_number):
        if i % 2 == 0:
            yield i

for i in generate_even(10):
    print(f'in for_loop: {i}')


try:
    # 调用next()可以逐步从生成器对象里拿到结果
    iter_ = generate_even(10)
    print(f'next: {next(iter_)}')
    print(f'next: {next(iter_)}')
    print(f'next: {next(iter_)}')
    print(f'next: {next(iter_)}')
    print(f'next: {next(iter_)}')
    print(f'next: {next(iter_)}')
except BaseException as e:
    print(f'e: {e}')

# 生成器是可迭代对象，可以使用list()等函数方便地把它转换为各种其他容器类型
print(f'list: {list(generate_even(10))}')