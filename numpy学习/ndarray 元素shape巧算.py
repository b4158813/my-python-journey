'''
shape计算

取出指定元素
'''

import numpy as np

arr1 = np.array(
    [
        [
            [1,2,3,4,5],
            [2,3,4,5,6],
            [3,7,4,5,6],
            [4,5,6,7,8]
        ],
        [
            [1, 23, 3, 4, 5],
            [2, 3, 4, 55, 6],
            [3, 74, 4, 5, 6],
            [4, 5, 6, 72, 8]
        ]
    ]
)

print(arr1.shape)
print(arr1.size)

print(arr1[0][1][1])
