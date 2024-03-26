# 1. 函数接收的参数要尽量少，不能太多
# 2. Python 支持有序位置参数 及 关键字参数
# 3. 当要调用参数较多（超过3个）的函数时，使用关键字参数模式可以大大提高代码的可读性。


def query_users1(limit, offset, min_followers_count, include_profile):
    '''查询用户
    :param min_followers_count: 最小关注者数量
    :param include_profile: 结果包含用户详细档案
    '''
    pass


# 使用位置参数调用（难读）
query_users1(20, 0, 100, True)

# 使用关键字参数(更易读）
query_users1(min_followers_count=100, include_profile=True, limit=20, offset=0)


# 4. 强制使用关键字参数
# 通过在参数列表中插入*符号，该符号后的所有参数都变成了“仅限关键字参数
# 如果调用方仍然想用位置参数来提供这些参数值，程序就会抛出错误
def query_users2(limit, offset, *, min_followers_count, include_profile):
    '''查询用户
    :param min_followers_count: 最小关注者数量
    :param include_profile: 结果包含用户详细档案
    '''
    pass


# 使用位置参数调用
try:
    query_users2(20, 0, 100, True)
except TypeError as e:
    print(f'未使用未知参数调用报错： {e}')

# 使用关键字参数
query_users2(20, 0, min_followers_count=100, include_profile=True)


# 对称方法：仅限位置参数'/'
def query_users2(limit, offset, /, min_followers_count, include_profile):
    '''查询用户
    :param min_followers_count: 最小关注者数量
    :param include_profile: 结果包含用户详细档案
    '''
    pass
