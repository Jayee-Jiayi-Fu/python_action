# __get__描述符
class InfoDescriptor:
    """打印帮助信息的描述符"""

    def __get__(self, instance, owner=None):
        print(f"Calling __get__, instance: {instance}, owner: {owner}")
        if not instance:
            print("Calling without instance...")
            return self
        return "informative descriptor"

    def __set__(self, instance, value):
        print(f"Calling __set__, instance: {instance}, value: {value}")

    def __delete__(self, instance):
        print(f"Calling __delete__, instance: {instance}")


class Foo:
    bar = InfoDescriptor()


# Foo.bar
# Foo().bar
# Foo.bar = None
# Foo().bar = 42
# del Foo().bar


class IntegerField:
    """整形字段，只允许一定范围的整数

    :param min_value: 允许的最小值
    :param max_value: 允许的最大值
    """

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        # 将绑定属性名保存在描述符对象中
        # 对与 age = IntegerField(...)来说，此处name就是“age”
        self._name = name

    def __get__(self, instance, owner=None):
        # 当不是通过实例访问时，直接返回描述符对象
        if not instance:
            return self
        # 返回保存在实例字典里的值
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        # 校验后将值保存在字典里
        value = self._validate_value(value)
        instance.__dict__[self._name] = value

    def _validate_value(self, value):
        """校验值是否为符合要求的整数"""
        try:
            value = int(value)
        except (TypeError, ValueError):
            raise ValueError("value is not a valid integer! ")
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(
                f"value must between {self.min_value} and {self.max_value}"
            )
        return value


class Person:
    age = IntegerField(min_value=0, max_value=150)

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Jayee", 1)
p2 = Person("Tom", 2)
print(p1.age, p2.age, p1.age == p2.age)
