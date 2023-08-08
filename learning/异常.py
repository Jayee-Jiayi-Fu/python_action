# 1. 优先使用异常捕获
# 和LBYL风格相比，EAFP风格更受社区偏爱，因为它更简单直接，可读性更高
# 另一个重要原因：在Python里抛出和捕获异常是很轻量的操作，即使大量抛出、捕获异常，也不会给程序带来过多额外负担。
def incr_by_one(value):
    try:
        value = int(value) + 1
        return value

    except (TypeError, ValueError) as e:
        print(f'Unable to perform incr for value: "{value}", error: {e}')
    except Exception as e:
        print('更高级的error')
    finally:
        print('不管是否抛出异常，或者执行了return语句，都始终会执行')


# 常用知识点:
# 1. 把更精确的except语句放在前面
# except 可捕获SomeError类型的所有派生类
# 内置异常类之间存在许多继承关系，例如：BaseException（一切异常类的父类） → Exception → LookupError →KeyError。
# 异常匹配会按照从上而下的顺序进行。若比较模糊的父类异常放在前面，就会导致在下面的except永远不会被触发


# 2. 使用else分支
#
if __name__ == "__main__":
    while(1):
        print('Please input the value:')
        input_value = input()
        print(incr_by_one(input_value))