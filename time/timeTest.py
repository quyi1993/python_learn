#!/usr/bin/python
# -*- coding: UTF-8 -*-

#字符串的时候    <----->    时间戳   相互转换
import time
#int转struct_time转string
struct_time = time.localtime(1497511561)
print struct_time
print time.strftime("%Y-%m-%d %H:%M:%S", struct_time)

guoqi =  2592000+1497511561
print guoqi
guoqi_struct_time = time.localtime(guoqi)
print guoqi_struct_time
print time.strftime("%Y-%m-%d %H:%M:%S", guoqi_struct_time)

#string转时间戳int
a = "2011-09-28 10:00:00"
#中间过程，一般都需要将字符串转化为时间数组
time_struct = time.strptime(a,'%Y-%m-%d %H:%M:%S')
#将"2011-09-28 10:00:00"转化为时间戳
i = time.mktime(time_struct)
print i






