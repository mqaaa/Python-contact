#! python3
# bulletPointAdder.py

import pyperclip
text = pyperclip.paste()

temp = text.split('\n')
for i in range(len(temp)):
    temp[i] = '* ' + temp[i]

text = '\n'.join(temp)
pyperclip.copy(text)
    
