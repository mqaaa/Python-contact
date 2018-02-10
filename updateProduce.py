#! python3
#updateProduce.py - 
#Usage:
#
#Author : qmeng
#MailTo : qmeng1128@163.com
#QQ     : 1163306125
#Blog   : http://blog.csdn.net/Mq_Go/
#Create : 2018-02-10 15:42:18
#Version: 1.0
#
import openpyxl
wb = openpyxl.load_workbook('temp.xlsx')
sheet = wb.get_sheet_by_name('Sheet3')
UPDATA = {'10点06分':'200',
			'10点07分':'300',
			'10点08分':'400'}
for row in range(1,sheet.max_row):
        if sheet['B'+str(row)].value in UPDATA.keys():
                sheet['D'+str(row)] = UPDATA[sheet['B'+str(row)].value]
                print(sheet['B'+str(row)].value)
wb.save('temp.xlsx')
