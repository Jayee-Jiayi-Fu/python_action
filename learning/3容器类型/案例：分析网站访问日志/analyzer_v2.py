from enum import Enum
from textwrap import dedent

class PagePerfLevel(str, Enum):
    LT_100 = 'less_than_100ms'
    LT_300 = 'between_100_and_300ms'
    LT_1000 = 'between_300_and_1s'
    GT_1000 = 'greater_than_1s'

class PathPerformance:
    def __init__(self,):
        self.total = 0
        self.performance = {}

        for item in PagePerfLevel:
            self.performance[item.value] = 0

    def cal_level(self,time_str):
        time_int = int(time_str)

        if time_int < 100:
            level = PagePerfLevel.LT_100
        elif time_int < 300:
            level = PagePerfLevel.LT_300
        elif time_int < 1000:
            level = PagePerfLevel.LT_1000
        else:
            level = PagePerfLevel.GT_1000

        return level

    def add_record(self, time_str):
        self.total += 1
        level = self.cal_level(time_str)
        self.performance[level] += 1


def analyzer():
    path_dict = {}

    with open('./logs.txt', 'r') as f:
        for line in f.readlines():
          (path, time_str) = line.strip().split()
          path_dict.setdefault(path, PathPerformance()).add_record(time_str)

    print(path_dict)

analyzer()

