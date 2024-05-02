
# 03. 抽象类的子类化机制
class Validator(ABC):  # ❶要定义一个抽象类，需要继承ABC类或使用abc.ABCMeta元类
    '''校验器抽象类'''
    @classmethod
    def __subclasshook__(cls, C):
        print(f'Running __subclasshook__： 实例所属类型会作为参数传入该方法: {C}')
        '''任何提供了 validate 方法的类，都被当做 Validator 的子类'''
        # ❷C.__mro__代表C的类派生路线上的所有类
        if any('validate' in B.__dict__ for B in C.__mro__):
            return True
        return NotImplemented

    def validate(self, value):
        raise NotImplementedError


# 上面代码的重点是__subclasshook__类方法。__subclasshook__是抽象类的一个特殊方法，
# 当你使用isinstance检查对象是否属于某个抽象类时，如果后者定义了这个方法，那么该方法就会被触发，然后：
# · 实例所属类型会作为参数传入该方法（上面代码中的C参数）；
# · 如果方法返回了布尔值，该值表示实例类型是否属于抽象类的子类；
# · 如果方法返回NotImplemented，本次调用会被忽略，继续进行正常的子类判断逻辑。

# 在我编写的Validator类中，__subclasshook__方法的逻辑是：所有实现了validate方法的类都是我的子类。
# 实例所属类型会作为参数传入该方法
class StringValidator:
    def validate(self, value):
        pass


print(isinstance(StringValidator(), Validator))


# 通过__subclasshook__类方法，我们可以定制抽象类的子类判断逻辑。
# 这种子类化形式只关心结构，不关心真实继承关系，所以常被称为“结构化子类”。
# 这也是之前的ThreeFactory类能通过Iterable类型校验的原因，因为Iterable抽象类对子类只有一个要求：实现了__iter__方法即可。


# 除了通过__subclasshook__类方法来定义动态的子类检查逻辑外，你还可以为抽象类手动注册新的子类。
# 比如，下面的Foo是一个没有实现任何方法的空类，但假如通过调用抽象类Validator的register方法，我们可以马上将它变成Validator的“子类”：
class Foo:
    pass


print('before regist, isinstance(Foo, Validator): ', isinstance(Foo, Validator))

Validator.register(Foo)
Validator.register(Foo)
print('after regist, isinstance(Foo(), Validator): ',
      isinstance(Foo(), Validator))
print('after regist, issubclass(Foo, Validator): ', issubclass(Foo, Validator))


# 总结一下，抽象类通过__subclasshook__钩子和.register()方法，
# 实现了一种比继承更灵活、更松散的子类化机制，并以此改变了isinstance()的行为。
# 有了抽象类以后，我们便可以使用isinstance(obj, type)来进行鸭子类型编程风格的类型校验了。
# 只要待匹配类型type是抽象类，类型检查就符合鸭子类型编程风格——只校验行为，不校验类型。
