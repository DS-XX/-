import pandas as pd
df=pd.read_excel('F:\股票预测测试\stock-prediction-main\数据集\中兴通讯10-20财务数据.xlsx')
print(df)
index=len(df.index)
longcolumn=df.shape[1]
for i in range(index):
    for j in range(2,longcolumn):
        x1=str(df.iloc[i,j])
        if x1 == '0.0' or x1=="":
            df.drop(index=i,axis=0)
#df.to_excel('./删0后的财务数据.xlsx', index=False, encoding='utf-8')
print(df)