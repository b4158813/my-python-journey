# -*- coding: utf-8 -*-

#读文件：
f=open("test2.txt","r")
c1=f.read(3)#此时指针指向第四个字节前面
print(c1)
pos1=f.tell()#位置
print(pos1)#第四个字节下标位为3
c2=f.read(1)#读第四个字符
print(c2)
f.seek(0,0)#seek(偏移量,方向2) 此刻回到开头
c2=f.read(3)
print(c2)
f.seek(0,1)#从当前位置开始读
c3=f.read(2)
print(c3)
f.close()
#os模块：
'''
import os
os.rename("test1.txt","test2.txt")#重命名
os.path.abspath("test2.txt")#获取绝对路径
os.path.getsize("test2.txt")#获取文件大小（字节数）
###批量修改文件名：
'''
#目录下的所有文件重新命名：
#注意：绝对路径不能写死
import os
file_list=os.listdir("test/")#获得一个列表，包含test目录下所有文件
for f in file_list:
    dest_file="re-"+f #重新命名之后的目标文件名
    #f为原始文件名，它不在工作目录下，所以不能使用文件名作为相对路径
    #f文件的相对路径为：test/f 或者干脆写绝对路径
    #os.rename("test/"+f,"test/"+dest_file)
    parent_dir=os.path.abspath("test")#获得父目录的绝对路径 动态获得绝对路径
    #文件的绝对路径=父目录的绝对路径+/+文件名
    source_file=os.path.join(parent_dir,f)#链接目录与文件名
    dest_file=os.path.join(parent_dir,dest_file)
    os.rename(source_file,dest_file)


