# 1. 双等号运算符==，它会对比两个值是否一致
x, y, z = 1, 1, 3
print(f'x==y : {x ==y}, x == z : {x == z}')


# 2. 类的 == 结果可操控，修改 __eq__方法
class EqualWithAnything():
    '''与任何对象相等'''

    def __eq__(self, other):
        '''other 是 == 右边的对象'''
        return True


foo = EqualWithAnything()
print(f'foo == False: {foo == False}')
print(f'foo == None: {foo == None}')


# 3. 严格检查某个对象为None
# 在执行x is y时，其实就是在判断id(x)和id(y)的结果是否相等，二者是否是同一个对象。
# （1）==对比两个对象的值是否相等，行为可被__eq__方法重载；
# （2）is判断两个对象是否是内存里的同一个东西，无法被重载。
print(f'foo is None: {foo is None}')
x = None
print(f'x is None: {x is None}')

# 注意：
# 除了None、True和False这三个内置对象以外，其他类型的对象在Python中并不是严格以单例模式存在的。
# 换句话说，即便值一致，它们在内存中仍然是完全不同的两个对象。


# 4. 驻留技术，对不变类型数据有效
# 一种底层优化技术，缓存在内存里的一个数组中，需要时从缓存返回，而不是新建对象
x = 123445
y = 123445
print(f'x = {x}, id(x): {id(x)}, y = {y}, id(y): {id(y)}')
print(f'x is y: {x is y}')


x = 'abcdefg'
y = 'abcdefg'
print(f'x = {x}, id(x): {id(x)}, y = {y}, id(y): {id(y)}')
print(f'x is y: {x is y}')

x = (1, 2, 3)
y = (1, 2, 3)
print(f'x = {x}, id(x): {id(x)}, y = {y}, id(y): {id(y)}')
print(f'x is y: {x is y}')


x = [1, 2, 3]
y = [1, 2, 3]
print(f'x = {x}, id(x): {id(x)}, y = {y}, id(y): {id(y)}')
print(f'x is y: {x is y}')
