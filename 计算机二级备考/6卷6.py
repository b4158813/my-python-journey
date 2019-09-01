'''
import jieba
with open("sgld.txt","r",encoding ="utf-8")as f:
    lssgld = f.readlines()

info=''
for line in lssgld:
    line=line.replace('\n',"")
    info+=line

print('人：', info.count('人'))
'''

import jieba
with open("sgld.txt","r",encoding ="utf-8")as f:
    lssgld = f.readlines()

info=''
for line in lssgld:
    line=line.replace('\n',"")
    info+=line

print('人：', info.count('人'))