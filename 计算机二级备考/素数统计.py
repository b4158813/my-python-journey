def isPrime(a):
    flag=0
    if a==2:
        return True
    try:
        for i in range(2,a):
            if a%i==0:
                flag+=1
        if flag>0:
            return False
        else:
            return True

    except:
        print('程序错误！')



