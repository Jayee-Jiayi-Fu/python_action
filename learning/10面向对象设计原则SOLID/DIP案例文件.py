from DIP依赖倒置原则 import SiteSourceGrouper, LocalHNWebPage
from collections import Counter


def test_grouper_returning_valid_type():
    # 测试 get_groups 是否返回了正确的类型
    page = LocalHNWebPage(page="./static_hn.html")
    grouper = SiteSourceGrouper(page)
    result = grouper.get_groups()
    assert isinstance(result, Counter, "groups  should be Counter isinstance")
