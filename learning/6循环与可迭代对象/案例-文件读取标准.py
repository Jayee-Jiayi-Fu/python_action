'''
01. 读取文件的标准做法
首先用with open (fine_name)上下文管理器语法获得一个文件对象，然后用for循环迭代它，逐行获取文件里的内容
'''

def count_digits(fname):
    """计算文件里包含多少个数字字符"""
    count = 0
    with open(fname) as file:
        for line in file:
            for s in line:
                if s.isdigit():
                    count += 1
    return count
'''
它有两个好处：
（1）with上下文管理器会自动关闭文件描述符；
（2）在迭代文件对象时，内容是一行一行返回的，不会占用太多内存。

缺点:
假如被读取的文件里根本就没有任何换行符，那么上面列的第（2）个好处就不再成立。
缺少换行符以后，程序遍历文件对象时只能一次性生成一个巨大的字符串对象，白白消耗大量时间和内存。
'''



'''
02．使用while循环加read()方法分块读取
调用file.read(chunk_size),会马上读取从当前游标位置往后chunk_size大小的文件内容，不必等待任何换行符出现
'''
def count_digits_v2(fname):
    """计算文件里包含多少个数字字符，每次计算8k"""
    count = 0
    block_size = 1024 * 8
    with open(fname) as file:
        while True:
           chunk = file.read(block_size)
           if not chunk:
               break
           for s in chunk:
               if s.isdigit():
                   count += 1
    return count

'''新代码虽然解决了大文件读取时的性能问题，循环内的逻辑却变得更零碎了。如果使用iter()函数，我们可以进一步简化代码。'''



'''
03 iter()的另一个用法
1. iter()是一个用来获取迭代器的内置函数，

2. 以iter(callable, sentinel)的方式调用iter()函数时，会拿到一个特殊的迭代器对象。
    用循环遍历这个迭代器，会不断返回调用callable()的结果，假如结果等于sentinel，迭代过程中止。
    利用这个特点，我们可以把上面的while重新改为for，让循环内部变得更简单
    
3. partical(func[, *args][, **keywords] ) 把一个函数的某些参数固定住，返回一个新函数
'''
from functools import partial
def count_digits_v3(fname):
    """计算文件里包含多少个数字字符，每次计算8k"""
    count = 0
    block_size = 1024 * 8
    with open(fname) as file:
        '''使用functiools.partial构造一个新的不用参数的函数'''
        _read = partial(file.read, block_size)
        '''构造一个不断调用 _read 的迭代器'''
        for chunk in iter(_read, ''):
            for s in chunk:
                if s.isdigit():
                    count += 1
    return count



'''
04．按职责拆解循环体代码

循环内部存在两个独立的逻辑：“数据生成”（从文件里不断获取数字字符）与“数据消费”（统计个数）。这两个独立逻辑被放在了同一个循环体内，耦合在了一起

要解耦循环体，生成器（或迭代器）是首选
'''
def read_file_digists(fp, block_size = 1024 * 8):
    _read = partial(fp.read, block_size)
    for chunk in iter(_read, ''):
        for s in chunk:
            if s.isdigit():
                yield s

def count_digits_v4(fname):
    count = 0
    with open(fname) as file:
        for _ in read_file_digists(file):
            count += 1
    return count

'''需要统计偶数时，可以直接复用read_file_digits()函数'''
from collections import defaultdict
def count_even_groups(fname):
    counter = defaultdict(int)
    with open(fname) as file:
        for num in read_file_digists(file):
            if int(num) % 2 == 0:
                counter[int(num)] += 1
    return counter