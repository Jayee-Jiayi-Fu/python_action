# 在一个类里，属性和方法有着不同的职责：属性代表状态，方法代表行为。
# 二者对外的访问接口也不一样，属性可以通过inst.attr的方式直接访问，而方法需要通过inst.method()来调用。

# @property装饰器模糊了属性和方法间的界限，使用它，你可以把方法通过属性的方式暴露出来
import os


class FilePath:
    def __init__(self, path):
        self.path = path

    def get_basename(self):
        '''获取文件名'''
        return self.path.split(os.sep)[-1]

    @property  # @property装饰器定义属性的读取逻辑,把上面的get_basename()方法变成一个虚拟属性
    def basename(self):
        '''获取文件名'''
        return self.path.split(os.sep)[-1]

    # ❶经过@property装饰，basename已经变成了property对象，

    # @property 自定义写入逻辑：
    @basename.setter
    def basename(self, name):  # ❷定义setter方法，该方法会在对属性赋值时被调用
        '''修改当前路径里的文件名部分'''
        new_path = self.path.split(os.sep)[:-1] + [name]
        self.path = os.sep.join(new_path)

    # @property 自定义删除逻辑：
    @basename.deleter
    def basename(self):  # ❸定义deleter方法，该方法会在删除属性时被调用
        raise RuntimeError('Cannot deleter basename')


f = FilePath('/worspack/python_action/learn.py')
print(f.get_basename())
print(f.basename)
f.basename = 'hello.txt'
print(f.path)
del f.basename


# @property是个非常有用的装饰器，它让我们可以基于方法定义类属性，精确地控制属性的读取、赋值和删除行为，灵活地实现动态属性等功能。
'''
当你决定把某个方法改成属性后，它的使用接口就会发生很大的变化。你需要学会判断，方法和属性分别适合什么样的场景。
举个例子，假如你的类有个方法叫get_latest_items()，调用它会请求外部服务的数十个接口，耗费5～10秒钟。
那么这时，盲目把这个方法改成.latest_items属性就不太恰当。
人们在读取属性时，总是期望能迅速拿到结果，调用方法则不一样——快点儿慢点儿都无所谓。让自己设计的接口符合他人的使用预期，也是写代码时很重要的一环。
'''
