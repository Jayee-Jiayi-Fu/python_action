# 字符串：str，也称“文本”，是给人看的，使用Unicode标准，可通过.encode()方法编码为字节串
# 字节串：bytes，也称“二进制字符串”，定包含某种真正的字符串编码格式（默认为UTF-8），可通过.decode()解码为字符串。

str_obj = 'hello, 世界'
print(str_obj, type(str_obj))

bin_str = str_obj.encode('UTF-8')
print(bin_str, type(bin_str))

# 默认使用‘UTF-8’
print(str_obj.encode('UTF-8') == bin_str)

# 创建字节串字面量
bin_obj2 = b'Hello'
print(type(bin_obj2))


# 两者不能混用， str 不能使用 bytes 的内置方法，反之亦然
# 最佳实践：应该尽量保证总是操作普通字符串，而非字节串


# 必须操作字面量的场景，一般只有两种：
# 1. 程序从文件或其他外部存储读取字节串内容，将其解码为字符串，然后再在内部使用；
# 2. 程序完成处理，要把字符串写入文件或其他外部存储，将其编码为字节串，然后继续执行其他操作。