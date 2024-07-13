# SRP认为：一个类应该仅有一个被修改的理由。换句话说，每个类都应该只承担一种职责。
# 要令脚本符合SRP，最传统的就是把大类拆分为小类。
import sys
from typing import Iterable, TextIO, Optional, List

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


class HNTopPostsSpider:
    '''抓取 Hacker New Top 内容条目

    :param fp:存储抓取结果的目标文件对象
    :param limit: 限制条目数，默认为5
    '''
    items_url = 'https://news.ycombinator.com/'
    file_title = 'Top news on HN'

    def __init__(self, limit: int = 5):
        self.limit = limit

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


'''
这样修改以后，HNTopPostsSpider和PostsWriter类都符合了SRP。这两个类各自的修改可以单独进行而不会相互影响。
只有当解析逻辑变化时，我才会修改HNTopPostsSpider类。
同样，修改PostsWriter类的理由也只有调整输出格式一种。


最后，由于现在两个类各自只负责一件事，需要一个新角色把它们的工作串联起来，因此我实现了一个新的函数get_hn_top_posts()：
函数同样可以做到“单一职责”
单一职责是面向对象领域的设计原则，通常用来形容类。
而在Python中，单一职责的适用范围不限于类——通过定义函数，我们同样能让上面的代码符合单一职责原则。
'''

# 某个职责拆分为新函数是一个具有Python特色的解决方案。它虽然没有那么“面向对象”，却非常实用，甚至在许多场景下比编写类更简单、更高效。


def get_hn_top_posts(fp: Optional[TextIO] = None):
    """获取 Hacker News Top 内容，并将其写入文件中

    :param fp: 需要写入的文件，如未提供，将向标准输出打印
    """
    dest_fp = fp or sys.stdout
    crawler = HNTopPostsSpider()
    writer = PostsWriter(dest_fp, title='Top news on HN')
    writer.write(list(crawler.fetch()))


def main():
    # with open('/tmp/hn_top5.txt') as fp:
    #     get_hn_top_posts（fp)

    # 实现向控制台标准输出打印功能
    get_hn_top_posts()


if __name__ == '__main__':
    main()
