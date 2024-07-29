import random
import string

import pytest


@pytest.fixture
def random_token() -> str:
    """生成随机 token"""
    token_l = []
    char_pool = string.ascii_lowercase + string.digits
    for _ in range(32):
        token_l.append(random.choice(char_pool))
    return "".join(token_l)


# @pytest.fixture(autouse=True)
# def prepare_data():
#     # 在测试开始前，创建两个用户
#     User.objects.create(...)
#     User.objects.create(...)
#     yield
#     # 在测试结束时，销毁所有用户
#     User.objects.all().delete()
