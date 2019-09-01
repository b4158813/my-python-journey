from random import *

first_choice=0
change_choice=0

for i in range(10000):
    my_first_choice=randint(0,2)
    my_change_choice=randint(0,2)
    if my_first_choice==my_change_choice:
        first_choice+=1
    else:
        change_choice+=1

print('不改变决定：',first_choice/10000)
print('改变决定：',change_choice/10000)

