
<<<<<<< HEAD
import process
'''

=======
'''
>>>>>>> parent of f8e5a89 (提交到第七章)
函数会在执行结束时通知管理员。为了在不同情况（有或没有“pending”状态的任务）下发送不同通知，函数在循环开始前定义了一个标记变量non_pending_found。
'''


<<<<<<< HEAD
def notify_admin():
    pass


=======
>>>>>>> parent of f8e5a89 (提交到第七章)
def process_tasks(tasks):
    """批量处理任务，如果遇到状态不为 pending 的任务，则中止本次处理"""
    non_pending_found = False
    for task in tasks:
        if not task.is_pending():
            non_pending_found = True
            break
        process(task)

    if non_pending_found:
        notify_admin('Found non-pending task, processing aborted.')
    else:
        notify_admin('All tasks was processed.')


'''
假如利用循环语句的else分支，这份代码可缩减成下面这样
for循环（和while循环）后的else关键字，代表如果循环正常结束（没有碰到任何break），便执行该分支内的语句
'''


def process_tasks(tasks):
    """批量处理任务，如果遇到状态不为 pending 的任务，则中止本次处理"""
    for task in tasks:
        if not task.is_pending():
            notify_admin('Found non-pending task, processing aborted.')
            break
        process(task)
    else:
        notify_admin('All tasks was processed.')


def process_tasks(tasks):
    """批量处理任务并将结果通知管理员"""
    if _process_tasks(tasks):
        notify_admin('All tasks was processed.')
    else:
        notify_admin('Found non-pending task, processing aborted.')


'''
用“拆分子函数”的技巧来重构它。通过把循环结构拆分为一个独立函数，完全避免“使用标记变量还是else分支”的艰难抉择
'''


def _process_tasks(tasks):
    """批量处理任务，如果遇到状态不为 pending 的任务，则中止本次处理

    :return: 是否完全处理所有任务
    :rtype: bool
    """
    for task in tasks:
        if not task.is_pending():
            return False
        process(task)
    return True
