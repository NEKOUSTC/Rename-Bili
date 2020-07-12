import json
import os
import re

boxname = 'download'
list = os.listdir(boxname)
print(list)
for fbox in list:
    print('原文件夹："'+fbox+'"')
    if re.search('\D',fbox):#only number
        print('skip"'+fbox+'"')
    else:
        with open(boxname+'/'+fbox+'/1/entry.json','r') as j_in:
            videoname = json.loads(j_in.read())['title']
            #print(videoname)
            a = re.findall(r'[^\*"/:?\\|<>]',videoname,re.S) 
            fname = "".join(a)
            print('重命名为："'+fname+'"')
        os.rename(boxname+'/'+fbox,boxname+'/'+fbox+' '+fname)