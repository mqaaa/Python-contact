#! python3
#removeCsvHeader.py - 
#Usage:
#
#Author : qmeng
#MailTo : qmeng1128@163.com
#QQ     : 1163306125
#Blog   : http://blog.csdn.net/Mq_Go/
#Create : 2018-02-12 15:17:52
#Version: 1.0
#
import csv,os
#创建修改后的文件夹
os.makedirs('CSV2',exist_ok=True)
#遍历要修改的文件夹
for i in os.listdir('.\\CSV'):
	if not i.endswith('.csv'):
		continue
	print('Removing header from '+i +'...')
	csvPath = os.path.join('.\\CSV',i)
	csvRow = []
	#读取文件
	csvFile = open(csvPath)
	csvReader = csv.reader(csvFile)
	for Row in csvReader:
		if csvReader.line_num == 1:
			continue
		csvRow.append(Row)
	csvFile.close()

	#将csvRow中的内容生成新的CSV文件
	csvPath = os.path.join('.\\CSV2',i)
	csvFile = open(csvPath,'w',newline='')
	csvWriter = csv.writer(csvFile)
	for Row in csvRow:
		csvWriter.writerow(Row)
	csvFile.close()
	

	
