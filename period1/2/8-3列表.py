# -*- coding: utf-8 -*-

name="he llo\tsdfds\ti2p tr9\n2fifjd use"
print(name.split())#括号里什么都不写：用字符串里常见隔开符隔开
print(name.split()[-2])#隔开后取倒数第二个



#list 列表
names1=[100,200,300,400]#列表中元素可以是任意类型


#列表的 增 删 改 査
names1.append(600)#append为在尾部添加
print(names1)
names2=[1,2]
names1.extend(names2)#extend为合并列表
print(names1)
names1.insert(2,"000")#insert为在某个下标位前插入 下标位会随之改变
print(names1)
names1[2]=666#修改某个下标位的值
print(names1)
names1.insert(2,666)#可重复
print(names1)


print(names1.count(666))#出现两次
print(100 in names1)#100在names1里面 返回True
print(100 not in names1)#返回false

del names1[1]#删除某下标位元素（括号内为某下标位）
print(names1)
#del names1 #删除全部

names1.pop()#删除列表最后一个元素
print(names1)

names1.remove(666)#删除某元素（括号内为内容）
print(names1)

#排序
names1.reverse()#逆置 也可以用names1[-1::-1]
print(names1)
names1.sort()#从小到大排序 必须是同一类型的
print(names1)
names1.sort(reverse=True)#降序
print(names1)





#
print("="*30)
print("学生管理系统".center(30))
print("请输入1：添加学生")
print("请输入2：查找学生")
print("请输入3：修改学生")
print("请输入4：删除学生")
print("请输入5：退出")

stus=[]
while True:
    operate=input("请输入你想要的操作：")
    if operate=="1":
        name=input("请输入添加学生的姓名：")
        stus.append(name.strip())
        print(stus)
    if operate=="2":
        name=input("请输入查找学生的名字：")
        if name not in stus:
            print("您输入的学生%s不存在"%name)
        else:
            print("该学生的位置为：%d"%(stus.index(name)+1))
    if operate=="3":
        name=input("请输入需要修改的学生的名字：")
        if name not in stus:
            print("您输入的学生%s不存在"%name)
            continue
        else:
            namea=input("请输入修改后的名字：")
            sequnce=int(stus.index(name))
            stus[sequnce]=namea
            print(stus)
    if operate=="4":
        name=input("请输入要删除的学生的姓名：")
        if name not in stus:
            print("您输入的学生%s不存在"%name)
            continue
        else:
            stus.remove(name)
            print(stus)
    if operate=="5":
        print('\n欢迎下次再来！\n')
        break





































