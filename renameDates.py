#！python3
#renameDates.py - Rename filenames with American MM-DD-YYYY date format to European DD-MM-YYYY

import os,shutil,re
#为美国风格的日期建立一个正则表达式
date = re.compile(r'''
	^(.*?)
	((0|1)?\d)-
	((0|1|2|3)?\d)-
	((19|20)\d\d)
	(.*?)$
	''',re.VERBOSE)
#Loop over the file in the working directory.
for filename in os.listdir('.'):
	mo = date.search(filename)
	#Skip files without date.
	if mo == None:
		continue
	#Get the different parts od the filename.
	beforPart = mo.group(1)
	monthPart = mo.group(2)
	dayPart = mo.group(4)
	yearPart = mo.group(6)
	afterPart = mo.group(8)
	"""
	date = re.compile(r'''
		^(1)
		(2(3))-
		(4(5))-
		(6(7))
		(8)$
	''',re.VERBOSE)
	"""
	#Form the European-style filename.
	euroDate = beforPart + dayPart +'-'+ monthPart +'-'+ yearPart + afterPart

	#Get the full,absolute file paths
	absPath = os.path.abspath('.')
	amerPath = os.path.join(absPath,filename)
	EuroPath = os.path.join(absPath,euroDate)

	#Rename the file.
	print('Rename %s to %s'%(amerPath,EuroPath))
	shutil.move(amerPath,EuroPath)



