import time
now = time.time()
print(now)

obj = time.localtime()
print(obj)

obj2=time.localtime(60)
print(obj2)
print(obj2.tm_year)

print(time.ctime())

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))