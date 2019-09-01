import random

random.seed(0x1010)

s='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*'
password=[]

excludes=[]

while len(password)<10:
    test_password=''
    for i in range(10):
        test_password += s[random.randint(0,len(s)-1)]
    if test_password[0] in excludes:
        continue

    password.append(test_password)
    excludes.append(test_password[0])

print('\n'.join(password))


