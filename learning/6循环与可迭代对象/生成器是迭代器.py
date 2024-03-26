'''
在第3章中我简单介绍过生成器对象:
生成器是一种“懒惰的”可迭代对象，使用它来替代传统列表可以节约内存，提升执行效率。
除此之外，生成器还是一种简化的迭代器实现，使用它可以大大降低实现传统迭代器的编码成本。
因此在平时，我们基本不需要通过__iter__和__next__来实现迭代器，只要写上几个yield就行。
'''

'''
如果利用生成器，上面的Range7Iterator可以改写成一个只有5行代码的函数：
'''
def range_7_gen(start, end):
    num = start
    while num < end:
        if num != 0 and (num % 7 == 0 or '7' in str(num)):
            yield num
        num += 1


nums = range_7_gen(0,20)
print('iter(nums) -- ',iter(nums))
print('iter(nums) == nums -- ',iter(nums) == nums)
print('next(nums) -- ', next(nums))
print('next(nums) -- ', next(nums))
print('next(nums) -- ', next(nums))
print('next(nums) -- ', next(nums)) # StopIteration

'''
生成器（generator）利用其简单的语法，大大降低了迭代器的使用门槛，是优化循环代码时最得力的帮手。
'''