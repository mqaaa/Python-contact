#! python3
#downloadXKcd.py - downloads every single XKCD comic.
#
#
#Author : qmeng
#MailTo : qmeng1128@163.com
#QQ     : 1163306125
#Blog   : http://blog.csdn.net/Mq_Go/
#Create : 2018-02-08
#Version: 1.0

import requests,os,bs4
url  = 'http://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
k = 0
while not url.endswith('#') and k != 5:
	k = k + 1
	#download the page.
	print('Downloading page %s...'%(url))
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text,"html.parser")

	#find the URL of the comic image.
	comicElem = soup.select('#comic img')
	if comicElem == []:
		print('Could not find comic image.')
	else:
		comicUrl = comicElem[0].get('src')
		comicUrl = 'http://xkcd.com' + comicUrl[1:]
		print('Downloading image %s...'%(comicUrl))
		res = requests.get(comicUrl)
		res.raise_for_status()

		imgFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
		for chunk in res.iter_content(100000):
			imgFile.write(chunk)
		imgFile.close()

	prevLink  = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prevLink.get('href')
			
