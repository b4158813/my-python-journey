'''
np.unique函数
    求数组的非重复值
'''

import numpy as np

arr = np.array(['China','United states','India','China','Britain','China','Britain'])
print(arr)
print(np.unique(arr))# 自动按首字母顺序排序