'''通过 iTunes API 搜索歌手发布的第一张专辑'''
# 评价函数好坏还有一个重要标准：函数内的代码是否在同一个抽象层内。
import sys
import requests
from requests.exceptions import HTTPError
from json.decoder import JSONDecodeError
ITUNES_API_EXNPOINT = 'https://itunes.apple.com/search'


class GetFirstAlbumError(Exception):
    '''获取第一张专辑失败'''


class QueryAlbumsError(Exception):
    ''' 获取专辑列表失败 '''


def command_first_album():
    '''通过输入参数查找并打印歌手的第一张专辑'''
    if not len(sys.argv) == 2:
        print(f'usage: python {sys.argv[0]} {{SEARCH_TERM}}')
        sys.exit(1)

    artist = sys.argv[1]

    try:
        album = get_first_album(artist)
    except GetFirstAlbumError as e:
        print(f'error: { e }', file=sys.stderr)
        sys.exit(2)

    # # 打印结果
    print(f"{artist}'s first album:")
    print(f" * Name: {album['name']}")
    print(f" * Genre: {album['genre_name']}")
    print(f" * Released at: {album['release_name']}")


def get_first_album(artist):
    '''根据专辑列表获取第一张专辑
    Args:
        artist (String): 歌手名称

    Returns:
        [Dict]: 第一张专辑

    Raises:
        GetFirstAlbumError: 获取失败时抛出
    '''
    try:
        albums = query_all_albums(artist)
    except QueryAlbumsError as e:
        raise GetFirstAlbumError(e)

    sorted_albums = sorted(albums, key=lambda item: item['releaseDate'])
    first_album = sorted_albums[0]

    # 去除发布日期里的小时与分钟
    release_date = first_album['releaseDate'].split('T')[0]

    return {
        'name': first_album['collectionName'],
        'genre_name': first_album['primaryGenreName'],
        'release_date': release_date,
    }


def query_all_albums(artist):
    '''根据歌手名字搜索所有专辑列表
    Args:
        artist (String): 歌手名字

    Returns:
        [List(Dict)]: 专辑列表，

    Raises:
        QueryAlbumsError: 获取专辑失败时抛出
    '''
    resp = requests.get(
        ITUNES_API_EXNPOINT,
        {
            'term': artist,
            'media': 'music',
            'entity': 'album',
            'attributes': 'artistTerm',
            'limit': 200
        }
    )

    try:
        resp.raise_for_status()
    except HTTPError as e:
        raise QueryAlbumsError(f'Error: failed to call iTunes API, {e}')

    try:
        albums = resp.json()['results']
    except JSONDecodeError as e:
        raise QueryAlbumsError(f'Error: response is not valid JSON format {e}')

    if not albums:
        raise QueryAlbumsError(f'Error: no albums found for artist "{artist}"')

    return albums


if __name__ == '__main__':
    print('Running first_albom >>>')
    command_first_album()
