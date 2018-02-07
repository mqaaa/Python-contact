#! python3
#backupToZip.py - Copies an entire folder and its contents into a ZIP file whose filename increments.
#Usage：backupToZip.py <Path> - Compress the file of the abspath to a backup.

#Author : qmeng
#MailTo : qmeng1128@163.com
#QQ     : 1163306125
#Blog   : http://blog.csdn.net/Mq_Go/
#Create : 2018-02-07
#Version: 1.0

import sys,zipfile,os
def backupfile(folder):
    #Backup the entire contents of "folder" into a zip file
    if os.path.isabs(folder) != True:
        folder = os.path.abspath(folder)
    number = 1
    while True:
        zipName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(os.path.join(os.path.dirname(folder),zipName)):
            print(os.path.join(os.path.dirname(folder),zipName))
            break
        number = number + 1

    # Create the zip file
    print('Create the %s...'%(zipName))
    backupZip = zipfile.ZipFile(os.path.join(os.path.dirname(folder),zipName),'w')

    #Walk the entire folder tree and compress the files in each folder.
    for folder,subfolders,files in os.walk(folder):
        print('Add file is in %s...'%(folder))
        backupZip.write(folder)
        for file in files:
            newBase = os.path.basename(folder)+'_'
            if file.startswith(newBase) and file.endswith('.zip'):
                continue
            backupZip.write(os.path.join(folder,file))
    backupZip.close()
    print('Done')
if len(sys.argv) == 2:
    if not os.path.exists(sys.argv[1].lower()):
        print('No such file')
    else:
        backupfile(sys.argv[1].lower())
        
    
        
    
