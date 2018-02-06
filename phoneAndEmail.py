#! python3
import pyperclip,re
mailRegex = re.compile(r'''(
    [a-zA-Z0-9_%+-]+   #username    
    @                 #
    [a-zA-Z0-9.-]+    #domain name
    (\.[a-zA-Z]{2,4})    #
    )''',re.VERBOSE)
phoneRegex = re.compile(r'''
    \(?(\d{3})\)?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})''',re.VERBOSE)

text = str(pyperclip.paste())
matches = []
#123-456-1234
for group in phoneRegex.findall(text):
    phoneNum = '-'.join([group[0],group[2],group[4]])
    matches.append(phoneNum)
for group in mailRegex.findall(text):
    matches.append(group[0])

if(len(matches) > 0):
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print("No found")
