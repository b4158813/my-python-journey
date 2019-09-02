# -*- coding: utf-8 -*-
import os
def read_stus():
    '''文件中存放数据的方式
    zs/t33/t465465456
    ls/t55/t987878787
    ww/t12/t142421421
    '''
    if os.path.exists(file_name):
        f=open(file_name,"r")
        while True:
            student_str=f.readline()
            if student_str=="":
                break
            elif student_str.strip()!="" and student_str.strip()!="\n":
                student_info_list=student_str.split("\t")
                student={"name":student_info_list[0],"age":student_info_list[1],"qq":student_info_list[2]}
                stus.append(student)
    
def write_stus_to_file():
    if os.path.exists(file_name):
        if os.path.exists(backup_file):
            os.remove(backup_file)
        os.rename(file_name,"backup-"+file_name)
    f=open(file_name,"w")
    for student in stus:
        student_str=("%s\t%s\t%s"%(student["name"],student["age"],student["qq"]))
        f.write(student_str)
        f.write("\n")
    f.close()
    
def print_menu():
    print("="*30)
    print("学生管理系统".center(30))
    print("请输入1：添加学生")
    print("请输入2：查找学生")
    print("请输入3：修改学生")
    print("请输入4：删除学生")
    print("请输入5：查看所有学生")
    print("请输入6：退出")
def add_student():
    name=input("请输入学生的姓名：")
    age=int(input("请输入学生的年龄："))
    qq=input("请输入学生的qq号：")
    stu={}
    stu["name"]=name.strip()
    stu["age"]=age
    stu["qq"]=qq.strip()
    stus.append(stu)
    print("添加成功")
def search_student(name):
    for item in stus:
        if item["name"]==name.strip():#判断字典中包含有该学生的姓名
            print("%s 学生存在"%name)
            print_student(item)
            break
    else:
        print("学生%s没有找到"%name)
def change_student(name):
    for item in stus:
        if item["name"]==name.strip():
            namea=input("输入修改后的名字:")
            item["name"]=namea
            break
    else:
        print("学生%s不存在\n"%name)
def delete_student(name):
    for item in stus:
        if item["name"]==name.strip():
            seq=stus.index(item)
            del stus[seq]
            break
    else:
        print("学生%s不存在\n"%name)
def print_student(item):
    print("%s\t%s\t%s"%(item['name'],item['age'],item['qq']))
def print_all_student():
    print("序号\t姓名\t年龄\tqq号")
    for i,item in enumerate(stus,1):
        print("%s\t"%i,end="")
        print_student(item)
def main():
    print_menu()
    read_stus()
    while True:
        operate=input("请输入你想要的操作：")
        if operate=="1":
            add_student()
            write_stus_to_file()
        if operate=="2":
            name=input("请输入要查找学生的名字：")
            search_student(name)
        if operate=="3":
            name=input("请输入需要修改的学生的名字：")
            change_student(name)
        if operate=="4":
            name=input("请输入要删除的学生的姓名：")
            delete_student(name)
            print("删除学生%s成功"%name)
            write_stus_to_file()
        if operate=="5":
            print_all_student()
        if operate=="6":
            print('\n欢迎下次再来！\n')
            break
        
file_name="stus.txt"#存放学生数据的文件
backup_file="backup-stus.txt"
stus=[]#全局变量
main()









































