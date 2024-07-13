class DeactivationNotSupported(Exception):
    '''当用户不支持停用时抛出'''


class User(Model):
    '''
    用户类，包含普通用户相关操作

    :raises: 当用户不支持停用时，抛出 DeactivationNotSupported 异常
    '''

    def deactive(self):
        '''停用当前用户'''
        self.is_active = False
        self.save()

    def list_related_posts(self) -> List[int]:
        '''查询所有预支相关的帖子ID'''
        return [post.id
                for post in session.query(Post).fillter(username=self.username)]


class Admin(User):
    '''管理员用户类'''

    def deactive(self):
        # raise RuntimeError('Admin can not be deactive')

        # 更优做法
        ''' 增加抛出异常相关说明 '''
        raise DeactivationNotSupported('Admin can not be deactive')

    def list_related_posts(self) -> Iterable[int]:
        # 管理员与所有帖子都有关，为了节约内存，使用生成器放着结果

        for post in session.query(Post).all():
            yield post.id


# 问题1：子类随意抛出异常
class VIPUser(User):
    def deactive(self):

        raise RuntimeError('VIPUser can not be deactive')


def deactive_users(users: Iterable[User]):
    ''' 批量停用多个用户

    :param users: 可迭代的用户对象 User
    '''
    for user in users:

        # 不好的解决方法：增加类型判断
        # 有新的类型不支持停用，就要不断增加判断
        # 同时不满足 OCP 原则
        if isinstance(user, (Admin, VIPUser)):
            logger.info(f'skip deactive admin user {user.username}')
            continue
        user.deactive()


def deactive_users(users: Iterable[User]):
    '''批量停用多个用户'''
    for user in users:
        try:
            user.deactive()
        except DeactivationNotSupported:
            logger.info(f'user {user.username} does not allow deactiving, skip.')


def get_user_posts_count(user: User) -> int:
    return len(user.list_related_posts())


# 场景3：
class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value

    def get_area(self) -> int:
        """返回当前长方形的面积"""
        return self.width * self.height


class Square(Rectangle):
    """正方形

    :param length: 边长
    """

    def __init__(self, length: int): ➊
    self._width = length
    self._height = length

    @property
    def width(self):
        return super().width

    @width.setter
    def width(self, value: int): ➋
    self._width = value
    self._height = value

    @property
    def height(self):
        return super().height

    @height.setter
    def height(self, value: int):
        self._width = value
        self._height = value


def test_rectangle_get_area(r: Rectangle):
    r.width = 3
    r.height = 5
    # 传入一个正方形对象Square，会发现它根本无法通过这个测试
    assert r.get_area() == 15
