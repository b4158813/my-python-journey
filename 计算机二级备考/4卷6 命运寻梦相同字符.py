fr_x=open('寻梦-字符统计.txt','r',encoding='utf-8')
fr_m=open('命运-字符统计.txt','r',encoding='utf-8')

fw_same=open('相同字符.txt','w')
txt_x=fr_x.read().split(',')
txt_m=fr_m.read().split(',')


for i in range(len(txt_x)):
    txt_x[i]=txt_x[i].split(':')[0]
    txt_m[i]=txt_m[i].split(':')[0]
fr_m.close()
fr_x.close()

ls=[]
for a in txt_x:
    if a in txt_m:
        ls.append(a)

fw_same.write(','.join(ls))
fw_same.close()