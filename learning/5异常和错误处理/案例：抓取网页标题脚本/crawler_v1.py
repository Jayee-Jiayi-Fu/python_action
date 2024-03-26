import requests
import re


def save_website_title(url, filename):
    '''获取某个地址的网页标题，然后写入文件中
    :return: 如果成功报错，返回True；否则打印错误并返回False
    '''
    try:
        resp = requests.get(url)
        obj = re.search(r'<title>(.*)</title>', resp.text)

        if not obj:
            print('save failed: title tag not in page content')
            return False

        # 注意：这里的函数写错了，应该是group，隐蔽性很强
        title = obj.grop(1)
        with open(filename, 'w') as fp:
            fp.write(title)
            return True

    except Exception:
        print(f'save failed: unable to save title of {url} to {filename}')
        print(Exception)
        return False


def main():
    save_website_title('https://www.qq.com', 'qq_title.txt')


if __name__ == '__main__':
    main()
