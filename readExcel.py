#! python3
#readExcel.py 
#
#Author : qmeng
#MailTo : qmeng1128@163.com
#QQ     : 1163306125
#Blog   : http://blog.csdn.net/Mq_Go/
#Create : 2018-02-010
#Version: 1.0
#
import openpyxl,pprint,os
print('Opening workbook...')
wb = openpyxl.load_workbook('2017.xlsx')
sheet = wb.get_sheet_by_name('Sheet0')
Data = {}
print('Reading rows...')
for row in range(3,sheet.max_row+1):
	Num      = sheet['B'+str(row)].value
	Name     = sheet['E'+str(row)].value
	sProject = sheet['F'+str(row)].value
	eProject = sheet['G'+str(row)].value
	
	#填充数据结构
	#Data.setdefault(Num,{Name:'',sProject:'',eProject:''})
	Data[Num] = {'Name':Name,'sProject':sProject,'eProject':eProject}
	#print(Name + ' 同学信息加载完毕...')
print('Writing results...')
File = open('abcdef.py','w')
File.write('allData = ' + pprint.pformat(Data))
File.close()
print('Done...')

#import abcdef
#>>> abcdef.allData['2017000349']
#{'Name': '18834198699', 'eProject': '9/933', 'sProject': 4.28}
