# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 18:30:23 2020

@author: AAA
"""

import pandas as pd
import numpy as np
import math

data=pd.read_csv('F:\股票预测测试\stock-prediction-main\代码\个股走势预测\models\\test\Zhongxing_event+senti_new10.01.csv',encoding='utf-8')
data.head()
df=pd.DataFrame()

date=[]
close=[]
pred=[]

for i in range(len(data)-1):
    date.append(data.iloc[i, 2])
    close.append(data.iloc[i, 3])
    if data.iloc[i, 0] > 0.5:
        pred.append(data.iloc[i, 3] + abs(data.iloc[i, 3]-data.iloc[i+1, 3]))
    else:
        pred.append(data.iloc[i, 3] - abs(data.iloc[i, 3]-data.iloc[i+1, 3]))

df['DATE']=date
df['CLOSE']=close
df['PRED']=pred

df.to_csv('./可视化的数据/test_visual_3.csv', encoding='utf-8', index=False)
        