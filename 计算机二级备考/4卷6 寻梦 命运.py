import operator

fr_x=open('寻梦-网络版.txt','r',encoding='utf-8')
fw_x=open('寻梦-字符统计.txt','w',encoding='utf-8')
fr_m=open('命运-网络版.txt','r',encoding='utf-8')
fw_m=open('命运-字符统计.txt','w',encoding='utf-8')

txt_x=fr_x.read()
txt_m=fr_m.read()
char_x={}
char_m={}

for i in txt_x:
    char_x[i]=char_x.get(i,0)+1
for i in txt_m:
    char_m[i]=char_m.get(i,0)+1

sort_char_x=sorted(char_x.items(),key=operator.itemgetter(1),reverse=True)
sort_char_m=sorted(char_m.items(),key=operator.itemgetter(1),reverse=True)
sort_100_char_x=sort_char_x[:101]
sort_100_char_m=sort_char_m[:101]

ls_sort_100_char_x=[]
for i in sort_100_char_x:
    ls_sort_100_char_x.append('{}:{}'.format(i[0],i[1]))
ls_sort_100_char_m=[]
for i in sort_100_char_m:
    ls_sort_100_char_m.append('{}:{}'.format(i[0],i[1]))

fw_x.write(','.join(ls_sort_100_char_x))
fw_m.write(','.join(ls_sort_100_char_m))
fr_x.close()
fr_m.close()
fw_x.close()
fw_m.close()




