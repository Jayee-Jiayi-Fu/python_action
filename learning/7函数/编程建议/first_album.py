'''通过 iTunes API 搜索歌手发布的第一张专辑'''
# 评价函数好坏还有一个重要标准：函数内的代码是否在同一个抽象层内。
import sys
import requests
from requests.exceptions import HTTPError
from json.decoder import JSONDecodeError
ITUNES_API_EXNPOINT = 'https://itunes.apple.com/search'

def command_first_album():
    '''通过脚本输入查找并打印歌手的第一张专辑信息'''
    # if not len(sys.argv) == 2:
    #     print(f'usage: python {sys.argv[0]} {{SEARCH_TERM}}')
    #     # 当脚本执行异常时，应该使用非0返回码，这是编写脚本的规范之一
    #     sys.exit(1)
    # term = sys.argv[1]

    term = 'linkin+park'
    resp = requests.get(
        ITUNES_API_EXNPOINT,
        {
            'term':term,
            'media':'music',
            'entity':'album',
            'attributes':'artistTerm',
            'limit':200
        }
    )

    try:
        resp.raise_for_status()
    except HTTPError as e:
        print(f'Error: failed to call iTunes API, {e}')
        sys.exit(2)
    try:
        albums = resp.json()['results']
    except JSONDecodeError:
        print(f'Error: response is not valid JSON format')
        sys.exit(2)

    if not albums:
        print(f'Error: no albums found for artist "{term}"')
        sys.exit(1)

    sorted_albums = sorted(albums, key = lambda item:item['releaseDate'])
    first_album = sorted_albums[0]

    # 去除发布日期里的小时与分钟
    release_date = first_album['releaseDate'].split('T')[0]

    # # 打印结果
    print(f"{term}'s first album:")
    print(f" * Name: {first_album['collectionName']}")
    print(f" * Genre: {first_album['primaryGenreName']}")
    print(f" * Released at: {release_date}")

if __name__ ==  '__main__':
    print('Running first_albom >>>')
    command_first_album()

