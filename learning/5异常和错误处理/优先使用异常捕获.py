# 1. 优先使用异常捕获
# 两种编程风格：
# - LBYL（look before you leap）：在执行一个可能会出错的操作时，先做一些关键的条件判断，仅当条件满足时才进行操作
# - EAFP（easier to ask for forgiveness than permission），不做任何事前检查，直接执行操作，但在外层用try来捕获可能发生的异常
# EAFP风格更受社区偏爱，因为它更简单直接，总是直奔主流程而去，把意外情况都放在异常处理try/except块内消化掉。可读性更高
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
