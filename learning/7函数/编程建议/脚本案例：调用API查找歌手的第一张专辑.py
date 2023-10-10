'''通过 iTunes API 搜索歌手发布的第一张专辑'''
import sys


def command_first_album():
    '''通过脚本输入查找并打印歌手的第一张专辑信息'''
    if not len(sys.argv) == 2:
        print(f'usage: python {sys.argv[0]}')

if __name__ ==  '__main__':
    command_first_album()

