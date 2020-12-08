from __future__ import print_function
import tensorflow as tf
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import openpyxl as opxl
import pandas as pd
from datetime import datetime

DATA_DIR = "./test_data"
DATA_FILE = os.path.join(DATA_DIR, "test_bachu.json")
DUMP_FILE = os.path.join(DATA_DIR, "test_bachu.pkl")


def import_data():
    """
    현재 가격과 날씨, 재배면적 데이터를 하나의 데이터 프레임으로 생성
    """
    price = pd.read_excel('./test_data/test_price_data(bachu).xlsx')
    weather = pd.read_excel('./test_data/test_weather_data.xlsx')
    area = pd.read_csv('.\data\KOSIS_재배면적_데이터\시도별_채소_재배면적.csv', encoding='CP949')

    is_onion = area['항목'] == '배추계'
    is_sum = area['종류별'] == '합계'
    onion_area = area[is_onion & is_sum]

    onion_area = onion_area.drop(['단위', '종류별','항목'],1) # 항목 버림
    onion_area = onion_area[onion_area['시도별'] != '계']
    onion_area = onion_area[onion_area['시도별'] != '충청도']
    onion_area = onion_area.fillna(0) #결측치 채우기
    onion_area = onion_area.set_index('시도별')
    print(onion_area.head(n=20))

    ##날짜 기준으로 모든 데이터 묶기
    is_area1 =  weather['지역(시)'] == '강원도'
    area_1 = weather[is_area1]
    area_1 = area_1.drop(['지역(시)', '최고기온', '최저기온','운량','적설량','순간최대풍속'],1) # 항목 버림
    is_area2 =  weather['지역(시)'] == '경기도'
    area_2 = weather[is_area2]
    area_2 = area_2.drop(['지역(시)', '최고기온', '최저기온','운량','적설량','순간최대풍속'],1) # 항목 버림
    is_area3 =  weather['지역(시)'] == '경상남도'
    area_3 = weather[is_area3]
    area_3 = area_3.drop(['지역(시)', '최고기온', '최저기온','운량','적설량','순간최대풍속'],1) # 항목 버림
    is_area4 =  weather['지역(시)'] == '경상북도'
    area_4 = weather[is_area4]
    area_4 = area_4.drop(['지역(시)', '최고기온', '최저기온','운량','적설량','순간최대풍속'],1) # 항목 버림
    is_area5 =  weather['지역(시)'] == '광주'
    area_5 = weather[is_area5]
    area_5 = area_5.drop(['지역(시)', '최고기온', '최저기온','운량','적설량','순간최대풍속'],1) # 항목 버림
    is_area6 =  weather['지역(시)'] == '대구'
    area_6 = weather[is_area6]
    area_6 = area_6.drop(['지역(시)', '최고기온', '최저기온','운량','적설량','순간최대풍속'],1) # 항목 버림
    is_area7 =  weather['지역(시)'] == '대전'
    area_7 = weather[is_area7]
    area_7 = area_7.drop(['지역(시)', '최고기온', '최저기온','운량','적설량','순간최대풍속'],1) # 항목 버림
    is_area8 =  weather['지역(시)'] == '부산'
    area_8 = weather[is_area8]
    area_8 = area_8.drop(['지역(시)', '최고기온', '최저기온','운량','적설량','순간최대풍속'],1) # 항목 버림
    is_area9 =  weather['지역(시)'] == '서울'
    area_9 = weather[is_area9]
    area_9 = area_9.drop(['지역(시)', '최고기온', '최저기온','운량','적설량','순간최대풍속'],1) # 항목 버림
    is_area10 =  weather['지역(시)'] == '울산'
    area_10 = weather[is_area10]
    area_10 = area_10.drop(['지역(시)', '최고기온', '최저기온','운량','적설량','순간최대풍속'],1) # 항목 버림
    is_area11 =  weather['지역(시)'] == '인천'
    area_11 = weather[is_area11]
    area_11 = area_11.drop(['지역(시)', '최고기온', '최저기온','운량','적설량','순간최대풍속'],1) # 항목 버림
    is_area12 =  weather['지역(시)'] == '전라남도'
    area_12 = weather[is_area12]
    area_12 = area_12.drop(['지역(시)', '최고기온', '최저기온','운량','적설량','순간최대풍속'],1) # 항목 버림
    is_area13 =  weather['지역(시)'] == '전라북도'
    area_13 = weather[is_area13]
    area_13 = area_13.drop(['지역(시)', '최고기온', '최저기온','운량','적설량','순간최대풍속'],1) # 항목 버림
    is_area14 =  weather['지역(시)'] == '제주특별자치도'
    area_14 = weather[is_area14]
    area_14 = area_14.drop(['지역(시)', '최고기온', '최저기온','운량','적설량','순간최대풍속'],1) # 항목 버림
    is_area15 =  weather['지역(시)'] == '충청남도'
    area_15 = weather[is_area15]
    area_15 = area_15.drop(['지역(시)', '최고기온', '최저기온','운량','적설량','순간최대풍속'],1) # 항목 버림
    is_area16 =  weather['지역(시)'] == '충청북도'
    area_16 = weather[is_area16]
    area_16 = area_16.drop(['지역(시)', '최고기온', '최저기온','운량','적설량','순간최대풍속'],1) # 항목 버림

    print(area_1.head())
    area_total_1 = pd.merge(area_1, area_2, on='거래일자', suffixes=('_강원도','_경기도'))
    area_total_2 = pd.merge(area_1, area_2, on='거래일자', suffixes=('_경상남도','_경상북도'))
    area_total_3 = pd.merge(area_1, area_2, on='거래일자', suffixes=('_광주','_대구'))
    area_total_4 = pd.merge(area_1, area_2, on='거래일자', suffixes=('_대전','_부산'))
    area_total_5 = pd.merge(area_1, area_2, on='거래일자', suffixes=('_서울','_울산'))
    area_total_6 = pd.merge(area_1, area_2, on='거래일자', suffixes=('_인천','_전라남도'))
    area_total_7 = pd.merge(area_1, area_2, on='거래일자', suffixes=('_전라북도','_제주특별자치도'))
    area_total_8 = pd.merge(area_1, area_2, on='거래일자', suffixes=('_충청남도','_충청북도'))
    
    area_total = pd.merge(area_total_1, area_total_2, on='거래일자')
    area_total = pd.merge(area_total, area_total_3, on='거래일자')
    area_total = pd.merge(area_total, area_total_4, on='거래일자')
    area_total = pd.merge(area_total, area_total_5, on='거래일자')
    area_total = pd.merge(area_total, area_total_6, on='거래일자')
    area_total = pd.merge(area_total, area_total_7, on='거래일자')
    area_total = pd.merge(area_total, area_total_8, on='거래일자')

    #벡터에 재배면적 합치기
    
    area_total['서울_재배면적'] = np.nan
    area_total['부산_재배면적'] = np.nan
    area_total['대구_재배면적'] = np.nan
    area_total['인천_재배면적'] = np.nan
    area_total['광주_재배면적'] = np.nan
    area_total['대전_재배면적'] = np.nan
    area_total['울산_재배면적'] = np.nan
    area_total['경기도_재배면적'] = np.nan
    area_total['강원도_재배면적'] = np.nan
    area_total['충청북도_재배면적'] = np.nan
    area_total['충청남도_재배면적'] = np.nan
    area_total['전라북도_재배면적'] = np.nan
    area_total['전라남도_재배면적'] = np.nan
    area_total['경상북도_재배면적'] = np.nan
    area_total['경상남도_재배면적'] = np.nan
    area_total['제주특별자치도_재배면적'] = np.nan

    for row in area_total.index :
       nowyear = area_total['거래일자'][row].year
       strIndex = str(nowyear) + " 년"
       area_total['서울_재배면적'][row] = onion_area[strIndex]['서울']
       area_total['부산_재배면적'][row] = onion_area[strIndex]['부산']
       area_total['대구_재배면적'][row] = onion_area[strIndex]['대구']
       area_total['인천_재배면적'][row] = onion_area[strIndex]['인천']
       area_total['광주_재배면적'][row] = onion_area[strIndex]['광주']
       area_total['대전_재배면적'][row] = onion_area[strIndex]['대전']
       area_total['울산_재배면적'][row] = onion_area[strIndex]['울산']
       area_total['경기도_재배면적'][row] = onion_area[strIndex]['경기도']
       area_total['강원도_재배면적'][row] = onion_area[strIndex]['강원도']
       area_total['충청북도_재배면적'][row] = onion_area[strIndex]['충청북도']
       area_total['충청남도_재배면적'][row] = onion_area[strIndex]['충청남도']
       area_total['전라북도_재배면적'][row] = onion_area[strIndex]['전라북도']
       area_total['전라남도_재배면적'][row] = onion_area[strIndex]['전라남도']
       area_total['경상북도_재배면적'][row] = onion_area[strIndex]['경상북도']
       area_total['경상남도_재배면적'][row] = onion_area[strIndex]['경상남도']
       area_total['제주특별자치도_재배면적'][row] = onion_area[strIndex]['제주특별자치도']


    area_total = pd.merge(area_total, price, how="left", left_on='거래일자', right_on='날짜')
    area_total = area_total.drop(['날짜'],1) # 항목 버림
    area_total = area_total.fillna(method="bfill") #결측치 채우기
    print(area_total.tail())
    
    return area_total

def dump_dataframes(dataframes):
    pd.to_pickle(dataframes, DUMP_FILE)


def load_dataframes():
    return pd.read_pickle(DUMP_FILE)

def remove_comma(x):
    if (str(type(x))== "<class 'str'>"):
        return x.replace(',','')
    else :
        return x

def multivariate_data(dataset, target, start_index, end_index, history_size,
                        target_size, single_step=False):
    data = []
    labels = []

    start_index = start_index + history_size
    if end_index is None:
        end_index = len(dataset) - target_size

    for i in range(start_index, end_index):
        indices = range(i-history_size, i)
        data.append(dataset[indices])

        if(single_step):
            labels.append(target[i+target_size])
        else:
            labels.append(target[i:i+target_size])

    return np.array(data), np.array(labels)


def test_LSTM(dataframes):
    past_history = 42
    future_target = 14
    BATCH_SIZE = 1024
    BUFFER_SIZE = 100
    EVALUATION_INTERVAL = 500
    EPOCHS = 20

    _x = dataframes
    _y = dataframes[:,96]
    print(_x[0:10])
    print(_y[0:10])
    x_train_multi, y_train_multi = multivariate_data(_x, _y, 0, None, past_history, future_target)
    x_val_multi, y_val_multi = multivariate_data(_x, _y, TRAIN_SPLIT, None, past_history, future_target)

    train_data_multi = tf.data.Dataset.from_tensor_slices((x_train_multi, y_train_multi))
    train_data_multi = train_data_multi.cache().batch(BATCH_SIZE).repeat()

    val_data_multi = tf.data.Dataset.from_tensor_slices((x_val_multi, y_val_multi))
    val_data_multi = val_data_multi.batch(BATCH_SIZE).repeat()

    multi_step_model = tf.keras.models.load_model("./onion_model/onion_42_21_1024")
    
    #multi-step 예층
    for x,y in val_data_multi.take(3):
        multi_step_plot(x[0], y[0], multi_step_model.predict(x)[0])

def test_onion():
    #1. 미리 위에서 처리한 test_price_data와 기존 학습 데이터인 /data/category.pkl을 합친다
    category_name = "onion"
    origin_data = pd.read_pickle("./data/onion.pkl")
    test_data = pd.read_pickle("./test_data/test_onion.pkl")
    data = pd.concat([origin_data, test_data], ignore_index=True)
    #print(data.tail(n=42)) 

    #2. 합친 데이터를 기준으로 표준화 

    mask = (data['거래일자'] > '2001-01-01') & (data['거래일자'] < '2020-10-06')
    df = data.loc[mask]
    df = df.set_index('거래일자')
    df['평균'] = df['평균'].apply(remove_comma)
    df['평균'] = pd.to_numeric(df['평균'])
    df = df.fillna(method="bfill") #결측치 채우기
    #print(df.tail(n=42))   #결측치가 없는지 확인

    dataset = df.values
    data_mean = dataset[0:len(dataset)].mean(axis=0)
    data_std = dataset[0:len(dataset)].std(axis=0)
    dataset = (dataset-data_mean)/data_std
    #print(dataset.shape) (7211, 97)

    #3. 밑에서 42일만 잘라서 test_LSTM
    test_x = dataset[7169:]
    #print(test_x)
    test_x_new = test_x[np.newaxis,:]
    #print(test_x.shape) (42,97)
    print(test_x_new.shape)
    multi_step_model = tf.keras.models.load_model("./onion_42_21_128")
    print(multi_step_model.predict(test_x_new))

    #이 결과를 다시 정규화 해제
    test_result = multi_step_model.predict(test_x_new)
    print(data_std[96]) 
    test_result_denormal = (test_result*data_std[96])+data_mean[96]
    print(test_result_denormal)

    return test_result_denormal

def test_carrot():
    #1. 미리 위에서 처리한 test_price_data와 기존 학습 데이터인 /data/category.pkl을 합친다
    origin_data = pd.read_pickle("./data/carrot.pkl")
    test_data = pd.read_pickle("./test_data/test_carrot.pkl")
    data = pd.concat([origin_data, test_data], ignore_index=True)
    #print(data.tail(n=42)) 

    #2. 합친 데이터를 기준으로 표준화 

    mask = (data['거래일자'] > '2001-01-01') & (data['거래일자'] < '2020-10-06')
    df = data.loc[mask]
    df = df.set_index('거래일자')
    df['평균'] = df['평균'].apply(remove_comma)
    df['평균'] = pd.to_numeric(df['평균'])
    df = df.fillna(method="bfill") #결측치 채우기
    #print(df.tail(n=42))   #결측치가 없는지 확인

    dataset = df.values
    data_mean = dataset[0:len(dataset)].mean(axis=0)
    data_std = dataset[0:len(dataset)].std(axis=0)
    dataset = (dataset-data_mean)/data_std
    #print(dataset.shape) (7211, 97)

    #3. 밑에서 42일만 잘라서 test_LSTM
    test_x = dataset[7169:]
    #print(test_x)
    test_x_new = test_x[np.newaxis,:]
    #print(test_x.shape) (42,97)
    print(test_x_new.shape)
    multi_step_model = tf.keras.models.load_model("./carrot_model/carrot_42_21_1024")
    print(multi_step_model.predict(test_x_new))

    #이 결과를 다시 정규화 해제
    test_result = multi_step_model.predict(test_x_new)
    print(data_std[96]) 
    test_result_denormal = (test_result*data_std[96])+data_mean[96]
    print(test_result_denormal)

    return test_result_denormal

def test_bachu():
    #1. 미리 위에서 처리한 test_price_data와 기존 학습 데이터인 /data/category.pkl을 합친다
    origin_data = pd.read_pickle("./data/bachu.pkl")
    test_data = pd.read_pickle("./test_data/test_bachu.pkl")
    data = pd.concat([origin_data, test_data], ignore_index=True)
    #print(data.tail(n=42)) 

    #2. 합친 데이터를 기준으로 표준화 

    mask = (data['거래일자'] > '2001-01-01') & (data['거래일자'] < '2020-10-06')
    df = data.loc[mask]
    df = df.set_index('거래일자')
    df['평균'] = df['평균'].apply(remove_comma)
    df['평균'] = pd.to_numeric(df['평균'])
    df = df.fillna(method="bfill") #결측치 채우기
    #print(df.tail(n=42))   #결측치가 없는지 확인

    dataset = df.values
    data_mean = dataset[0:len(dataset)].mean(axis=0)
    data_std = dataset[0:len(dataset)].std(axis=0)
    dataset = (dataset-data_mean)/data_std
    #print(dataset.shape) (7211, 97)

    #3. 밑에서 42일만 잘라서 test_LSTM
    test_x = dataset[7169:]
    #print(test_x)
    test_x_new = test_x[np.newaxis,:]
    #print(test_x.shape) (42,97)
    print(test_x_new.shape)
    multi_step_model = tf.keras.models.load_model("./bachu_model/bachu_42_21_1024")
    print(multi_step_model.predict(test_x_new))

    #이 결과를 다시 정규화 해제
    test_result = multi_step_model.predict(test_x_new)
    print(data_std[96]) 
    test_result_denormal = (test_result*data_std[96])+data_mean[96]
    print(test_result_denormal)

    return test_result_denormal

def test_garlic():
    #1. 미리 위에서 처리한 test_price_data와 기존 학습 데이터인 /data/category.pkl을 합친다
    origin_data = pd.read_pickle("./data/garlic.pkl")
    test_data = pd.read_pickle("./test_data/test_garlic.pkl")
    data = pd.concat([origin_data, test_data], ignore_index=True)
    #print(data.tail(n=42)) 

    #2. 합친 데이터를 기준으로 표준화 

    mask = (data['거래일자'] > '2001-01-01') & (data['거래일자'] < '2020-10-06')
    df = data.loc[mask]
    df = df.set_index('거래일자')
    df['평균'] = df['평균'].apply(remove_comma)
    df['평균'] = pd.to_numeric(df['평균'])
    df = df.fillna(method="bfill") #결측치 채우기
    #print(df.tail(n=42))   #결측치가 없는지 확인

    dataset = df.values
    data_mean = dataset[0:len(dataset)].mean(axis=0)
    data_std = dataset[0:len(dataset)].std(axis=0)
    dataset = (dataset-data_mean)/data_std
    #print(dataset.shape) (7211, 97)

    #3. 밑에서 42일만 잘라서 test_LSTM
    test_x = dataset[7169:]
    #print(test_x)
    test_x_new = test_x[np.newaxis,:]
    #print(test_x.shape) (42,97)
    print(test_x_new.shape)
    multi_step_model = tf.keras.models.load_model("./garlic_model/garlic_42_21_1024")
    print(multi_step_model.predict(test_x_new))

    #이 결과를 다시 정규화 해제
    test_result = multi_step_model.predict(test_x_new)
    print(data_std[96]) 
    test_result_denormal = (test_result*data_std[96])+data_mean[96]
    print(test_result_denormal)

    return test_result_denormal



def main():
    predict_onion = test_onion().tolist()
    predict_carrot = test_carrot().tolist()
    predict_bachu = test_bachu().tolist()
    predict_garlic = test_garlic().tolist()
    dt_index = pd.date_range(start='20201006', end='20201019')
    dt_list = dt_index.strftime("%Y.%m.%d").tolist()
    dt_list_list=[]
    dt_list_list.append(dt_list)
    print(predict_onion[0])
    print(dt_list)


    dict_data = {'양파':predict_onion[0], '당근':predict_carrot[0], '배추': predict_bachu[0], '마늘': predict_garlic[0], '라벨':dt_list}
    #df = pd.DataFrame(dict_data)

    #print(df)
    #df.to_excel('./test_data/predict_result3.xlsx')
    return dict_data







if __name__ == "__main__":
    main()

