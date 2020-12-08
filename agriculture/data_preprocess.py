from __future__ import print_function
import numpy as np
import os
import openpyxl as opxl
import pandas as pd
from dateutil.parser import parse
from datetime import datetime

#weather = opxl.load_workbook('.\data\OASIS_날씨_데이터\kma20200921153551627.xlsx', )
#현재 Active Sheet 얻기
weather = pd.read_excel('./test_data/kma20201007030713889.xlsx')
weather = weather.drop(['조사지역', '지역(군)'], axis=1)
weather_group = weather.groupby(["거래일자", "지역(시)"])  
weather = weather_group.mean().reset_index()                                # calculate mean

for row in weather.index :
    weather['거래일자'][row] = parse(str(weather['거래일자'][row]))

weather['거래일자'] = weather['거래일자'].dt.date

print(weather.head(n=10))
weather.to_excel('./test_data/test_weather_data.xlsx', index=False)
print("preprosessing_done!")