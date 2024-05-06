# =======================
# 01．用函数降低API使用成本
# =======================
# 使用requests请求某个网址，只要写两行代码即可：
from project.config import AppConfig
from request import sessions
import requests


r = requests.get('https://example.com', auth=('user', 'pass'))

# 上面代码的内部实现是这样的
# 来自 requests.api模块


def request(method, url, **kwargs):
    with sessions.Session() as session:  # ❶实例化一个Session上下文对象，完成请求
        return session.request(method=method, url=url, **kwargs)


'''
假如requests包的作者删掉这个函数，让用户直接使用sessions.Session()对象，行不行？
当然可以。但在使用者看来，显然调用函数比实例化Session()对象要讨喜得多。


在Python中，像上面这种用函数搭配面向对象的代码非常多见，它有点儿像设计模式中的外观模式（facade pattern）。
在该模式中，函数作为一种简化API的工具，封装了复杂的面向对象功能，大大降低了使用成本。
'''


# =======================
# 02．实现“预绑定方法模式”
# =======================
# 下面的代码就应用了单例模式的配置类AppConfig
class AppConfig:
    """程序配置类，使用单例模式"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            inst = super().__new__(cls)
            # 省略：从外部配置文件读取配置
            ...
            cls._instance = inst
        return cls._instance

    def get_database(self):
        """读取数据库配置"""
        ...

    def reload(self):
        """重新读取配置文件，刷新配置"""
        ...


'''
在Python中，实现单例模式的方式有很多，而上面这种最为常见，它通过重写类的__new__方法来接管实例创建行为。
当__new__方法被重写后，类的每次实例化返回的不再是新实例，而是同一个已经初始化的旧实例cls._instance


基于上面的设计，如果其他人想读取数据库配置，代码需要这样写：
'''
db_conf = AppConfig().get_database()
# 重新加载配置
AppConfig().reload()

'''
虽然在处理这种全局配置对象时，单例模式是一种行之有效的解决方案，但在Python中，其实有一种更简单的做法——预绑定方法模式。


预绑定方法模式（prebound method pattern）
是一种将对象方法绑定为函数的模式。要实现该模式，
第一步就是完全删掉AppConfig里的单例设计模式。因为在Python里，实现单例压根儿不用这么麻烦，我们有一个随手可得的单例对象——模块（module）。
当你在Python中执行import语句导入模块时，无论import执行了多少次，每个被导入的模块在内存中只会存在一份（保存在sys.modules中）。
因此，要实现单例模式，只需在模块里创建一个全局对象即可：
'''


class AppConfig:
    """程序配置类，使用单例模式"""

    def __init__(self):  # ➊ 完全删掉单例模式的相关代码，只实现__init__方法
        # 省略：从外部配置文件读取配置
        ...


# ➋_config就是我们的“单例AppConfig对象”，它以下划线开头命名，表明自己是一个私有全局变量，以免其他人直接操作
_config = AppConfig()

# 下一步，为了给其他模块提供好用的API，我们需要将单例对象_config的公有方法绑定到config模块上：
# file: project/config.py
_config = Config()
get_database_conf = _config.get_database
reload_config = _config.reload
