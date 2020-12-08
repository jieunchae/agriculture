from __future__ import print_function
import tensorflow as tf
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import openpyxl as opxl
import pandas as pd
from datetime import datetime

DATA_DIR = "./data"
DATA_FILE = os.path.join(DATA_DIR, "garlic.json")
DUMP_FILE = os.path.join(DATA_DIR, "garlic.pkl")

def import_data():
    """
    현재 양파 가격과 날씨, 재배면적 데이터를 하나의 데이터 프레임으로 생성
    """
    price = pd.read_excel('price_data(garlic).xlsx')
    weather = pd.read_excel('weather_data.xlsx')
    area = pd.read_csv('.\data\KOSIS_재배면적_데이터\시도별_채소_재배면적.csv', encoding='CP949')

    is_onion = area['항목'] == '마늘'
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

def remove_comma(x):
    if (str(type(x))== "<class 'str'>"):
        return x.replace(',','')
    else :
        return x

def dump_dataframes(dataframes):
    pd.to_pickle(dataframes, DUMP_FILE)


def load_dataframes():
    return pd.read_pickle(DUMP_FILE)

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

def create_time_steps(length):
    return list(range(-length,0))

#샘플 데이터 포인트 플로팅
def multi_step_plot(history, true_future, prediction):
    plt.figure(figsize=(12,6))
    num_in = create_time_steps(len(history))
    num_out = len(true_future)

    plt.plot(num_in, np.array(history[:,96]), label='History')
    plt.plot(np.arange(num_out), np.array(true_future), 'bo', label = 'True Future')

    if prediction.any():
        plt.plot(np.arange(num_out), np.array(prediction), 'ro', label='Predicted Future')
    plt.legend(loc='upper left')
    plt.show()

def plot_train_history(history, title):
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    
    epochs = range(len(loss))

    plt.figure()

    plt.plot(epochs, loss, 'b', label='Training loss')
    plt.plot(epochs, val_loss, 'r', label='Validation loss')
    plt.title(title)
    plt.legend()

    plt.show()

def predict_LSTM(dataframes):
    past_history = 42
    future_target = 14
    TRAIN_SPLIT = int(len(dataframes)*0.7)   #70퍼
    BATCH_SIZE = 1024
    BUFFER_SIZE = 100
    EVALUATION_INTERVAL = 500
    EPOCHS = 20


    print(dataframes.shape)
    _x = dataframes
    _y = dataframes[:,96]
    print(_x[0:10])
    print(_y[0:10])
    x_train_multi, y_train_multi = multivariate_data(_x, _y, 0, None, past_history, future_target)
    x_val_multi, y_val_multi = multivariate_data(_x, _y, TRAIN_SPLIT, None, past_history, future_target)
    print(x_train_multi[0].shape)
    print(y_train_multi[0].shape)

    train_data_multi = tf.data.Dataset.from_tensor_slices((x_train_multi, y_train_multi))
    train_data_multi = train_data_multi.cache().batch(BATCH_SIZE).repeat()

    val_data_multi = tf.data.Dataset.from_tensor_slices((x_val_multi, y_val_multi))
    val_data_multi = val_data_multi.batch(BATCH_SIZE).repeat()

    #for x,y in train_data_multi.take(1):
    #    multi_step_plot(x[0], y[0], np.array([0]))

    multi_step_model = tf.keras.models.Sequential()
    multi_step_model.add(tf.keras.layers.LSTM(97, return_sequences=True, input_shape=x_train_multi.shape[-2:]))
    multi_step_model.add(tf.keras.layers.LSTM(97, activation='relu'))
    multi_step_model.add(tf.keras.layers.Dense(14))

    multi_step_model.compile(optimizer=tf.keras.optimizers.Adam(clipvalue=1.0), loss='mae')

    for x,y in val_data_multi.take(1):
        print(multi_step_model.predict(x).shape)

    multi_step_history = multi_step_model.fit(train_data_multi, epochs=EPOCHS, steps_per_epoch=EVALUATION_INTERVAL,
                                            validation_data=val_data_multi, validation_steps=100)
    plot_train_history(multi_step_history, 'Multi-Step Training and validation loss')

    #multi-step 예층
    for x,y in val_data_multi.take(10):
        multi_step_plot(x[0], y[0], multi_step_model.predict(x)[0])

    multi_step_model.save("./garlic_model/garlic_42_21_1024")

def test_LSTM(dataframes):
    past_history = 42
    future_target = 14
    TRAIN_SPLIT = int(len(dataframes)*0.8)   #60퍼
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

    multi_step_model = tf.keras.models.load_model("./garlic_model/garlic_42_21_1024")
    
    #multi-step 예층
    for x,y in val_data_multi.take(3):
        multi_step_plot(x[0], y[0], multi_step_model.predict(x)[0])




def main():
    #데이터는 한번만 실행하면 됨
    print("[*] Parsing data...")
    data = import_data()
    print("[+] Done")

    print("[*] Dumping data...")
    dump_dataframes(data)
    print("[+] Done\n")

    data = load_dataframes()

    mask = (data['거래일자'] > '2001-01-01') & (data['거래일자'] < '2020-09-01')
    df = data.loc[mask]
    df = df.set_index('거래일자')
    df['평균'] = df['평균'].apply(remove_comma)
    df['평균'] = pd.to_numeric(df['평균'])
    print(df.head())

    #표준화
    #TRAIN_SPLIT = int(len(df)*0.7)   #70퍼
    dataset = df.values
    data_mean = dataset[0:len(dataset)].mean(axis=0)
    data_std = dataset[0:len(dataset)].std(axis=0)
    dataset = (dataset-data_mean)/data_std
    
    predict_LSTM(dataset)
    test_LSTM(dataset)




if __name__ == "__main__":
    main()
