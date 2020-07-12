import re
with open('try.txt') as f1:
    str2 = str(f1.read())
str1 = '0:1*2?3"4<5>6|7/8\\9'
print(str1,str2)
#transed = re.sub('\*' | ':' | '\?' | '<' | '>' | '\|' | '\/' | '\\','',str2)
a = re.findall(r'[^\*"/:?\\|<>]',str1,re.S) 
a = "".join(a)
print(a)