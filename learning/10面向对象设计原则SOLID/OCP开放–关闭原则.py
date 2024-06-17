# SOLID原则的第二条是OCP（开放–关闭原则）。该原则认为：类应该对扩展开放，对修改封闭。换句话说，你可以在不修改某个类的前提下，扩展它的行为。
import sys
from typing import Iterable, TextIO, Optional, List

import requests
from lxml import etree
from urllib import parse
from abc import ABC, abstractmethod


class Post:
    ''' Hacker News 上的条目

    :param title: 标题
    :param link: 链接
    :param points: 当前评分
    :param comments_cnt: 评论数
    '''

    def __init__(self, title: str, link: str, points: str, comments_cnt: str):
        self.title = title
        self.link = link
        self.points = points
        self.comments_cnt = comments_cnt


# 把“写入文件”相关的内容进行拆分
class PostsWriter:
    '''负责将帖子列表写入文件中'''

    def __init__(self, fp, title):
        self.fp = fp
        self.title = title

    def write(self, posts: List[Post]):
        '''以纯文本格式将 hacker News Top 内容写入文件'''
        self.fp.write(f'# {self.title}\n\n')
        # ❶enumerate()接收第二个参数，表示从这个数开始计数（默认为0）
        for i, post in enumerate(posts, 1):
            self.fp.write(f'> Top {i}: {post.title}\n')
            self.fp.write(f'> 分数：{post.points} 评论数：{post.comments_cnt}\n')
            self.fp.write(f'> 地址：{post.link}\n')
            self.fp.write('------\n')


class PostFilter(ABC):
    '''抽象类：定义如何过滤结果'''
    @abstractmethod
    def validate(self, post: Post) -> bool:
        '''判断帖子是否应该保留'''


class DefaultPostFilter(PostFilter):
    '''保留所有帖子'''

    def validate(self, post: Post) -> bool:

        return True


class GithubPostFilter(PostFilter):

    def validate(self, post: Post) -> bool:
        # 只关注来自GitHub的内容

        parsed_link = parse.urlparse(post.link)
        return parsed_link.netloc == 'github.com'


class HNTopPostsSpider:
    '''抓取 Hacker New Top 内容条目

    :param limit: 限制条目数，默认为5
    :param post_filter: 过滤结果条目算法，默认保留所有
    '''
    items_url = 'https://news.ycombinator.com/'
    file_title = 'Top news on HN'

    # def __init__(self, limit: int = 5,
    #              post_filter: Optional[PostFilter] = None):
    # 方法二：依赖注入

    #     self.limit = limit
    #     self.post_filter = post_filter or DefaultPostFilter()

    def __init__(self, limit: int = 5,
                 filter_by_hosts: Optional[List[str]] = None):
        # 方法三：数据驱动

        self.limit = limit
        self.filter_by_hosts = filter_by_hosts

    def fetch(self) -> Iterable[Post]:
        ''' 从 Hacker News 抓取 Top 内容

        :return: 可迭代的 Post 对象
        '''
        resp = requests.get(self.items_url)

        # 使用 XPath 可以方便地从页面揭示出需要的内容，以下均为页面解析代码
        html = etree.HTML(resp.text)
        items = html.xpath('//table/tr[@class="athing"]')
        counter = 0

        for item in items:
            if counter > self.limit:
                break

            node_title = item.xpath('.//span[@class="titleline"]/a')[0]
            link = node_title.get('href')
            node_detail = item.getnext()
            points_text = node_detail.xpath('.//span[@class="score"]/text()')
            comments_text = node_detail.xpath(
                './/span[@class="subline"]/a[last()]/text()')

            post = Post(
                title=node_title.text,
                link=link,
                # 条目可能会没有评分和评论
                points=points_text[0].split()[0] if points_text else '0',
                comments_cnt=comments_text[0].split(
                )[0] if comments_text else '0'
            )

            # 方法一：继承
            # if self.interested_in_post(post):

            # 方法二：“依赖注入”
            # if self.post_filter.validate(post):

            # 方法三：数据驱动
            if self._check_link_from_hosts(post.link):
                counter += 1
                yield post

    def interested_in_post(self, post: Post) -> bool:
        # 判断是否应将帖子放入结果中

        # 只关注来自GitHub的内容
        # parsed_link = parse.urlparse(link)
        # if parsed_link.netloc == 'github.com':

        return True

    def _check_link_from_hosts(self, link: str) -> bool:
        # 检查某链接是否属于所定义站点

        if self.filter_by_hosts is None:
            return True
        parsed_link = parse.urlparse(link)
        return parsed_link.netloc in self.filter_by_hosts


def get_hn_top_posts(fp: Optional[TextIO] = None):
    """获取 Hacker News Top 内容，并将其写入文件中

    :param fp: 需要写入的文件，如未提供，将向标准输出打印
    """
    dest_fp = fp or sys.stdout

    # 方法二：依赖注入
    # crawler = HNTopPostsSpider(post_filter=GithubPostFilter())

    # 方法三：数据驱动
    hosts = ['github.com', 'micropolisweb.com']
    crawler = HNTopPostsSpider(filter_by_hosts=hosts)

    writer = PostsWriter(dest_fp, title='Top news on HN')
    writer.write(list(crawler.fetch()))


def main():
    # with open('/tmp/hn_top5.txt') as fp:
    #     get_hn_top_posts（fp)

    # 实现向控制台标准输出打印功能
    get_hn_top_posts()


if __name__ == '__main__':
    main()
