#! python3
# pw.py - An insecure password locker program.

PASSWORDS = {'email':'15735184252@163.com',
             'blog':'http://blog.csdn.net/mq_go',
             'luggage':'123456' }
import sys,pyperclip
if len(sys.argv)<2:
    print('Usage:python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  #这里应该是account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' is copied to clipboard.')
else:
    print('There is no account named '+ account)
