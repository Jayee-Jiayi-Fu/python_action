class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        # 设置年龄，只允许 0~150岁
        try:
            value = int(value)
        except (TypeError, ValueError):
            raise ValueError("value is not a valid interger!")
        if not (0 < value < 150):
            raise ValueError("value must between 0 and 150")
        self._age = value


# p = Person('Jayee', 'invalid_age')
# p = Person('Jayee', 150)
p = Person("Jayee", 18)
print(p.age)
