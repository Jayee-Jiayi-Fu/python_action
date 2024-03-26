'''
01 中断嵌套循环的正确方式

想要中断某个循环时，可以使用break语句。但break不能马上跳出嵌套循环。更多的break意味更容易出bug。

'''


def print_first_word(fp, prefix):
    '''找到文件里第一个以指定前缀开头的单词并打印出来'''
    first_word = None
    for line in fp:
        for word in line.split():
            if word.startwith(prefix):
                # 注意：此处的break 只能跳出最内层循环
                break
        # 一定要在外层加一个额外的break 语句来判断是否结束循环
        if first_word:
            break
    if first_word:
        print(f'Found the first word startswith "{prefix}": "{first_word}"')
    else:
        print(f'Word starts with "{prefix}" was not found.')


'''
要从嵌套循环中快速跳出，更好的做法是把循环代码拆分为一个新函数，然后直接使用return
上面例子可以改写成两个函数
'''


def find_first_word(fp, prefix):
    for line in fp:
        for word in line.split():
            if word.startwith(prefix):
                return word
    return None


def print_first_word_v2(fp, prefix):
    first_word = find_first_word(fp, prefix)
    if first_word:
        print(f'Found the first word startswith "{prefix}": "{first_word}"')
    else:
        print(f'Word starts with "{prefix}" was not found.')
