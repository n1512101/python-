import requests
import re

url = 'http://www.weather.com.cn/weather1d/101010100.shtml'
res = requests.get(url)
res.encoding = 'utf-8'
# print(res.text)

city = re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>', res.text)
print(city)