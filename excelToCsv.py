import pandas as pd
data = pd.read_excel('e98334945fbd99f0.xlsx','原始',index_col=0)
data.to_csv('data1.csv',encoding='utf-8')
data = pd.read_excel('5月机构分润（参考数据）.xlsx','Sheet1',index_col=0)
data.to_csv('data2.csv',encoding='utf-8')

