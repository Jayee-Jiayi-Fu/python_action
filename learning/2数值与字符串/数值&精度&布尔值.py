from decimal import Decimal

# 三种内置数值类型：整型（int）、浮点型（float）和复数类型（complex）
score = 100
temp = 37.5
com = 1 + 2j

# 相互转化
int(temp)
float(score)

# 如果数字特别长，可以通过插入_分隔符来让它变得更易读：
i = 1_000_000
i = i + 10


# 浮点数精度问题
# 由于Python使用“双精度”，导致计算小数时出现精度损失
# k = 0.30000000000000004
k = 0.1 + 0.2
# 内置模块：decimal，使用decimal.Decimal对象来替代普通浮点数，解决精度丢失问题
# 注意：必须使用字符串来表示数字。如果使用普通浮点数，在转换为Decimal对象前就会损失精度，掉进所谓的“浮点数陷阱”
Decimal('0.1') + Decimal('0.2')
Decimal('0.3')


# 布尔值其实也是数字
# 布尔类型是整型的子类型，在绝大多数情况下，True和False可直接当作 1 和 0 使用
int(True)
int(False)
n = True + 1
# 布尔值的这个特点，最常用来简化统计总数操作。
# 假设有一个包含整数的列表，我需要计算列表里一共有多少个偶数。
numbers = [1, 2, 4, 5, 7]
count = sum(i % 2 == 0 for i in numbers)
