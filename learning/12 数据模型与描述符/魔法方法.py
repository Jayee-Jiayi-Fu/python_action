
# __str__
class Person:
    """docstring for Person

    :param name:姓名
    """

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        return self.name

    def __repr__(self):
        return '自定义：{cls_name}(name={name!r}, age={age!r},color={color!r})'.format(
            cls_name=self.__class__.__name__,
            name=self.name,
            age=self.age,
            color=self.color)

    def __format__(self, format_spec):
        if format_spec == 'verbose':
            return f'{self.name}({self.age})[{self.color}]'

        elif format_spec == 'simple':
            return f'{self.name}({self.age})'

        return self.name


p = Person('Jayee', 31, 'red')
print(Person)
print(p)

print(repr(Person))
print(repr(p))

print('{p:verbose}'.format(p=p))
print(f'{p:simple}')
print(f'{p}')
