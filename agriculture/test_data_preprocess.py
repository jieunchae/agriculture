from __future__ import print_function
import numpy as np
import os
import openpyxl as opxl
import pandas as pd
from datetime import datetime

total_data = [] #리스트 생성

for yearnow in range(2020,2021):
    filename ='./test_data/가격정보_carrot.xlsx'
    price = pd.read_excel(filename)
    price = price.transpose()   #전치행렬

    #1. 평균만 남기고 없앤다
    price_avg = price[0]
    price_avg = price_avg.reset_index() 
    price_avg = price_avg.drop([0,1],0)
    price_avg.columns=['날짜', '평균']
    price_avg = price_avg.drop(2,0)
    price_avg = price_avg.dropna()
    print(price_avg[0:250])
    #2. 년도가 잘못 저장되어 있으므로 바꿔준다
    price_avg['날짜'] = pd.to_datetime(price_avg['날짜'],errors="coerce").fillna(0)
    price_avg['Month'] = price_avg['날짜'].dt.month
    price_avg['Day'] = price_avg['날짜'].dt.day

    for row in price_avg.index :
        try:
            price_avg['날짜'][row] = datetime(yearnow, price_avg['Month'][row], price_avg['Day'][row])
        except:
            continue

    price_avg = price_avg.drop(['Month','Day'],1)
    price_avg.reset_index(drop=True,inplace=True)

    #print(price_avg.head())

    for row in price_avg.index :
        total_data.append(
                [price_avg['날짜'][row], price_avg['평균'][row]]
            )

data_total = pd.DataFrame(data=total_data, columns=['날짜','평균'])
print(data_total.head())
data_total.to_excel('./test_data/test_price_data(carrot).xlsx', index=False)