import time

#  1. 般读取文件方法
# 须有手动调用close关闭读取开关
def normal_read():
    f = None
    try:
        f = open('data.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print("文件不存在！")
    except LookupError:
        print("使用了未知编码")
    except UnicodeDecodeError:
        print("读取文件时解码错误")
    finally:
        f.close()


# 2. 使用 with 语句，简化调用
# 不需要显式调用close
def with_read():
    try:
        # 一次性读取整个文件内容
        with open('data.txt','r',encoding='utf-8') as f:
            print(f.read())

        # 通过for-in逐行读取
        with open('data.txt',mode='r') as f:
            for line in f:
                print('--',line)
                time.sleep(0.5)

        # 读取文件按行读取到列表中
        with open('data.txt','r',) as f:
            lines = f.readlines()
            print(lines)

    except FileNotFoundError:
        print("文件不存在！")
    except LookupError:
        print("使用了未知编码")
    except UnicodeDecodeError:
        print("读取文件时解码错误")