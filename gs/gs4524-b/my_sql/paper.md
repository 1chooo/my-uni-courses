# 論文閱讀進度

## Detecting sleep outside the clinic using wearable heart rate devices
###### Article Link: [click here](https://www.nature.com/articles/s41598-022-11792-7)

> View:
> ---
> 林群賀
> 賴應賢

### 林群賀：

#### 前文
- 手腕裝置缺陷（三缺）：
    - 不同數據及的適應性（不能混用）
    - 夜間以外的數據記錄
    - 依賴自我報告
- combine heart rate and movement sensor.

#### 方法介紹
- 四個數據集（這邊或許我們也可以用身份來劃分，針對不同數據集做不同處理已找最後總結出協調的結果）

#### 延伸探討
為了得知我們所使用的 Garmin Watch 是何種 Sensor Type？
* [What is Advanced Sleep Monitoring in Garmin Connect?](https://support.garmin.com/en-US/?faq=mBRMf4ks7XAQ03qtsbI8J6)
* [Why Does Garmin Connect Show Missing Heart Rate Readings During Sleep?](https://support.garmin.com/en-US/?faq=1N1Rm5YV3Y9NhC5F6DYcf8)

### 賴應賢：
HRV和疲勞之間存在一定程度的負相關

### 心得



---

## Generalisable machine learning models trained on heart rate variability data to predict mental fatigue

> View:
> ---
> 陳暐鈞
> 張博鈞


### 陳暐鈞

### 心得
僅使用HRV訓練的模型能夠有效地檢測疲勞，最佳accuracy得分範圍在75％至91％之間

Task-related：該文章中使用了被測試者在完成特定認知任務期間所產生的生理數據，來訓練機器學習算法，以檢測疲勞。
基於Task-related訓練的算法的優勢可能僅適用於HRV，並不一定推廣到其他生理測量（例如，EEG腦電圖測量）。

測試受試者主觀感受是否疲勞：VAS視覺類比量表（Visual Analog Scale），通常由一條長度為100毫米的直線構成，兩端標註有極端的描述詞（例如“無疲勞”和“疲勞”）。 受試者被要求在這條線上標記他們感覺的位置，從而測量他們的感受程度。被廣泛用於測量疼痛、焦慮、疲勞等感覺。

結論：透過機器學習基於HRV數據來檢測疲勞是有效的，（分類和回歸模型）均包括非線性分析（熵、Poincaré圖、去趨勢的波動分析detrended fLuctuation analyses）獲取的HRV指標都是特別重要的疲勞預測因素。
### 張博鈞
### 心得
睡眠窗口（the final sleep window）的特徵：
1.在睡眠開始的前四個小時，清醒的時間不超過90分鐘
2.在前四個小時和後60分鐘具有高心率波動時期
最終睡眠窗口定義為開始和結束的最後一個和第一個高波動時期，這樣做是為了找出精準的睡眠時長，避免掉賴床或者準備睡覺的時間。

<b>所以我們可以跟數據去做比較驗證上面的特徵有沒有出現，再進一步地去找睡眠窗口</b>

另外，論文裡面也提到了小睡和被叫醒(awakenings)兩種狀況
小睡在主睡眠窗口的兩側會有180分鐘的緩衝窗口
awakenings的狀況我不太確定是什麼意思，但論文裡面寫說會比白天(8.-22.)從累積分布函數圖的分位臨界值高

<b>因此在分析數據上也可以注意這兩種狀況</b>


---
# 或許有機會讀的論文
## Mental fatigue detection using a wearable commodity device and machine learning

## Detection of mental fatigue state with wearable ECG devices

## Performance of seven consumer sleep-tracking devices compared with polysomnography
##### Article Link [click here](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8120339/)