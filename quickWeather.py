#! python3
#quickWeather.py - 
#Usage:
#
#Author : qmeng
#MailTo : qmeng1128@163.com
#QQ     : 1163306125
#Blog   : http://blog.csdn.net/Mq_Go/
#Create : 2018-02-12 16:34:59
#Version: 1.0
#
import json,requests,sys
#输入查询地点
if len(sys.argv) < 2:
	print('Usage:quickWeather.py location')
	sys.exit()
location = ''.join(sys.argv[1:])

#下载JSON数据
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt3'%(location)
response = requests.get(url)
response.raise_for_status()

#加载JSON数据并打印天气
weatherData = json.loads(response.text)
w = weatherData['list']
print('Current weather in %s:'%(location))
print(w[0]['weather'][0]['main'],'-',w[0]['weather'][0]['description'])
print()
print('Tomorrow')
print(w[1]['weather'][0]['main'],'-',w[1]['weather'][0]['description'])
print()
print('Day After Tomorrow')
print(w[2]['weather'][0]['main'],'-',w[2]['weather'][0]['description'])
print()


