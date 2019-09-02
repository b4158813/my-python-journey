# -*- coding: utf-8 -*-

age_of_oldboy = 56

count = 0
while count <3:
    guess_age = int(input('guess age:'))
    if guess_age == age_of_oldboy :
        print('yes, you got it')
        break
    elif guess_age > age_of_oldboy:
        print('think it smaller...')
    else:
        print('think it bigger!')
        
    count +=1
    if count ==3:
        continue_confirm = input('do you want to keep trying..?')
        if continue_confirm != 'n':
            count =0
#else:
#print('you have tried too many times.. fuck off')
            
            
            
            