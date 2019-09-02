# -*- coding: utf-8 -*-

#打开和关闭文件：
#f=open("test1.txt","w")#当前目录下创建文件
#"r"不会创建文件，"w"则会创建一个文件
#f.write("hello\tworld")
#f.close()
f=open("test1.txt","r")
content=f.read(5)#只读五个字节
print(content)
f.close()

#文件拷贝：
import os
source_file=os.path.join(os.path.dirname(os.path.dirname(__file__))+"/.spyproject/","workspace.ini")
print(source_file)
#目标文件在当前目录下，文件名在原始文件名的前面加上copy-
dest_file="copy-"+source_file[source_file.rfind("/")+1:]

print("目标文件名字：%s"%dest_file)
#打开文件

source_f=open(source_file,"rb")
dest_f=open(dest_file,"wb")
#读取原始文件
content=source_f.read()
#把读取的内容写到目标文件中
dest_f.write(content)
#关闭文件
source_f.close()
dest_f.close()









