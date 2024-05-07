# 类型注解是一种给函数参数、返回值以及任何变量增加类型描述的技术，规范的注解可以大大提升代码可读性。

from typing import List
import random


class Duck:
    def __init__(self, color: str):  # ❶给函数参数加上类型注解
        self.color = color

    def quack(self) -> None:  # ❷通过->给返回值加上类型注解
        print(f"Hi, I'm a {self.color} duck!")


# ➌用typing模块的特殊对象List来标注列表成员的具体类型，注意，这里用的是[]符号，而不是()
def create_random_ducks(number: int) -> List[Duck]:
    ducks: List[Duck] = []  # ❹声明变量时，也可以为其加上类型注解
    for _ in number:
        # ❺类型注解是可选的，非常自由，比如这里的color变量就没加类型注解
        color = random.choice(['yellow', 'white', 'gray'])
        ducks.append(Duck(color=color))
    return ducks


'''
typing是类型注解用到的主要模块，除了List以外，该模块内还有许多与类型有关的特殊对象，举例如下。
· Dict：字典类型，例如Dict[str, int]代表键为字符串，值为整型的字典。
· Callable：可调用对象，例如Callable[[str, str], List[str]]表示接收两个字符串作为参数，返回字符串列表的可调用对象。
· TextIO：使用文本协议的类文件类型，相应地，还有二进制类型BinaryIO。
· Any：代表任何类型。


默认情况下，你可以把Python里的类型注解当成一种用于提升代码可读性的特殊注释，因为它就像注释一样，只提升代码的说明性，不会对程序的执行过程产生任何实际影响。

但是，如果引入静态类型检查工具，类型注解就不再仅仅是注解了。它在提升可读性之余，还能对程序正确性产生积极的影响。在13.1.5节中，我会介绍如何用mypy来做到这一点

如果你想了解更多内容，可以查看Python官方文档的“类型注解”部分，里面的内容相当详
'''
