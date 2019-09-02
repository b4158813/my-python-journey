import numpy as np
import pandas as pd
from pandas import DataFrame,Series
#select by label:loc 根据标签选择
#select by position:iloc 根据位置选择
#mixed selection:ix 混合选择
#Boolean indexing
dates = pd.date_range('20190219',periods=6)
df = DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df.iloc[2,2] = 1111# 根据位置更改值
df.loc['20190219','B'] = 2222# 根据标签改值
df[df.A>8] = 0#
print(df)