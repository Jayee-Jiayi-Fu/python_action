'''
03 当心已被耗尽的迭代器


'''
numbers = [1, 2, 3]

# 使用生成器表达式创建一个新的生成器对象
# 此时想象中的numbers 内容为：2, 4, 6
numbers = (i * 2 for i in numbers)

# 假如你连着对numbers做两次成员判断，程序会返回截然不同的结果：

#第一次 in 判断会触发生成器遍历，找到 4后返回 True
4 in numbers
#True

# 做第二次 in 判断时，生成器已被部分遍历过，无法再找到 4，因此返回意料外的结果 False
4 in numbers
#False

'''
这种由生成器的“耗尽”特性所导致的bug，隐蔽性非常强，当它出现在一些复杂项目中时，尤其难定位
因此在平时，你需要将生成器（迭代器）的“可被一次性耗尽”特点铭记于心，避免写出由它所导致的bug。
假如要重复使用一个生成器，可以调用list()函数将它转成列表后再使用。

除了生成器函数、生成器表达式以外，人们还常常忽略内置的map()、filter()函数也会返回一个一次性的迭代器对象。在使用这些函数时，也请务必当心。
'''