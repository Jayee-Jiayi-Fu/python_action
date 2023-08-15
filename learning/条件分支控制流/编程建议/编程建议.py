# 1. 尽量避免多层分支嵌套
# 要竭尽所能地避免分支嵌套，一个简单的优化技巧——“提前返回”
# 当你在编写分支时，首先找到那些会中断执行的条件，把它们移到函数的最前面，然后在分支里直接使用return或raise结束执行。


# 2. 别写太复杂的条件表达式
# 一个包含大量not/and/or的复杂表达式，通过把它们封装成函数或者对应的类方法进行简化
# 进行恰当的封装后，之前大段的注释文字甚至可以直接删掉了，因为优化后的条件表达式已经表意明确
# 封装不仅仅是用来提升可读性的可选操作，有时甚至是必须要做的事情
# 如果判断逻辑在项目中多次出现时，假设缺少封装，那些复杂的条件表达式就会被不断地“复制粘贴”，彻底让代码变得不可维护。
# 例如：if activity.allow_new_user() and user.match_activity_condition():


# 3. 尽量降低分支内代码的相似性
# 很多时候因为一些逻辑上的相似性，导致代码也很类似。这种“类似”有几种表现形式，有时是完全重复的语句，有时则是调用函数时的重复参数。
# 假如不同分支下的代码过于相似，读者就会很难理解代码的含义，因为他需要非常细心地区分不同分支下的行为究竟有什么差异。
# 技巧1：把重复代码移到分支外
# 技巧2：动态关键字参数（**kwargs）特性


# 4. 使用“德摩根定律”
# not A or not B等价于not (A and B)


# 5. 使用all()/any()函数构建条件表达式
# · all(iterable)：仅当iterable中所有成员的布尔值都为真时返回True，否则返回False。
# · any(iterable)：只要iterable中任何一个成员的布尔值为真就返回True，否则返回False。
def all_numbers_gt_10(members):
    return bool(members) and all(n>10 for n in members)


# 6. 留意and和or的运算优先级
# and运算符的优先级高于or
# 如果加上一些括号可以让逻辑变得更清晰，那就不要吝啬。


# 7. 避开or运算符的陷阱
# or 具有“短路求值”特性
# a or b or c or ...这样的表达式，会返回这些变量里第一个布尔值为真的对象，直到最末一个为止
# or陷阱： or计算的是变量的布尔真假值，所以不光是None，0、[]、{}以及其他所有布尔值为假的东西，都会在or运算中被忽略