# __get__描述符
class InfoDescriptor:
    """打印帮助信息的描述符"""

    #
    def __get__(self, instance, owner=None):
        print(f'Calling __get__, instance: {instance}, owner: {owner}')
        if not instance:
            print('Calling without instance...')
            return self
        return 'informative descriptor'


class Foo:
    bar = InfoDescriptor()

class IntegerField:
    """ 整型字段，只允许一定范围的整数

    :param min_value: 允许的最小值
    :param max_value: 允许的最大值
    """
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __get__(self, instance, owner = None):
        # 当不是通过实例访问时，直接返回描述符对象
        if not instance:
            return self
        # 返回保存在实例字典里的值
        return instance.__dict__['__interger_field']


