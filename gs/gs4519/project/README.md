# 梅雨還是沒雨？

### Rainy Predict with Machine Learning techniques

[![project badge](https://img.shields.io/badge/1chooo-rain__prediction-informational)](https://github.com/1chooo/rain_prediction)
[![Made with Python](https://img.shields.io/badge/Python->=3.7-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")
[![License](https://img.shields.io/badge/License-MIT-blue)](./LICENSE "Go to license section")

<a href="https://colab.research.google.com/github/1chooo/ML-Rainy-Predict/blob/main/main.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

This project marks the end of the GS4519A course at NCU. 

We are using machine learning techniques to predict the likelihood of rain.

## Members

#### Group Four

|  Name  | Student Number | Divide and Conquer |
| :----: | :------------: | :----------------: |
| 林群賀  |    109601003   | data, GUI, report  |
| 王采琳  |    109601001   | data, code, report |
| 黃于恩  |    109601501   | data, code, report |
| 林晴葳  |    109601508   | data, code, report |
| 吳彥叡  |    109601510   |    code, report    |

## Getting Started
Python version `python3.10.1` with `gradio, scikit-learn, seaborn, pandas, numpy, matplotlib, joblib`
### Build `venv` for **MacOS**
```shell
$ pip3 install virtualenv
$ virtualenv venv --python=python3.10.1
$ source venv/bin/activate
$ pip install -r requirements.txt
$ deactivate
$ rm -rf venv     # remove the venv
```

### Build `venv` for Windows
```shell
$ pip install virtualenv
$ virtualenv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ deactivate
$ rmdir /s venv     # remove the venv
```

## Motivation

從古自今，天氣一直是影響人類生活和經濟發展的重大因素，因此科學家們不斷在尋找最佳的天氣預測方法，而目前普遍的做法是收集大量的觀測數據（氣溫、濕度、風向和風速、氣壓等等），並利用對大氣物理過程的認識來確定未來某地點大氣層的狀態。但由於大氣過程的複雜，因此現今天氣預測總是存在一定的誤差。

身為大氣系的學生，我們想試看看利用機器學習來預測天氣，就像鐵達尼號和房價預測，先給程式大量的歷史數據，從中尋找相關性高的變數，讓程式去訓練出最佳的預測模式。

我們想要預測五、六月的梅雨，所以上中央氣象局的資料庫下載了平鎮測站過去14年五月和六月的資料。


## Background

<br>

![Pressure](imgs/pressure.png)

* 高氣壓：下沉氣流，空氣塊溫度會升高，變乾燥。
* 低氣壓：上升氣流，上升冷卻達到飽和狀態，往往會凝結降雨。


![Temperature](imgs/temperature.png)

* 地面溫度較低：空氣便會冷卻收縮下沉，形成高壓。
* 地面溫度較高：空氣就會受熱膨脹上升，形成低壓。


![Wind](imgs/wind.png)

風對降雨的影響主要是通過把海洋水汽帶到大陸形成降雨，所以迎風岸降雨較多。


![Humidity](imgs/humidity.png)

相對濕度是指單位體積空氣中，實際水蒸氣和飽和水氣含量的百分比。

相對濕度愈高，代表環境愈潮濕，也反映了降雨、有霧的可能性。


## Data

[中央氣象局](https://www.cwb.gov.tw/V8/C/)

[觀測資料查詢](https://e-service.cwb.gov.tw/HistoryDataQuery/index.jsp)

## What we did?

### Drop unneeded data

``` python
df.drop(['ObsTime', 'SeaPres', 'StnPresMaxTime', 'StnPresMinTime'], axis = 1, inplace = True)
df.drop(['T Max Time', 'T Min Time', 'Td dew point'], axis = 1, inplace = True)
df.drop(['RHMinTime', 'WGustTime'], axis = 1, inplace = True)
df.drop(['PrecpHour', 'PrecpMax10', 'PrecpMax10Time', 'PrecpMax60', 'PrecpMax60Time'], axis = 1, inplace = True)
df.drop(['SunShine', 'SunShineRate', 'GloblRad', 'VisbMean'], axis = 1, inplace = True)
df.drop(['EvapA', 'UVI Max', 'UVI Max Time', 'Cloud Amount'], axis = 1, inplace = True) 
df.info()
```

### Replace the data unused

``` python
df = df.replace('...','-999')
df = df.replace('/','-999')


for i in range(854):
    for j in range(0, 13):
        if df.iloc[i, j] == '-999':
            df.iloc[i, j] = 0.0

df = pd.DataFrame(df, dtype = np.float)
```

我們先處理降雨量，因為有降水及代表有下雨，所以只要大於大於0就轉換為1，反之轉換為0。

有些資料我們打算用平均值來填補，並取到小數點後第一位

剩下的資料我們以眾數的方式來填補缺失值

### Model

``` python
X = df.drop(['Precp'], axis=1)
y = df['Precp']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

X_train,X_test, y_train,y_test = train_test_split(X, y, test_size=0.3, random_state=67)
lr = LogisticRegression(max_iter=200)
lr.fit(X_train, y_train)
predictions = lr.predict(X_test)
accuracy_score(y_test, predictions)
recall_score(y_test, predictions)
precision_score(y_test, predictions)
```

經過多次交叉測試後，發現什麼都沒有刪除，分數會最高


|               | Predict not rain | Predict rain |
| :-----------: | :--------------: | :----------: |
| True not rain |       149        |      19      |
|   True rain   |        24        |      65      |

### Export model

``` python
import joblib
joblib.dump(lr,'Precipitation_Predict.pkl',compress=3)
```


## How to improve?

* 蒐集更多數據
* 套用數學迴歸方法，且搭配數學公式，如此還可以篩選掉原先的極端值，保留對機器真正有用的學習。


## Reference

1. [DataFrame中的object转换成float](https://blog.csdn.net/wushaowu2014/article/details/78963709)
2. [文件檔頭資料](https://www.csie.ntu.edu.tw/~r91112/myDownload/WEB/html.html)
3. [Python Web Flask — 如何透過Form取得資料](https://medium.com/seaniap/python-web-flask-如何透過form取得資料-7a63ebf9ff1f)
4. [Flask - Bad Request The browser (or proxy) sent a request that this server could not understand [duplicate]](https://stackoverflow.com/questions/48780324/flask-bad-request-the-browser-or-proxy-sent-a-request-that-this-server-could)
5. [TypeError: __init__() got an unexpected keyword argument 'method'](https://stackoverflow.com/questions/42126772/typeerror-init-got-an-unexpected-keyword-argument-method)
6. [如何用python做后端寫網頁-flask框架](https://www.uj5u.com/ruanti/262589.html)
7. [中央氣象局](https://www.cwb.gov.tw/V8/C/)
8. [DataFrame中的object转换成float](https://blog.csdn.net/wushaowu2014/article/details/78963709)
