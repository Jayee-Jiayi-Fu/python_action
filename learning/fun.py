# 调用函数
# abs(100)
# n1 = 255
# n2 = 1000
# print(hex(n1),hex(n2))

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

# 函数参数
# def power(x,n = 2):
#     r = 1
#     while n > 0:
#         r =  x * r
#         n = n - 1
#     return r
# print(power(5,1),power(5),power(5,3))


# 参数陷阱
# def fun_trap( L=[]):
#     L.append('END')
#     return L
# print(fun_trap())
# print(fun_trap())

# def fun_trap1( L = None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
# print(fun_trap1())
# print(fun_trap1())

# def fun_trap( L=''):
#     L = L + 'str'
#     return L
# print(fun_trap())
# print(fun_trap())

# 可变参数
# def calc(numbers):
#     sum = 0
#     for x in numbers:
#         sum = sum + x * x
#     return sum
# print(calc([1,2,3,4,5]))
# print(calc((1,2,3,4,5)))


# def calc(*numbers):
#     sum = 0
#     for x in numbers:
#         sum = sum + x * x
#     return sum
# print(calc(1,2,3,4,5))
# print(calc())


# 关键字参数
# def person(name,age,**kw):
#     print('name=',name,'age=',age,'other:',kw)
# person('Jayee',28,city = 'ShenZhen',Country='China')
# info = {'city':'GuangZhou','counter':'China'}
# person('Shally',23,**info)


# 命名关键字参数
# def person(name,age,*,city,job):
#     print(name,age,city,job)

# person('Jack',23,city='Beijing',job='Engineer')

# def person2(name,*ages,city):
#     print(name,city)
# person2('Jack',city='Shanghai')



# 递归函数
# def fat(n):
#     if n == 1:
#         return n
#     return fat(n-1)*n
# print(fat(1),fat(5))

# 递归函数，尾递归优化
def fat(n):
    return fat_iter(n,1)
def fat_iter(num,product):
    if num == 1:
        return product
    else:
        return fat_iter(num-1,num*product)
print(fat(1),fat(5))
