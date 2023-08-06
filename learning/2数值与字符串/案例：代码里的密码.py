from enum import Enum


# 源代码
def add_daily_points(user):
    '''用户每天完成第一次登录后，为其增加积分'''
    if user.type == 13:
        return
    if user.type == 3:
        user.points += 120
        return
    user.points += 100
    return


# 重构
# 用户每日奖励积分数
DAILY_POINTS = 100
# VIP 用户每日额外奖励积分数
VIP_EXTRA_POINTS = 20


# 用户类型
# 把数字字面量改成常量和枚举类型后，我们就能很好地规避输入错误问题
class UserType(int, Enum):
    # VIP 用户
    VIP = 3
    # 封禁用户
    BANDED = 13


def refactor_add_daily_points(user):
    '''用户每天完成第一次登录后，为其增加积分'''
    if user.type == UserType.BANDED:
        return

    if user.type == UserType.VIP:
        user.point += DAILY_POINTS + VIP_EXTRA_POINTS
        return

    user.point += DAILY_POINTS

    return





