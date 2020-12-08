from __future__ import print_function
import numpy as np
import os
import openpyxl as opxl
import pandas as pd
from datetime import datetime


total_onion = [] #리스트 생성

for yearnow in range(2001,2021):
    price = pd.read_excel('.\data\KAMIS_가격_데이터\onion\양파가격_%04d.xlsx'%(yearnow))
    price = price.transpose()   #전치행렬

    #1. 평균만 남기고 없앤다
    price_avg = price[0]
    price_avg = price_avg.reset_index() 
    price_avg = price_avg.drop([0,1],0)
    price_avg.columns=['날짜', '평균']

    #2. 년도가 잘못 저장되어 있으므로 바꿔준다
    price_avg['날짜'] = pd.to_datetime(price_avg['날짜'])
    price_avg['Month'] = price_avg['날짜'].dt.month
    price_avg['Day'] = price_avg['날짜'].dt.day
    for row in price_avg.index :
        price_avg['날짜'][row] = datetime(yearnow, price_avg['Month'][row], price_avg['Day'][row])

    price_avg = price_avg.drop(['Month','Day'],1)
    price_avg.reset_index(drop=True,inplace=True)

    #print(price_avg.head())

    for row in price_avg.index :
        total_onion.append(
                [price_avg['날짜'][row], price_avg['평균'][row]]
            )

data_onion = pd.DataFrame(data=total_onion, columns=['날짜','평균'])
print(data_onion.head())
data_onion.to_excel('price_data(onion).xlsx', index=False)



