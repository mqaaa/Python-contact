#! python3
#-*- encoding: utf-8 -*-# formFiller.py - 
# Usage:
#
# Author : qmeng
# MailTo : qmeng1128@163.com
# QQ     : 1163306125
# Blog   : http://blog.csdn.net/Mq_Go/
# Create : 2018-02-20 13:27:48
# Version: 1.0
#
import pyautogui,time
# 建立坐标
nameField = (648, 319)
submitButton = (651, 817)
submitButtonColor = (75, 141, 249)
submitAnotherLink = (760, 224)
# 要填写的内容
formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
            ]

#在每次Gui函数时停留0.5秒
pyautogui.PAUSE = 0.5

# 开始键入数据
for person in formData:
	print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)

    while not pyautogui.pixelMatchesColor(submitButton[0],submitButton[1],submitButtonColor):
    	time.sleep(0.5)

    print('Entering %s info...' % (person['name']))
    pyautogui.click(nameField[0], nameField[1])

    # Fill out the Name field.
    pyautogui.typewrite(person['name'] + '\t')

    # Fill out the Greatest Fear(s) field.
    pyautogui.typewrite(person['fear'] + '\t')
    
    # 处理选项列表和单选按钮
    if person['source'] == 'wand':
        pyautogui.typewrite(['down', '\t'])
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down', 'down', '\t'])
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down', '\t'])
    elif person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'])

    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\t'])
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right', 'right', '\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])

    pyautogui.typewrite(person['comments'] + '\t')
    pyautogui.press('enter')
    print('Clicked Submit.')
    time.sleep(5)
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])

