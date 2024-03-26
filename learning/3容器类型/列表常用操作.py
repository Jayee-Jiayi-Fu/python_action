# 1. 创建列表
# 1.1 创建列表字面量
numbers = [1, 2, 3]

# 1.2 内置函数list(iterable)则可以把任何一个可迭代对象转换为列表
list('foo')

# 1.3 索引访问
numbers[2]

# 1.4切片获取一段内容
numbers[1:]

# 1.5 删除列表中一段内容
del numbers[1:]

# 2. 遍历列表时获取下标
# enumerate()适用于任何“可迭代对象”，包括元组、字典、字符串等
# start参数，用于指定循环下标的初始值（默认为0）
names = ['foo', 'bar', 'too', 'sooo', 'pee']
for index, s in enumerate(names, start=10):
    print(index, s)

# 3. 列表推导式
# 剔除列表中的奇数，并将所有数字乘以100。
numbers = [3, 5, 77, 22, 45, 22, 6, 81, 14]
print([n * 100 for n in numbers if n % 2 == 0])


# 4. 列表的可变性
# Python里的内置数据类型，大致上可分为可变与不可变两种。
# · 可变（mutable）：列表、字典、集合。
# · 不可变（immutable）：整数、浮点数、字符串、字节串、元组。
# Python在进行函数调用传参时，采用的既不是值传递，也不是引用传递，而是传递了“变量所指对象的引用”
# 一切行为取决于对象的可变性

# 为字符串追加内容
def add_str(in_func_obj):
    print(f'In add [before]: in_func_obj="{in_func_obj}"')
    in_func_obj += ' suffix'
    print(f'In add [after]: in_func_obj="{in_func_obj}"')


orig_obj = 'foo'
print(f'Outside [before]: orig_obj="{orig_obj}"')
add_str(orig_obj)
print(f'Outside [after]: orig_obj="{orig_obj}"')


# 为列表追加内容
def add_list(in_func_obj):
    print(f'In add [before]: in_func_obj="{in_func_obj}"')
    in_func_obj += ['suffix']
    print(f'In add [after]: in_func_obj="{in_func_obj}"')


orig_obj = ['foo', 'baf']
print(f'Outside [before]: orig_obj="{orig_obj}"')
add_list(orig_obj)
print(f'Outside [after]: orig_obj="{orig_obj}"')

# 5. 不要在遍历列表是时修改
# 要修改列表，请不要在遍历时直接修改。只需选择启用一个新列表来保存修改后的成员


def remove_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            numbers.remove(n)
    return numbers


numbers = [1, 2, 4, 8, 11]
print(f'remove_even(numbers): {remove_even(numbers)}')
