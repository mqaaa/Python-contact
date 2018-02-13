#! python3
#stopwatch.py - 
#Usage:
#
#Author : qmeng
#MailTo : qmeng1128@163.com
#QQ     : 1163306125
#Blog   : http://blog.csdn.net/Mq_Go/
#Create : 2018-02-13 16:18:46
#Version: 1.0
#
import time
print('Press ENTER to begin.Afterwards,\npress ENTER to "click" the stopwatch \nPress Ctrl+C to quit.')
input()
print('Started...')
startTime = time.time()
lastTime = startTime
lapNum = 1;

#记录并打印单圈时间
try:
	while True:
		input()
		temp = time.time()
		lapTime = round(temp-lastTime,2)
		lastTime = temp
		totalTime = round(time.time()-startTime,2)
		print('第 %s 圈，用时 %s 秒，总用时 %s 秒'%(lapNum,lapTime,totalTime))
		lapNum += 1
except KeyboardInterrupt:
	print('\nDone')
