'''
通用带参数装饰器
1.不定长参数
2.带返回值
'''

from time import ctime,sleep

def timefun(func):
    def wra