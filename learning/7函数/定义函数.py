
# 1. 定义与调用函数
def add(x, y):
    return x + y


result = add(3, 4)
print(f'3 + 4 = {result}')


# 2. lambda 定义匿名函数
def add(x, y):
    return x


result = add(4, 3)
print(f'4 + 3 = {result}')


# 3. 直接调用内部函数
abs(100)
n1 = 255
n2 = 1000
print(hex(n1), hex(n2))

# print('-------------------')

# 定义函数
# def my_abs(x):
#     if not isinstance(x,(int,float)):


#         raise TypeError('bad operated type')
#     if x >= 0 :
#         return x
#     else:
#         return -x
# print(my_abs('A'))


# 返回多个值
# def move(x,y,step):
#     nx = x + step * 2
#     ny = y - step * 3
#     return nx, ny
# r = move(2,3,4)
# x,y = r
# print(r,x,y)


# 递归函数
# def fat(n):
#     if n == 1:
#         return n
#     return fat(n-1)*n
# print(fat(1),fat(5))

# 递归函数，尾递归优化
def fat(n):
    return fat_iter(n, 1)


def fat_iter(num, product):
    if num == 1:
        return product

    else:
        return fat_iter(num-1, num*product)


print(fat(1), fat(5))
