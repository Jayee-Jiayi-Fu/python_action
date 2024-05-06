'''
在编写类时，有一个常被忽略的细节：类方法的组织顺序。
这个细节很小，并不影响代码的正确性，和程序的执行效率也没有任何关系。但如果你在写代码时忽视了它，就会让整个类变得十分难懂。
'''


# 面这个类的方法组织顺序就很糟糕：
# 当从上而下阅读UserServiceClient类时，你的思维会不断地来回跳跃，很难搞明白它所提供的主要接口究竟是什么
class UserServiceClient:
    """请求用户服务的Client 模块"""

    def __init__(self, service_host, user_token): ...

    def __str__(self):
        return f'UserServiceClient: {self.service_host}'

    def get_user_profile(self, user_id):
        """获取用户资料"""

    def request(self, params, headers, response_type):
        """发送请求"""

    @staticmethod
    def _parse_username(username):
        """解析用户名"""

    def _filter_posts(self, posts):
        """过滤无效的用户文章"""

    def get_user_posts(self, user_id):
        """获取用户所有文章"""

    @classmethod
    def initialize_from_request(self, request):
        """从当前请求初始化一个 UserServiceClient 对象"""


'''
在组织类方法时，我们应该关注使用者的诉求，把他们最想知道的内容放在前面，把他们不那么关心的内容放在后面。

下面是一些关于组织方法顺序的建议:
1. 作为惯例，__init__实例化方法应该总是放在类的最前面，__new__方法同理。
2. 公有方法应该放在类的前面，因为它们是其他模块调用类的入口，是类的门面，也是所有人最关心的内容。
3. 以_开头的私有方法，大部分是类自身的实现细节，应该放在靠后的位置。
4. 至于类方法、静态方法和属性对象，你不必将它们区分对待，直接参考公有/私有的思路即可。
    比如，大部分类方法是公有的，所以它们通常会比较靠前。
    而静态方法常常是内部使用的私有方法，所以常放在靠后的位置。
5. 以__开头的魔法方法比较特殊，我通常会按照方法的重要程度来决定它们的位置。
    比如一个迭代器类的__iter__方法应该放在非常靠前的位置，因为它是构成类接口的重要方法。
6. 最后一点，当你从上往下阅读类时，所有方法的抽象级别应该是不断降低的，就好像阅读一篇新闻一样，第一段是新闻的概要，之后才会描述细节。
'''

# 基于上面这些原则，我重新组织了UserServiceClient类


class UserServiceClient:
    """请求用户服务的Client 模块"""

    def __init__(self, service_host, user_token):
        ...

    @classmethod
    def initialize_from_request(self, request):
        # ❶initialize_from_request是类对外提供的API，所以放在靠前的位置
        """从当前请求初始化一个 UserServiceClient 对象"""

    def get_user_profile(self, user_id):
        """获取用户资料"""

    def get_user_posts(self, user_id):
        """获取用户所有文章"""

    def request(self, params, headers, response_type):
        # ❷request方法比其他两个公开方法的抽象级别要低，所以放在它们后面
        """发送请求"""

    def _filter_posts(self, posts):
        # ❸私有方法靠后放置
        """过滤无效的用户文章"""

    @staticmethod
    def _parse_username(username):
        """解析用户名"""

    def __str__(self):
        # ❹__str__魔法方法对于当前类来说不是很重要，可以放在靠后的位置
        return f'UserServiceClient: {self.service_host}'
