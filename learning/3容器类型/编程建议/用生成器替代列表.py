# 一个可能很耗时的处理函数
def foo(data):
    pass

# 若函数遵循同一种模式：“初始化结果容器→处理→将结果存入容器→返回容器”
# 它有两个问题：
# 一、如果需要处理的对象items过大，每次执行都特别慢，存放结果的对象results也会占用大量内存
# 二、如果函数调用方想在某个processed_item对象满足特定条件时中断，不再继续处理后面的对象，现在的batch_process()函数也做不到——它每次都得一次性处理完所有items才会返回。
def batch_process(items):
    results = []
    for item in items:
        # 处理 item， 可能需要消耗大量时间
        processed_item = foo(item)
        results.append(processed_item)

# 可以用生成器函数来改写它。简单来说，就是用yield item替代append语
def batch_process_better(items):
    for item in items:
        processed_item = foo(item)
        yield processed_item