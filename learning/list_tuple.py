
# # list集合
# list1 = ['Lily','Kimy']
# print(list1,'-',list1[1])

# list1.append('Jim')
# print('append:',list1)

# list1.insert(1,'Ori')
# print('insert:',list1)

# list1.pop()
# print('pop:',list1)

# list1.pop(0)
# print('pop(0):',list1)
# print('---------------------------')

# # tuple 集合
# tuple1 = (1,2,list1)
# print(tuple1)
# print(tuple1[1])

# list1[0] = 'Nico'
# print(tuple1)

# tuple2 = (1)
# tuple3 = (1,)
# print(tuple2,tuple3)


# =========================================
# 高级特性
# =========================================
# L = [1,2]
# print( len(L[:5]) )  

# 生成器
# g = (x * x for x in range(10))

# for n in g:
#     print (n)

# Fibonacci数列
# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         yield(b)
#         a,b = b,a+b
#         n = n +1 
#     return 'done'

# # 拿不到 return 的值
# for n in fib(6):
#     print(n)

# g = fib(6)
# while True:
#     try:
#         n = next(g)
#         print('g:',n)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break

# 生成器和yield
# def odd():
#     print('step1')
#     yield 1
#     print('step2')
#     yield 3
#     print('step3')
#     yield 5
# o = odd()
# next(o)
# next(o)
# next(o)

