'''
@Author: your name
@Date: 2020-05-18 20:03:14
@LastEditTime: 2020-05-19 13:19:54
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \opms\hesuantest.py
'''
import pandas as pd
df = pd.read_excel('519hs1.xlsx',sheet_name = 0)
data = df.head()   #前五条记录
print ("概览表:\n{0}".format(data))
data = df.values
#print ("获取的所有值:\n{0}".format(data))
print ("输出列标题", df.columns.values)
data = df.ix[0].values
print (data)