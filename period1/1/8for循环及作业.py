# -- coding: utf-8 -*-
'''
for i in range(0,10):
    if i < 5:
        print ('loop',i)
    else:
        continue#结束本次循环 进行下一次循环
    print('hehe...')
'''

    
for i in range(10):
    print('--------',i)
    for j in range(10):
        print(j)
        if j >5:
            break