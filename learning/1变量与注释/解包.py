# 注释是为了明白代码的意图，而非描述代码本身
# 好的变量和注释并非为计算机而写，是为每个阅读代码的人而写（包括你自己）


# 变量常见用法
# 1. 定义变量
# Python是一门动态类型的语言，所以我们无须预先声明变量类型
author = 'piglei'
print('Hello,{}!'.format(author))

# 2. 同时操作多个变量
author, reader = 'Jim', 'King'
author, reader = reader, author
print(author, reader)

# 3. 变量解包
# 特殊赋值操作，把一个可迭代对象（比如列表）的所有成员，一次性赋值给多个变量
usernames = ['Lily', 'Jack']
author, reader = usernames
print(author, reader)


# 4. 展开多层嵌套数据
attrs = [1, ['piglei', 100]]
user_id, (usernames, score) = attrs
print(user_id, usernames, score)

# 5. 星号表达式（*variables）作为变量名，会贪婪地捕获多个值对象
data = ['piglei', 'apple', 'orange', 'banana', 100]
username, *fruits, score = data
print(username, fruits, score)

# 6. 循环中解包
for username, score in [('piglei', 100), ('raymod', 60)]:
    print(username, score)