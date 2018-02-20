#! python3
#-*- encoding: utf-8 -*-# resizeAndAddLogo.py - 
# Usage:
#
# Author : qmeng
# MailTo : qmeng1128@163.com
# QQ     : 1163306125
# Blog   : http://blog.csdn.net/Mq_Go/
# Create : 2018-02-19 15:40:07
# Version: 1.0
#
import os
from PIL import Image
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

#打开徽标图案
logoIm = Image.open(LOGO_FILENAME)
logoWidth,logoHeight = logoIm.size

#遍历所有文件打开图像
for filename in os.listdir('.'):
	if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
		continue
	im = Image.open(filename)
	width,height = im.size
	if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
		if width > height:
			height = int((SQUARE_FIT_SIZE/width)*height)
			width = SQUARE_FIT_SIZE
		else:
			width = int((SQUARE_FIT_SIZE/height)*width)
			height = SQUARE_FIT_SIZE
		print('Resizing %s...'%(filename))
		im.resize((width,height),Image.ANTIALIAS)
		print('Adding logo to %s...'%(filename))
		im.paste(logoIm,(width - logoWidth,height - logoHeight),logoIm)
	im.save(os.path.join('withLogo',filename))
