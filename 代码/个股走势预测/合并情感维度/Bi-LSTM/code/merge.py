# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 22:50:40 2020

@author: AAA
"""
import pandas as pd

# 暂时注释掉
'''
df = pd.read_csv('../data/preProcess/GeliNews_fenci.csv', header = None, encoding = 'utf-8')
df2 = pd.read_csv('./Geli_predict.csv', header = None, encoding = 'utf-8')
df['pred'] = df2[0]
df.to_csv(r'./Geli_predict_merge.csv',index=False)

df3 = pd.read_csv('../data/preProcess/ZhongxingNews_fenci.csv', header = None, encoding = 'utf-8')
df4 = pd.read_csv('./Zhongxing_predict.csv', header = None, encoding = 'utf-8')
df3['pred'] = df4[0]
df3.to_csv(r'./Zhongxing_predict_merge.csv',index=False)
'''

# 让负面情绪转成-1
# df3 = pd.read_csv('../data/preProcess/GeliNews_fenci.csv', header = None, encoding = 'utf-8')
# df4 = pd.read_csv('./Geli_predict.csv', header = None, encoding = 'utf-8')

"""df3 = pd.read_csv(
    'E:\学习文件\pytorch\大三下学期工作室项目——股票数据分析预测\stock-prediction-main\代码\个股走势预测\合并情感维度\Bi-LSTM\data\preProcess\TechNews_modified_500_fenci.csv',
    header=None,encoding='utf-8')
df4 = pd.read_csv('F:\股票预测测试\stock-prediction-main\代码\个股走势预测\合并情感维度\Bi-LSTM\code\最新可以运行的结果TechNewsbyXu_clean.csv',
                  header=None, encoding='utf-8')"""
'''df3 = pd.read_csv(
    'E:\学习文件\pytorch\大三下学期工作室项目——股票数据分析预测\stock-prediction-main\代码\个股走势预测\合并情感维度\Bi-LSTM\data\preProcess\TechNews_modified_500_fenci.csv',
    encoding='utf-8')'''
#df3 = pd.read_csv('E:\学习文件\pytorch\大三下学期工作室项目——股票数据分析预测\stock-prediction-main\数据集\中兴通讯新闻分词.csv',
     #             encoding='utf-8')
df4 = pd.read_csv('F:\股票预测测试\stock-prediction-main\代码\个股走势预测\合并情感维度\Bi-LSTM\code\中兴分词情感预测结果.csv',
                  encoding='utf-8')
df3 = pd.read_csv('E:\学习文件\pytorch\大三下学期工作室项目——股票数据分析预测\stock-prediction-main\数据集\中兴通讯新闻分词.csv',

                  encoding='utf-8')
# print(type(df4.iloc[3, 0]))

for i in range(0, len(df4)):
    if int(df4.iloc[i, 0]) == 0:
        df4.iloc[i, 0] = -1

df3['pred'] = df4['pred']
print(df4['pred'])
df3.to_csv(r'merge合并预测结果.csv', index=False)


