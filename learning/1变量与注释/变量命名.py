# 几条命名的原则

# 1. 遵循PEP 8原则
# · 对于普通变量，使用蛇形命名法，比如max_value；
# · 对于常量，采用全大写字母，使用下划线连接，比如MAX_VALUE；
# · 如果变量标记为“仅内部使用”，为其增加下划线前缀，比如_local_var；
# · 当名字与Python关键字冲突时，在变量末尾追加下划线，比如class_。
#   类名应该使用驼峰风格（FooClass）、函数应该使用蛇形风格（bar_function）


# 2. 描述性要强
# 在可接受的长度范围内，变量名所指向的内容描述得越精确越好


# 3. 要尽量短
# 为变量命名要结合代码情境和上下文


# 4. 要匹配类型
# 4.1 匹配布尔值类型的变量名
# 要让人觉得它只有“肯定”和“否定”两种可能。例如：is、has、allow

# 4.2 匹配int/float类型的变量名
# 释义为数字的所有单词，比如port（端口号）、age（年龄）、radius（半径）等；
# 使用以_id结尾的单词，比如user_id、host_id；
# 使用以length/count开头或者结尾的单词，比如length_of_username、max_length、users_count。
# 最好别拿一个名词的复数形式来作为int类型的变量名，比如apples、trips等

# 4.3 匹配其他类型的变量名
# 剩下的字符串（str）、列表（list）、字典（dict）等其他值类型，强烈建议在代码中明确标注它们的类型详情


# 5. 超短命名
# 5.1 大家约定俗成的短名字
# · 数组索引三剑客i、j、k· 某个整数n· 某个字符串s· 某个异常e· 文件对象fp
# 但如果条件允许，建议尽量用更精确的名字替代

# 5.2 对一些其他常用名的缩写
# 如果一些长名字反复出现，可以为它们设置一些端名字作为别名，使代码更紧凑、易读。但是同一个项目内不宜太多，否则适得其反。
'''
from django.utils.translation import gettext as _
    print(_('带翻译文字'))
'''


# 6. 其他技巧
# · 在同一段代码内，不要出现多个相似的变量名，比如同时使用users、users1、users3这种序列；
# · 可以尝试换词来简化复合变量名，比如用is_special来代替is_not_normal；
# · 请打开GitHub[插图]，到其他人的开源项目里找找灵感吧！
