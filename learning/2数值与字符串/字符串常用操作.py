# 1. 把字符串当序列
# 可以对它进行遍历、切片等操作，就像访问一个列表对象一样
s = 'Hello. world!'
for c in s:
    print(c)

s2 = s[::-1]
print(s, s2)

# 2. 字符串格式化
# 三种主要的字符串格式化方式

username, score = 'piglei', 100
# C语言风格：历史最为悠久，但现在已经很少使用
print('Welcome %s, your score is %d' % (username, score))

# 新式字符串格式化（str.format）方式（Python 2.6新增）
print('Welcome {}, your score is {:d}'.format(username, score))
# str.format支持用位置参数来格式化字符串
print('{0}:name={0} score{1}'.format(username, score))

# f-string字符串字面量格式化表达式（Python 3.6新增）
print(f'Welcome {username}, your score is {score:d}')


# 3. 拼接多个字符串
# 常见的Python式做法是：首先创建一个[空列表]，然后把需要拼接的字符串都放进列表，最后调用str.join来获得大字符串
words = ['Numbers(1-10):']
for i in range(10):
    words.append(f'Value: {i + 1}')
print('\n'.join(words))


# 4. 不常用但特别好用的字符串方法
#  s.isdigit()
#  判断某个字符串是否只包含数字
print('123'.isdigit(), 'foo'.isdigit())

# s.partition()
# 按照分隔符sep切分字符串，返回一个包含三个成员的元组：(part_before, sep, part_after)


def extract_value_v1(s):
    items = s.split(':')
    if len(items) == 2:
        return items[1]
    else:
        return ''


def extract_value_v2(s):
    # 当s包含分隔符：时，元组最后一个成员刚好是value
    # 若没有分隔符，最后一个成员默认是空字符串‘’
    return s.partition(':')[-1]


print(extract_value_v1('name:piglei'))
print(extract_value_v2('name:piglei'))

# s.translate()
# 按规则一次性替换多个字符
s = '明明是中文,却使用了英文标点.'
table = s.maketrans(',.', '，。')
s2 = s.translate(table)
print(s, s2)
