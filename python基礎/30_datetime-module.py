from datetime import datetime
from datetime import timedelta

date = datetime.now()
print(date)

date2 = datetime(2020,2,4,12,34)
print(type(date2))
print(date2)
print(date2.year,date2.month,date2.day,date2.hour,date2.minute,date2.second)

date_str = date.strftime('%Y/%m/%d %H:%M:%S')
print(date_str)

str_datetime = '2028年8月8日20時10分'
date3 = datetime.strptime(str_datetime, '%Y年%m月%d日%H時%M分')
print(date3)

print('-'*50)

delta1=datetime(2028,10,1)-datetime(2028,5,1)
print(type(delta1), delta1)

delta2 = timedelta(10,11)
print(delta2)