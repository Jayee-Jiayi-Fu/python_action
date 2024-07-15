# ISP：	一条与接口有关的原则，要求”用户“不应该依赖任何它不适用的方法。
# 一个接口所提供的方法应该刚好满足使用方的需求，一个不多一个不少
# 用户：接口的使用方（客户模块），也就是依赖接口的「高层模块」
# 设计接口的技巧：让客户（调用方）来驱动协议设计

import datetime
import requests
from abc import ABC, abstractmethod


class ContentOnlyHNWebPage(ABC):
    """抽象类： Hacker News 站点页面（仅提供内容）"""
    @abstractmethod
    def get_text(self) -> str:
        raise NotImplementedError()


class HNWebPage(ABC):
    """抽象类： Hacker News 站点页面（含元数据）"""

    @abstractmethod
    def get_text(self) -> str:
        """获取页面文本内容"""
        raise NotImplementedError()

    @abstractmethod
    def get_size(self) -> int:
        """获取页面大小"""

    @abstractmethod
    def get_generated_at(self) -> datetime.datetime:
        """获取页面生成时间"""


class RemoteHNWebPage(HNWebPage):
    """远程页面： 通过请求 Hacker News 站点返回内容"""

    def __init__(self, url: str):
        self.url = url
        # 保存当前请求结果
        self._resp = None
        self._generated_at = None

    def get_text(self) -> str:
        """获取页面内容"""
        self._request_on_demand()
        return self._resp.text

    def get_size(self) -> int:
        """获取页面大小"""
        return len(self.get_text())

    def get_generated_at(self) -> datetime.datetime:
        """获取页面生成时间"""
        self._request_on_demand()
        return self._generated_at

    def _request_on_demand(self):
        """请求远程地址并避免重复"""
        if self._resp is None:
            self._resp = requests.get(self.url)
            self._generated_at = datetime.datetime.now()


class LocalHNWebPage(ContentOnlyHNWebPage):
    """本地页面，根据本地文件返回页面内容

    :param path: 本地路径
    """

    def __init__(self, path: str):
        self.path = path

    def get_text(self) -> str:
        with open(self.path, 'r') as fp:
            return fp.read()


class SiteAchiever:
    """将不同时间点的Hacker News 页面归类"""
    @staticmethod
    def save_page(page: HNWebPage):
        """将页面保存到后端数据库"""
        data = {
            'content': page.get_text(),
            'generated_at': page.get_generated_at(),
            'size': page.get_size()
        }
        return data
        # 将data保存到数据库中...
