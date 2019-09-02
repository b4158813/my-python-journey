# -*- coding: utf-8 -*-
'''
for i in range(10):
    print('loop',i)
   '''  

age_of_oldboy = 56

for i in range(3):
    guess_age = int(input('guess age:'))
    if guess_age == age_of_oldboy :
        print('yes, you got it')
        break
    elif guess_age > age_of_oldboy:
        print('think it smaller...')
    else:
        print('think it bigger!')
else:
    print('you have tried too many times.. fuck off')
    
    
'''
只打印偶数
'''
for i in range(0,10,2):#默认为 1 （x，x，1）
    print('loop',i)
