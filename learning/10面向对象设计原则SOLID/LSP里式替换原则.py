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
