x=input("输入一串字符：")
c_e=0
c_n=0
c_s=0
c_else=0
for i in x:
    if 'A'<i<'z':
        c_e+=1
    elif '0'<i<'9':
        c_n+=1
    elif i==' ':
        c_s+=1
    else:
        c_else+=1

print('英文字符{0}个，数字{1}个，空格{2}个，其他字符{3}个'.format(c_e,c_n,c_s,c_else))

