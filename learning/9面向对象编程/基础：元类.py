# 元类是Python中的一种特殊对象。
# 元类控制着类的创建行为，就像普通类控制着实例的创建行为一样。
# type是Python中最基本的元类，利用type，你根本不需要手动编写class ... :代码来创建一个类——直接调用type()就行：

import types
import time
Foo = type('Foo', (), {'bar': 3})
print(Foo, Foo.bar, Foo.mro())


# ❶参数分别为type(name, bases, attrs)
# 在调用type()创建类时，需要提供三个参数，它们的含义如下。

# （1） name：str，需要创建的类名
# （2） bases：Tuple[Type]，包含其他类的元组，代表类的所有基类。
# （3） attrs：Dict[str, Any]，包含所有类成员（属性、方法）的字典。


# 虽然type是最基本的元类，但在实际编程中使用它的场景其实比较少。
# 更多情况下，我们会创建一个继承type的新元类，然后在里面定制一些与创建类有关的行为。


# class AutoPropertyMeta(tyep):
#     '''元类
#        - 把所有类方法变成动态属性
#        - 为所有示例增加创建时间属性
#     '''
#     def __new__(cls, name, bases, attrs):
#         for key, value in attrs.items():
#             if isinstance(value, types.FunctionType) and not key.startwith('_'):
#                 attrs[key] = property(value)
#             return super().__new__(cls, name, bases, attrs)

#     def __call__(cls, *args, **kwargs):
#         inst = super(), __call__(*args, **kwargs)
#         inst.created_at = time.time()
#         return inst


class AutoPropertyMeta(type):
    """元类：
    - 把所有类方法变成动态属性
    - 为所有实例增加创建时间属性
    """
    def __new__(cls, name, bases, attrs):
       for key, value in attrs.items():
            if isinstance(value, types.FunctionType) and not key.startswith('_'):
                attrs[key] = property(value)
        return super().__new__(cls, name, bases, attrs) 

    def __call__(cls, *args, **kwargs): 
       inst = super().__call__(*args, **kwargs)
        inst.created_at = time.time()
        return inst
