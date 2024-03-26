import time
date = "2023-08-14 16:58:32"

# strptime() 函数根据指定的格式把一个时间字符串解析为时间元组。
date_array = time.strptime(date, "%Y-%m-%d %H:%M:%S")

# 2、将上面的时间元组转化为时间戳
timestamp = int(time.mktime(date_array))

print(timestamp)
