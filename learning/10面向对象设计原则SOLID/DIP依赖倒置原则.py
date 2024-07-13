# 案例：按来源统计 Hacker News条目数
import requests
from lxml import etree
from typing import Dict
from collections import Counter
from abc import ABC, abstractmethod


class HNWebPage(ABC):
    '''抽象类： Hacker News 站点页面'''

    @abstractmethod
    def get_text(self) -> str:
        raise NotImplementedError()


class RemoteHNWebPage(HNWebPage):
    # 低层模块依赖抽象的表现：提供抽象的具体实现
    '''远程页面，通过请求 Hacker News 站点返回内容'''

    def __init__(self, url: str):
        self.url = url

    def get_text(self) -> str:
        resp = requests.get(self.url)
        return resp.text


class LocalHNWebPage(HNWebPage):
    '''本地页面，根据本地文件返回页面内容

    :param path: 本地路径
    '''

    def __init__(self, path: str):
        self.path = path

    def get_text(self) -> str:
        with open(self.path, 'r') as fp:
            return fp.read()


class SiteSourceGrouper:
    '''
    对 Hacker News 新闻来源站点进行分组统计

    :param url: Hacker News 首页地址
    '''

    def __init__(self, page: HNWebPage):
        self.page = page

    def get_groups(self) -> Dict[str, int]:
        '''获取 （域名，个数） 分组'''
        html = etree.HMTL(self.page.get_text())

        # 通过 XPath语法 筛选新闻域名标签
        elems = html.xpath(
            '//table[@class="itemlist"]//span[@class="sitestr"]')
        groups = Counter()
        for elem in elems:
            groups.update([elem.text])
        return groups


def main():
    page = RemoteHNWebPage(url="Https://news.ycombinator.com/")
    groups = SiteSourceGrouper(page).get_groups()
    # 打印最常见的3个域名
    for key, value in groups.most_commom(3):
        print(f'Site: {key} | Count: {value}')
