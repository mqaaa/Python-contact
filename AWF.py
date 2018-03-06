#! python3
#-*- encoding: utf-8 -*-
#AWF.py - AUTO_WRITE_INFO
#Usage:AWF.py FileNmame  
#
#Author : qmeng
#MailTo : qmeng1128@163.com
#QQ     : 1163306125
#Blog   : http://blog.csdn.net/Mq_Go/
#Create : 2018-02-10 15:37:32
#Version: 1.0
#
import time,sys,subprocess,os,pyperclip
_cpp_path_ = 'E:\\CPP\\'
_cpp_IDE_ = 'D:\\编译器\\devcpp\\Dev-cpp5.4.0及API帮助文档\\Dev-Cpp\\devcpp.exe'
_py_path_ = 'E:\\python\\'
_py_IDE_ = 'D:\\安装包\\Sublime Text 3.3126x64\\sublime_text.exe'
_txt_path_ = 'E:\\txt\\'
_txt_exe_ = 'D:\\安装包\\Sublime Text 3.3126x64\\sublime_text.exe'

def makeDir(path):
	if not os.path.exists(path):
		os.makedirs(path)

if len(sys.argv) < 2:
	print('输入格式不正确...')
temp = ' '.join(sys.argv[1:])
if temp.endswith('.cpp'):
	_file_path_ = os.path.join(_cpp_path_,temp)
	if os.path.exists(_file_path_):
		print('文件已存在！！！')
		subprocess.Popen([_cpp_IDE_,_file_path_])
		sys.exit()
	makeDir(_cpp_path_)
	file = open(_file_path_,'a')
	file.write('''
/*************************************************************
Author : qmeng
MailTo : qmeng1128@163.com
QQ     : 1163306125
Blog   : http://blog.csdn.net/Mq_Go/
Create : '''+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +'''
Version: 1.0
**************************************************************/
#include <cstdio>
#include <iostream>

using namespace std;
int main(){
	return 0;
}
	''')
	file.close()
	subprocess.Popen([_cpp_IDE_,_file_path_])
elif temp.endswith('.py') or temp.endswith('.pyw'):
	_file_path_ = os.path.join(_py_path_,temp)
	if os.path.exists(_file_path_):
		print('文件已存在！！！')
		subprocess.Popen([_py_IDE_,_file_path_])
		sys.exit()
	makeDir(_py_path_)
	file = open(_file_path_,'a')
	file.write('#! python3\n')
	file.write('#-*- encoding: utf-8 -*-\n')
	file.write('# '+temp+' - \n')
	file.write('# Usage:')
	file.write('''
#
# Author : qmeng
# MailTo : qmeng1128@163.com
# QQ     : 1163306125
# Blog   : http://blog.csdn.net/Mq_Go/
# Create : '''+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +'''
# Version: 1.0
#
import 
	''')
	file.close()
	subprocess.Popen([_py_IDE_,_file_path_])
else:
	makeDir(_txt_path_)
	_file_path_ = os.path.join(_txt_path_,temp)
	file = open(_file_path_,'a')
	file.write('\n'+pyperclip.paste());
	file.close()
	subprocess.Popen([_txt_exe_,temp])
