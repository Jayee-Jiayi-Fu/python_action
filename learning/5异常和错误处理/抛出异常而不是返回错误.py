# 返回错误并非解决此类问题的最佳办法。这是因为这种做法会增加调用方处理错误的成本
# Python有完善的异常机制，并且在某种程度上鼓励我们使用异常。所以，用异常来进行错误处理才是更地道的做法。

# 1. 引入自定义异常类

class CreateItemError(Exception):
    '''创建 Item 失败'''

# · 新函数拥有更稳定的返回值类型，它永远只会返回Item类型或是抛出异常。
# · 虽然我们鼓励使用异常，但异常总是会不可避免地让人“感到惊讶”，所以，最好在函数文档里说明可能抛出的异常类型。
def create_item(name):
    '''创建一个新的item
    ：raises：当无法创建时抛出 CreateItemError
    '''
    if len(name) > MAX_LENGTH_OF NAME:
         raise CreateItemError('name of item is too long')
    if len(get_current_items()) > MAX_ITEMS_QUOTA:
         raise CreateItemError('items is full')
    return Item(name = name)


# · 不同于返回值，异常在被捕获前会不断往调用栈上层汇报。
# 因此create_item()的直接调用方也可以完全不处理CreateItemError，而交由更上层处理。
# 异常的这个特点给了我们更多灵活性，但同时也带来了更大的风险:
# 具体来说，假如程序缺少一个顶级的统一异常处理逻辑，那么某个被所有人忽视了的异常可能会层层上报，最终弄垮整个程序。
def create_from_input():
    name = input()
    try:
        item = create_item(name)
    except CreateItemError as e:
        print(f'create item is failed: {e}')
    else:
        print(f'item<{name}> created')


