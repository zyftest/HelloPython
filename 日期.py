# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 引入模块
import time
import calendar
import datetime

ticks = time.time()
print("当前时间戳为:", ticks)

localtime = time.localtime(time.time())
print("本地时间为 :", localtime)

print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))


cal = calendar.month(2018,4)
print("以下输出2018年4月份的日历:")
print(cal)

i = datetime.datetime.now()
print("当前的日期和时间是 %s" % i)
print("ISO格式的日期和时间是 %s" % i.isoformat())
print("当前的年份是 %s" %i.year)
print("当前的月份是 %s" %i.month)
print("当前的日期是  %s" %i.day)
print("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year))
print("当前小时是 %s" % i.hour)
print("当前分钟是 %s" % i.minute)
print("当前秒是  %s" % i.second)