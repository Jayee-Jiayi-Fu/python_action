from collections import OrderedDict

# 字典：多维度的key: value键值对

# 1. 创建和获取
movie = {'name': "Burning", 'type': 'movie', 'year': 2018}
# 通过key获取
print(movie['name'])
# 可变类型，增加新key
movie['rating'] = 10
print(movie['rating'])
# key不可重复，同一个key复制会覆盖旧址
movie['rating'] = 9.8
print(movie['rating'])


# 2. 遍历字典
for key in movie:
    print(key, movie[key])

for key, value in movie.items():
    print(key, value)


# 3. 访问不存在的字典键
# 比较常见的处理方式有两种：
# （1）读取内容前先做一次条件判断，只有判断通过的情况下才继续执行其他操作；
if 'rating' in movie:
    rating = movie['rating']
else:
    rating = 0
# （2）直接操作，但是捕获KeyError异常。(更推荐)
try:
    rating = movie['rating']
except KeyError:
    rating = 0
# 如果只是“提供默认值的读取操作”，可以直接使用字典的.get()方法。
print(movie.get('price', '55'))


# 4. 使用setdefault取值并修改
# ❶若key不存在，以空列表[]初始化并返回
# ❷若key存在，直接返回旧值
d = {'title': 'foobar'}
d.setdefault('items', []).append('foo')
print('d>> ', d)
d.setdefault('items',[]).append('bar')
print('d>> ', d)


# 5. 使用pop方法删除不存在的键
# 一般要想安全地删除某个键，需要加上一段异常捕获逻辑
try:
    del d['title']
    print('del>> ', d)
except KeyError:
    pass
# 想去掉某个键，并不关心它存在与否、删除有没有成功,使用dict.pop(key,default)方法就够了
# 严格说来，pop方法的主要用途并不是删除某个键，而是取出这个键对应的值。但偶尔用它来执行删除操作也无伤大雅。
d.pop('title',None)
print('del>> ', d)


# 6. 字典推导式
d1 = {'foo':3, 'bar':4}
d2 = {key:value * 10 for key, value in d1.items() if key == 'foo'}
print(d2)


# 7. 字典的有序性与无序性
# 3.6 版本以前，“Python的字典是无序的。”
# 3.6 优化了底层实现，字典变得有序了
# 3.7 版本，它已经彻底成了语言规范的一部分

# 7.1 collections.OrderedDict
# 原生字典 key he value 相同，即相等
# orderedDict，顺序也要相同才相等
d1 = {'name': 'piglei', 'fruit':'apple'}
d2 = {'fruit':'apple', 'name':'piglei'}
print('d1==d2:', d1 == d2)

d1 = OrderedDict(name= 'piglei', fruit='apple')
d2 = OrderedDict(fruit='apple', name='piglei')
print('d1==d2:', d1 == d2)