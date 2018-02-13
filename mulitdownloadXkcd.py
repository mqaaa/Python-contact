#! python3
# mulitdownloadXkcd.py - 
# Usage:
#
# Author : qmeng
# MailTo : qmeng1128@163.com
# QQ     : 1163306125
# Blog   : http://blog.csdn.net/Mq_Go/
# Create : 2018-02-13 21:31:39
# Version: 1.0
#

import requests,os,bs4,threading
os.makedirs('XKCD',exist_ok=True)

def downloadXkcd(startComic,endComic):
	#Download rhe page
	for urlNumber in range(startComic,endComic):
		print('Downloading page http://xkcd.com/%s...\n'%(urlNumber))
		res = requests.get('http://xkcd.com/%s'%(urlNumber))
		try:
			res.raise_for_status()
		except requests.exceptions.HTTPError:
			print('Not Found for url: https://xkcd.com/0')
			continue
		soup = bs4.BeautifulSoup(res.text,"html.parser")

		#find the url od the comic image
		comicElem = soup.select('#comic img')
		if comicElem == []:
			print('Could not find comic image '+ urlNumber +'...\n')
		else:
			comicUrl = comicElem[0].get('src')
			comicUrl = 'http:'+ comicUrl
			print('Downloading image %s...'%(comicUrl))
			res = requests.get(comicUrl)
			res.raise_for_status()

			imageFile = open(os.path.join('XKCD',os.path.basename(comicUrl)),'wb')
			for chunk in res.iter_content(100000):
				imageFile.write(chunk)
			imageFile.close()

#创建并启动线程
downloadThreads = [] #a list of all the Thread objects
for i in range(0,1400,100):
	downloadThread = threading.Thread(target=downloadXkcd,args=(i,i+3))
	downloadThreads.append(downloadThread)
	downloadThread.start()

#等待所有的线程结束
for downloadThread in downloadThreads:
	downloadThread.join()
print('Done...')

