[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/fJskUh3G)
# Python第1次作業

## 作業要求
修改`hw1_0.py`、`hw1_1.py`、`hw1_2.py`、`hw1_3.py`，根據下列要求完成作業。

* 只能更改 #---- 中的程式碼
* 不可以直接人工計算然後填入對應值!

### hw1_0.py
> 將價錢( 105、130 )用字串slice方式取出，並相加後，並賦值給變數 cost

```python
def hw1_0():
    string1 = "小明花105元買了蘋果"
    string2 = "小華花130元買了香蕉"
    #-------------------------------
    # 注意cost為字串(string)的型別
    # cost = # ...
    #-------------------------------
    return "小明和小華共花了" + cost + "元買水果"
```

### hw1_1.py
> 透過字串可使用的函式或方法，使用變數 str1 組合出 "ABCCCCdIIkGHH"，並賦值給 output

```python
def hw1_1():
    str1 = "abcdefghijk"
    output = ""
    #-------------------------------
    # output = # ...
    #-------------------------------
    return output
```

### hw1_2.py
> 美國國家儀器股份有限公司(股票代號 [NASDAQ：NATI](https://finance.yahoo.com/quote/NATI/))生產多款資料擷取裝置(DAQ, Data Acquisition)，DAQ用途為將電壓(類比訊號)轉換為電腦看得懂的數位訊號。由於感測器接收到如溫度或震動等物理量多使用電壓呈現，使用DAQ量測感測器輸出的電壓將可讓電腦讀取真實世界感測器的物理量。
> 一個DAQ主要的規格為電壓解析度與取樣速率。我們先來專注「電壓解析度」，舉例來說，一個具有10 bit解析度的DAQ可將最大量測電壓範圍(-10V ~ +10V)切分成2^10份，也就是最小可以量測到 (10-(-10))/2^10 V
> 現在你的實驗室想要購買DAQ量測訊號，請參考[USB-6001](https://www.ni.com/zh-tw/support/model.usb-6001.html)的[規格表](https://www.ni.com/pdf/manuals/374369a.pdf)，計算出USB-6001的最小量測電壓為何? 單位為伏特(V)，`output`的資料型態為浮點數。

```python
def hw1_2():
    output = 0
    #-------------------------------
    # output = # ....
    #-------------------------------
    return output
```

### hw1_3.py
> 請利用巢狀迴圈 (Nested loops) 製作出九九乘法表，請輸出以下樣式：
```
2 * 2 = 2
2 * 3 = 6
2 * 4 = 8
...(類推)...
2 * 9 = 18
==
3 * 2 = 6
...(類推)...
3 * 9 = 27
==
...(類推)...
==
9 * 2 = 18
...(類推)...
9 * 9 = 81
(注意這裡有一行)
```

```python
def hw1_3():
    output = ""
    #-------------------------------
    # output = # ....
    #-------------------------------
    return output
```

## 如何完成作業
1. 禁止抄襲，歡迎同學互相討論以完成作業
1. 可以使用ChatGPT，但必須使用註解說明那些程式碼使用了ChatGPT，使用後得到了甚麼啟發
1. 作業應包含解題內容，如直接貼答案，即使自動評分通過，仍會被人工判定為錯誤
1. 繳交期限：2023/11/8 23:59

