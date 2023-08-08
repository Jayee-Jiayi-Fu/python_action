from math import sqrt
"""判断素数是函数"""
def is_pritm(n):
    assert n > 0
    for factor in range(2,int(sqrt(n))+1):
        if n % factor == 0:
            return False
    return True if n != 1 else False


filenames = ('a.txt','b.txt','c.txt')
fs_list = []
try:
    for filename in filenames:
        fs_list.append(open(filename,'w',encoding='utf-8'))
    for number in range(1,10000):
        if is_pritm(number):
            value = str(number) + '\n'
            if number < 100:
                fs_list[0].write(value)
            if number < 1000:
                fs_list[1].write(value)
            else:
                fs_list[2].write(value)

except FileNotFoundError:
    print("文件不存在！")
except LookupError:
    print("使用了未知编码")
except UnicodeDecodeError:
    print("读取文件时解码错误")
except IOError:
    print("读写文件时发生错误！")