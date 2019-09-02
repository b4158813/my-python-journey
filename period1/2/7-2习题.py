# -*- coding: utf-8 -*-
#第一题
length_of_knife = int(input("请输入小刀的长度："))

if length_of_knife <= 10 and length_of_knife > 0:
    print ("允许上火车！")
elif length_of_knife > 10:
    print ('不允许上火车！')
else:
    print ('invalid digits')
    
    
    
#第二题
print('（身高单位为m 体重单位为kg）')
hight = float(input('请输入身高：'))
weight = float(input('请输入体重：'))
print('小明的身高为:%.2f,体重为:%.2f'%(hight,weight))
BMI_index = weight/(hight**2)
print("您的BMI指数为:%.2f"%BMI_index)
if BMI_index < 18.5 and BMI_index > 0:
    print ('过轻')
elif BMI_index >= 18.5 and BMI_index < 25:
    print("正常")
elif BMI_index >= 25 and BMI_index < 28:
    print ('肥胖')
elif BMI_index > 32:
    print ('严重肥胖！')
else:
    print('数据错误！')
    
