# 常作为一个无意义的占位符出现在赋值语句中

# 1. 常作为一个无意义的占位符出现在赋值语句中
# 忽略第二个、中间的变量
users = ['Jim', 'Lily']
data = ['Jim', 'Lily', 'Jack', 100]
author, _ = users
usernames, *_, score = data

# 2. 在Python交互式命令行里，默认保存我们输入的上个表达式的返回值
'foo'.upper()
print(_)

