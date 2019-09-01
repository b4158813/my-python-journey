fread=open('天龙八部-网络版.txt','r',encoding='utf-8')
fwrite=open('天龙八部-汉字统计.txt','w',encoding='utf-8')

txt=fread.read()
d = {}
for i in txt:
	d[i]=d.get(i,0)+1
del d[' ']
del d['\n']

l = []
for p in d:
	l.append('{}:{}'.format(p,d[p]))
fwrite.write(','.join(l))
fread.close()
fwrite.close()
print('ok')



