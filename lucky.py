#! python3
#lucky.py - Opens several search results.
#
#
#Author : qmeng
#MailTo : qmeng1128@163.com
#QQ     : 1163306125
#Blog   : http://blog.csdn.net/Mq_Go/
#Create : 2018-02-08
#Version: 1.0

import requests,sys,bs4,webbrowser
print('正在搜索...')
re = requests.get('https://www.sogou.com/web?query='+' '.join(sys.argv[1:]))
print('https://www.sogou.com/web?query='+' '.join(sys.argv[1:]))
re.raise_for_status()
#print(re.text[:5600])
#Retrieve top search result links.
soup = bs4.BeautifulSoup(re.text, "html.parser")
#Open a browser tab for each result.
linkElems = soup.select('.vrTitle a')

numopen = min(3,len(linkElems))
for i in range(numopen):
	print('已经为您打开'+linkElems[i].getText())
	print()
	webbrowser.open(linkElems[i].get('href'))
