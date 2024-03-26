from typing import List

# 1.  函数文档


def remove_invalid(items):
    ''' 剔除 items 里的无效元素
    :param items: 待剔除对象
    :type items: 包含整数的列表，[int, ...]
    '''
    pass


# 2. 类型注解，Python3.5后内置
# - “类型注解”只是一种有关类型的注释，不提供任何校验功能
# - 大部分的现代化IDE[插图]会读取类型注解信息，提供更智能的输入提示
# - 类型注解配合mypy等静态类型检查工具，能提升代码正确性
def remove_invalid2(items: List[int]):
    ''' 剔除 items 里的无效元素
    '''
    pass
