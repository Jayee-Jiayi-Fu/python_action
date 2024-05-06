# 1. 定义类的私有属性：属性名前加双下划线
class Duck:
    def __init__(self):
        self.__name = 'Tom'


# 直接从外部调用会报错
duck = Duck()

try:
    print(duck.__name)
except AttributeError as e:
    print(e)  # 'Duck' object has no attribute '__name'


# 遇到双下划线属性__{var} ，Python进行了重写 _{class}__{var}
print(duck._Duck__name)  # Tom


# 私有属性的这套机制最大的用途，是在父类中定义一个「不容易」被子类重写的受保护属性。在需要的时候仍然能修改它。所以其实它是一个“君子协定”
# 但是实际开发过程中，极少会使用标准的双下划线。如果仅仅想要标示“私有属性”，可以使用单下划线。“大家都是成年人”，“让程序员做正确的事”
