from collections import defaultdict
from collections.abc import MutableMapping
from enum import Enum

# 知识点1
# defaultdict(default_factory,...)
# 若d[key]访问的 key不存在，defaultdict对象会自动调用default_factory()
# 并将结果作为值保存在对应的key里


# 知识点2

class PagePerfLevel(str, Enum):
    LT_100 = 'less_than_100ms'
    LT_300 = 'between_100_and_300ms'
    LT_1000 = 'between_300_and_1s'
    GT_1000 = 'greater_than_1s'


class PerfLevelDict(MutableMapping):
    '''存储响应时间性能等级的字典'''

    def __init__(self):
        self.data = defaultdict(int)

    def __getitem__(self, key):
        # 当某个性能等级不存在，默认返回0
        return self.data[self.compute_level(key)]

    def __setitem__(self, key, value):
        # 将key转为对应的性能等级，然后设置值
        self.data[self.compute_level(key)] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def total_request(self):
        '''返回请求总数'''
        return sum(self.values())

    def items(self):
        '''按照PagePerfLevel的循序返回性能等级数据'''
        return sorted(self.data.items(),
                      key=lambda pair: list(PagePerfLevel).index(pair[0]))

    @staticmethod
    def compute_level(time_cost_str):

        # 传入性能等级直接返回，如'less_than_100ms'
        if time_cost_str in list(PagePerfLevel):
            return time_cost_str

        '''根据响应时间计算性能等级'''
        time_cost = int(time_cost_str)
        if time_cost < 100:
            return PagePerfLevel.LT_100
        elif time_cost < 300:
            return PagePerfLevel.LT_300
        elif time_cost < 1000:
            return PagePerfLevel.LT_1000
        return PagePerfLevel.GT_1000


def analyzer_v3():
    path_groups = defaultdict(PerfLevelDict)

    with open('logs.txt', 'r',) as fp:
        for line in fp:
            path, time_cost_str = line.strip().split()
            path_groups[path][time_cost_str] += 1

    for path, result in path_groups.items():
        print(f' == Path: {path}')
        print(f'    Total request: {result.total_request()}')
        print(f'    Performance:')
        for level_name, count in result.items():
            print(f'    - {level_name}: {count}')


analyzer_v3()
