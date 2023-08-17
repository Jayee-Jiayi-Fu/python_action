# 对捕获异常的正确思考：
# 在代码中捕获异常，表面上是避免程序因为异常发生而直接崩溃，
# 但它的核心，其实是编码者对处于程序主流程之外的、已知或未知情况的一种妥当处置。而「妥当」这个词正是异常处理的关键。
# 弄一个庞大的try语句，把所有可能出错、不可能出错的代码，一股脑儿地全部用except Exception：包起来，显然是不妥当的。


# 精准捕获包括：
# · 永远只捕获那些可能会抛出异常的语句块；
# · 尽量只捕获精确的异常类型，而不是模糊的Exception；
# · 如果出现了预期外的异常，让程序早点儿崩溃也未必是件坏事


import re
import requests
from requests.exceptions import RequestException


def save_website_title(url, filename):
    '''获取某个地址的网页标题，然后写入文件中
    :return: 如果成功报错，返回True；否则打印错误并返回False
    '''

    # 抓取页面
    try:
        resp = requests.get(url)
    except RequestException as e:
        print(f'save failed: unable to get page content:{e}')
        return False

    # 获取标题
    obj = re.search(r'<title>(.*)</title>', resp.text)
    if not obj:
        print('save failed: title tag not in page content')
        return False
    title = obj.group(1)

    # 保存文件
    try:
        with open(filename,'w') as fp:
            fp.write(title)
    except IOError as e:
        print(f'save failed: unable to write to file {filename}: {e}')
        return False
    else:
        return True


def main():
    save_website_title('https://www.qq.com', 'qq_title.txt')


if __name__ =='__main__':
    main()
