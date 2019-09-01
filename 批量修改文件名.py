import os

path = input('请输入文件路径(结尾加上/)：')

# 获取该目录下所有文件，存入列表中
f = os.listdir(path)


def rename(oldname, type, n):
    # 设置新文件名
    newname = path + str(n + 1) + '.' + type

    # 用os模块中的rename方法对文件改名
    os.rename(oldname, newname)
    print(oldname, '======>', newname)


n = 0

for i in f:
    # 设置旧文件名（就是路径+文件名）
    oldname = path + f[n]
    if f[n][-3:] == 'JPG':
        rename(oldname, 'JPG', n)
    elif f[n][-3:] == 'PNG':
        rename(oldname, 'PNG', n)
    elif f[n][-3:] == 'MP3':
        rename(oldname, 'MP3', n-1)
    elif f[n][-3:] == 'MP4':
        rename(oldname, 'MP4', n-1)

    n += 1
