# 案例：一个简单的Hacker News爬虫
# 从设计的角度看，下面代码违反了SOLID原则中的第一条：SRP，
# SRP认为：一个类应该仅有一个被修改的理由。换句话说，每个类都应该只承担一种职责。
import io
import sys
from typing import Iterable, TextIO

import requests
from lxml import etree


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


class HNTopPostsSpider:
    '''抓取 Hacker New Top 内容条目

    :param fp:存储抓取结果的目标文件对象
    :param limit: 限制条目数，默认为5
    '''
    items_url = 'https://news.ycombinator.com/'
    file_title = 'Top news on HN'

    def __init__(self, fp: TextIO, limit: int = 5):
        self.fp = fp
        self.limit = limit

    def write_to_file(self):
        '''以纯文本格式将 hacker News Top 内容写入文件'''
        self.fp.write(f'# {self.file_title}\n\n')
        # ❶enumerate()接收第二个参数，表示从这个数开始计数（默认为0）
        for i, post in enumerate(self.fetch(), 1):
            self.fp.write(f'> Top {i}: {post.title}\n')
            self.fp.write(f'> 分数：{post.points} 评论数：{post.comments_cnt}\n')
            self.fp.write(f'> 地址：{post.link}\n')
            self.fp.write('------\n')

    def fetch(self) -> Iterable[Post]:
        ''' 从 Hacker News 抓取 Top 内容

            :return: 可迭代的 Post 对象
            '''
        resp = requests.get(self.items_url)

        # 使用 XPath 可以方便地从页面揭示出需要的内容，以下均为页面解析代码
        html = etree.HTML(resp.text)
        items = html.xpath('//table/tr[@class="athing"]')

        for item in items[:self.limit]:
            node_title = item.xpath('.//span[@class="titleline"]/a')[0]
            node_detail = item.getnext()
            points_text = node_detail.xpath('.//span[@class="score"]/text()')
            comments_text = node_detail.xpath(
                './/span[@class="subline"]/a[last()]/text()')

            yield Post(
                title=node_title.text,
                link=node_title.get('href'),
                # 条目可能会没有评分和评论
                points=points_text[0].split()[0] if points_text else '0',
                comments_cnt=comments_text[0].split(
                )[0] if comments_text else '0',
            )


def main():
    # with open('/tmp/hn_top5.txt') as fp:
    #     crawler = HNTopPostsSpider(fp)
    #     crawler.write_to_file()

    # 因为 HNTopPostSpider接收任何 file-like 对象，所以可以把 sys.stdout 传进去
    # 实现向控制台标准输出打印功能
    crawler = HNTopPostsSpider(sys.stdout)
    crawler.write_to_file()


if __name__ == '__main__':
    main()
