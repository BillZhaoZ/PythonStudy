# Python学习  一江夜雨  2018
import calendar
import time
import datetime

# 计算运行时间
start_time = datetime.datetime.now()
time.sleep(0.11111)
end_time = datetime.datetime.now()

print((end_time - start_time).seconds)

# 计算10天之后的日期
d1 = datetime.datetime.now()
d2 = d1 + datetime.timedelta(days=10)

print(d2)
print(d2.ctime())

# Seconds
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970: ", ticks)

# Python时间函数将时间处理为9个数字的元组
localtime = time.localtime(time.time())
print("Local current time :", localtime)

# 当前时间
curtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(curtime)

# 获取一个月的日历
cal = calendar.month(2018, 1)
print("Here is the calendar:")
print(cal)
