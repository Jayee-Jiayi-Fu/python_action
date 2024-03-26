'''
一个简单的例子
enumerate()是Python的一个内置函数，它接收一个可迭代对象作为参数，
返回一个不断生成(当前下标,当前元素)的新可迭代对象。
enumerate()函数很简单，但它其实代表了一种循环代码优化思路：通过修饰可迭代对象来优化循环。
'''
names = ['foo', 'bar', 'foobar']
for i, name in enumerate(names):
    print(i, name)


'''
使用生成器函数修饰可迭代对象
'''


def derecator_names(names: list):
    for i in range(len(names)):
        yield f'No.{i}', f'name is {names[i]}'


for i, name in derecator_names(names):
    print(i, name)


'''
例子2
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def sum_even_only(numbers):
    '''对numbers中所有偶数求和'''
    sum = 0
    for num in numbers:
        if num % 2 == 0:
            sum += num
    return sum


print('sum_even_only = ', sum_even_only(numbers))


'''
提炼成一个生成器函数，从而简化循环内部代码
生成器函数even_only()，它专门负责偶数过滤工作
'''


def even_only(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num


def sum_even_only_v2(numbers):
    sum = 0
    for num in even_only(numbers):
        sum += num
    return sum


print('sum_even_only_v2 = ', sum_even_only_v2(numbers))

'''
“修饰可迭代对象”是指用生成器（或普通的迭代器）在循环外部包装原本的循环主体，
完成一些原本必须在循环内部执行的工作——比如过滤特定成员、提供额外结果等，以此简化循环代码。

'''
