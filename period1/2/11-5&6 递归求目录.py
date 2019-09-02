# -*- coding: utf-8 -*-

#从/home/python目录下找包含hello的py文件是哪些？
import os
file_list=[]

#递归函数，该函数中所有文件路径全部采用绝对路径,parent_dir:文件所在的父目录的绝对路径;file_name:当前要处理的文件或目录
def find_hello(parent_dir,file_name):
    file_abspath=os.path.join(parent_dir,file_name)#当前正在处理的文件或者目录的绝对路径
    if  os.path.isdir(file_abspath):#判断当前文件文件是一个目录
        for f in os.listdir(file_abspath):#进入目录，列出该目录下的所有文件列表
            find_hello(file_abspath,f)#递归调用自己本身的函数
    else:
        if file_abspath.endswith(".py"):#如果传入的文件就是文件，判断文件名是否以.py结尾
            if read_and_find_hello(file_abspath):#读取该py结尾的文件，并且看看文件内容中是否包含有hello
                file_list.append(file_abspath)#把包含hello的文件目录保存到列表中

def read_and_find_hello(py_file):
    flag=False
    f=open(py_file,)
    while True:
        line=f.readline()
        if line=="":#文件读到最后一行，终止循环
            break
        elif "hello" in line:
            flag=True
            break
    f.close()
    return flag

find_hello("/period 1","2")
print(file_list)

#把学生管理系统改成文件版，学生保存之后写到某个文件中，程序第一次启动的时候，学生列表从读取文件内容中来








































