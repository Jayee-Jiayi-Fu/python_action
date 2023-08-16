# 1. try/except 基础语法
# 当某类异常被抛出，将执行对应except下的语句
# 一个try可对应多个except
# finally 语句中的代码无论如何都会执行，哪怕已经执行了return
def safe_int(value):
     try:
         return int(value)
     except TypeError:
         print(f'type error: { type(value) } is invalid')
     except ValueError:
         print(f'value eror: {value} is invalid')
     finally:
         print('function completd')


# 2. 把更精确的except语句放在前面
# except 可捕获SomeError类型的所有派生类
# 内置异常类之间存在许多继承关系，例如：BaseException（一切异常类的父类） → Exception → LookupError →KeyError。
# 异常匹配会按照从上而下的顺序进行。若比较模糊的父类异常放在前面，就会导致在下面的except永远不会被触发
def incr_by_key(d, key):
    try:
        d[key] += 1
    except Exception as e:
        print('捕获到 KeyError 时，会先执行')
    except KeyError:
        print('KeyError 已经在')



# 2. 使用else分支
# 在用try捕获异常时，有时程序需要仅在一切正常时做某件事。为了做到这一点，我们常常需要在代码里设置一个专用的标记变量。
# 异常捕获语句里的else表示：仅当try语句块里没抛出任何异常时，才执行else分支下的内容，效果就像在try最后增加一个标记变量一样。
# 和finally语句不同，假如程序在执行try代码块时碰到了return或break等跳转语句，中断了本次异常捕获，那么即便代码没抛出任何异常，else分支内的逻辑也不会被执行

# 之前一般做法
'''
sync_succeeded = False
try:
    sync_profile(user.profile, to_external = True)
    sync_succeeded = True
except Exception as e:
    print(e)
if sync_succeeded:
    do something with no error happened
'''

# 使用else写法(当成then更好理解)
'''
try: 
    sync_prifile(user.profile, to_external=True)
except Exception as e:
    print(e)
else:
    do something with no error happened
'''


# 3. 空raise语句
# 空raise语句出现在except块里时，它会原封不动地重新抛出当前异常
def incr_by_key(d, key):
    try:
        d[key] += 1
    except KeyError:
        print(f'key {key} does not exists, re-raise the exception')
        raise