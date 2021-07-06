# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 18:24:08 2019

@author: wuzix
"""
import re
import jieba
import pandas as pd
import jieba.analyse
#from zhon.hanzi import punctuation

text1='../../数据集/中兴通讯10-20新闻数据集.xlsx'
text2= '../../数据集/中兴新闻分词.csv'

jieba.load_userdict("../../数据集/stock_dict.txt")
jieba.analyse.set_stop_words('../../数据集/stopwords2.txt')

reg = "[^A-Za-z\u4e00-\u9fa5]"

f=pd.read_excel(text1)  # sep=',' ,encoding='utf-8',error_bad_lines=False
title=f.iloc[:,1]  #标题
outfile=open(text2,'w',encoding='utf-8')
results = pd.DataFrame()
news = []

def fenci(line):
    print(line)
    line = line.strip()
    line_result = re.sub(reg, '', line)
    return line_result


for line in title:
    line=str(line)
    kk = fenci(line)
    seg_list = jieba.cut(kk)
    descript = ''
    for word in seg_list:
        descript += word
        descript += " "
    # descript = " ".join(seg_list)
    print(descript)
    news.append(descript)

    # outfile.write(descript+'\n')
Date=[]
for i in f.iloc[:,0]:
    x1=str(i).split(" ")[0]
    Date.append(x1)
results['Date']=Date
results['Bid']='000063.SZ'
results['Descript'] = news
results.to_csv('./中兴新闻分词.csv', index=False, encoding='utf-8')


