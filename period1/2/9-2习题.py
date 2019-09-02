# -*- coding: utf-8 -*-
#
print("="*30)
print("学生管理系统".center(30))
print("请输入1：添加学生")
print("请输入2：查找学生")
print("请输入3：修改学生")
print("请输入4：删除学生")
print("请输入5：查看所有学生")
print("请输入6：退出")
#一个学生包含很多信息，一个学生一个字典。学生列表用列表存储

stus=[]
while True:
    operate=input("请输入你想要的操作：")
    if operate=="1":
        name=input("请输入学生的姓名：")
        age=int(input("请输入学生的年龄："))
        qq=input("请输入学生的qq号：")
        #一个学生包括三个信息，这三个信息存到一个字典中
        stu={}#申明一个字典变量
        stu["name"]=name.strip()#往字典中添加一个元素
        stu["age"]=age#往字典中添加一个元素
        stu["qq"]=qq.strip()#往字典中添加一个元素
        stus.append(stu)
        print("添加成功")
    if operate=="2":
        name=input("请输入要查找学生的名字：")
        for item in stus:
            if item["name"]==name.strip():#判断字典中包含有该学生的姓名
                print("%s 学生存在，年龄为:%s，qq号为:%s"%(item['name'],item['age'],item['qq']))
                break
        else:#break是整个循环终止，不会执行else
            print("学生%s没有找到"%name)
    if operate=="3":
        name=input("请输入需要修改的学生的名字：")
        for item in stus:
            if item["name"]==name.strip():
                namea=input("输入修改后的名字:")
                item["name"]=namea
                break
        else:
            print("学生%s不存在\n"%name)
    if operate=="4":
        name=input("请输入要删除的学生的姓名：")
        for item in stus:
            if item["name"]==name.strip():
                seq=stus.index(item)
                del stus[seq]
                break
        else:
            print("学生%s不存在\n"%name)
    if operate=="5":
        print("序号\t姓名\t年龄\tqq号")
        for i,item in enumerate(stus,1):
            print("%s\t%s\t%s\t%s"%(i,item['name'],item['age'],item['qq']))
    if operate=="6":
        print('\n欢迎下次再来！\n')
        break


