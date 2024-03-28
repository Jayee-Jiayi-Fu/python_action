# Python 是动态语言，可以返回多种类型结果
def get_users(user_id=None):
    if user_id is not None:
        return ("name", 'Jayee')
    else:
        return "Not Found"


print(get_users())
print(get_users(1))


# 建议：01 尽量只返回一种类型
# 如果会返回多个类型，最好是拆分成独立的函数分别返回，例如：
# （1） get_user_by_id(user_id)：返回单个用户。
# （2） get_active_users()：返回多个用户列表。


# 建议：02．谨慎返回None值
# “空值”通常用来表示某个应该存在但是缺失的东西
# 在Python中，None是独一无二的存在，在Python中，None是独一无二的存在
# 当我们需要让函数返回None时，主要是下面3种情况

# 1. 操作类函数的默认返回值
# 当某个操作类函数不需要任何返回值时，通常会返回None。与此同时，None也是不带任何return语句的函数的默认返回值


# 2. 意料之中的缺失值
# 函数执行后可能有结果，也可能没有结果。而重点在于，对于函数的调用方来说，“没有结果”是意料之中的事情。


# 3. 在执行失败时代表“错误”
# 对这些函数来说，用抛出异常来代替返回None会更为合理


# 总结：从上面的分析来看，适合返回None的函数需要满足以下两个特点：
# （1）函数的名称和参数必须表达“结果可能缺失”的意思；
# （2）如果函数执行无法产生结果，调用方也不关心具体原因。

# 除了“搜索”“查询”几个场景外，对绝大部分函数而言，返回None并不是一个好的做法。对这些函数来说，用抛出异常来代替返回None会更为合理
class UnableToCreateUser(Exception):
    """当无法创建用户时抛出"""


def create_user_from_name(username):
    """通过用户名创建一个 User 实例
    :raises: 当无法创建用户时抛出 UnableToCreateUser
    """
    if validate_username(username):
        return User.from_username(username)
    else:
        raise UnableToCreateUser(f'unable to create user from {username}')


try:
    user = create_user_from_name(username)
except UnableToCreateUser:
    pass
    # 此处编写异常处理逻辑
else:
    user.do_something()


# 早返回，多返回
# “单一出口”原则的可读性不是很好，阅读函数过程中必须先把所有逻辑装进脑子里，只有等到最后的return出现时，才能搞清楚所有事情
def user_get_tweets(user):
    """获取用户已发布状态
    - 如果配置"展示随机状态"，获取随机状态
    - 如果配置"不展示任何状态"，返回空的占位符状态
    - 默认返回最新状态
    """
    tweets = []
    if user.profile.show_random_tweets:
        tweets.extend(get_random_tweets(user))
    elif user.profile.hide_tweets:
        tweets.append(NULL_TWEET_PLACEHOLDER)
    else:
        # 最新状态需要用token 从其他服务获取，并转换格式
        token = user.get_token()
        latest_tweets = get_latest_tweets(token)
        tweets.extend([transorm_tweet(item) for item in latest_tweets])
    return tweets


# 调整一下写代码的思路：一旦函数在执行过程中满足返回结果的要求，就直接返回，函数的逻辑变得更容易理解。
# 函数的逻辑变得更容易理解
def user_get_tweets(user):
    """获取用户已发布状态"""
    if user.profile.show_random_tweets:
        return get_random_tweets(user)
    if user.profile.hide_tweets:
        return [NULL_TWEET_PLACEHOLDER]
    # 最新状态需要用token 从其他服务获取，并转换格式
    token = user.get_token()
    latest_tweets = get_latest_tweets(token)
    return [transorm_tweet(item) for item in latest_tweets]
