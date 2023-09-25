#datetime
""" from datetime import datetime as dt

print(dt.now())

from pytz import timezone
tz = timezone('UTC')
print("timezone : ", dt.now(tz))

date_string = '2021-07-08'
date_object = dt.strptime(date_string, '%Y-%m-%d')
print(date_object)

date_object = dt.now()
date_string = date_object.strftime('%Y-%m-%d')
print(date_string) """

""" import mod.utils as mu

dtnow = mu.get_dtnow()
print(dtnow)

ret = mu.cvt_time2str("2022-09-25")
print(ret)

res = mu.cvt_str2time () """

#os
""" import os

print(os.getcwd())
print(os.chdir("../"))
print(os.getcwd())
print(os.listdir())
os.mkdir('new directory')
print(os.listdir())
os.rmdir('new directory')
print(os.listdir()) """

""" import os
import mod.utils as mu

print(mu.get_curdir())

pname = "python"
mu.os_mkdir("python")
print(os.listdir())

os.rmdir(pname)
print(os.listdir()) """

#sys
""" import sys

print(sys.version)
print(sys.argv) """

#스택 stack
""" list = []
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
print(list)

top = list.pop()
print(top)
print(list)
print(len(list)) """

#큐 queue
queue = []
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
print(queue)

front = queue.pop(0)
print(front)
print(queue)
print(len(queue))

