#! python3
# mcb.pyw - Save and loads pieces of text to the clipboard
# Usage: mcb.pyw save <key> - Save clipboard to keyworld
#        mcb.pyw <key> - Loads keyworld to clipboard
#        mcb.pyw list - Loads all keyworld to clipboard
#        mcb.pyw del <key> - del keyworld
#        mec.pyw del - del all key world

#Author : qmeng
#MailTo : qmeng1128@163.com
#QQ     : 1163306125
#Blog   : http://www.cnblogs.com/Mq_Go
#Create : 2018-02-06
#Version: 1.0

import sys,pyperclip,shelve
mcbShelf = shelve.open('mcb')

# TODO:Save and del clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'del':
        if sys.argv[2] in mcbShelf.keys():
            del mcbShelf[sys.argv[2]]
            print(sys.argv[2] + '删除成功')
        else:
            print('没有'+sys.argv[2]+'项')

# TODO:List keywords and load cintent or del all keyworlds.
if len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'del':
        if mcbShelf is not None:
            for item in mcbShelf.items():
                print('删除数据[{}] = [{}]'.format(item[0], mcbShelf[item[0]]))
                del mcbShelf[item[0]]
        else:
             print('mcb 为空!')
    else:
        if sys.argv[1].lower() in mcbShelf.keys():
            pyperclip.copy(mcbShelf[sys.argv[1]])
        else:
            print('Sorry,未找到该项')
mcbShelf.close()
            
        
        


