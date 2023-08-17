"""复制图片"""
def copy_img():
    try:
        with open('Nico.jpeg', 'rb') as fs1:
            data = fs1.read()

            # <class 'bytes'>
            print(type(data))

        with open('Nico_copy.jpeg', 'wb') as fs2:
            fs2.write(data)

    except FileNotFoundError:
        print("文件不存在！")
    except LookupError:
        print("使用了未知编码")
    except UnicodeDecodeError:
        print("读取文件时解码错误")
    except IOError:
        print("读写文件时发生错误！")