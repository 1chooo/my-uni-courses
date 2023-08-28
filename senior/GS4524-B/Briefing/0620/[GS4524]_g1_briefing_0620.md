---
type: slide
title: 06/20 Report        # 簡報的名稱
tags: GS4524   # 簡報的標籤
slideOptions:        # 簡報相關的設定
  theme: solarized   # 顏色主題
  slideNumber: true
  transition: 'fade' # 換頁動畫
keyboard: true
---


# 06/20 Briefing 📝
### Sleep Analysis
Third-Year @ Dept. ATM

109601003 林群賀

---

## The Thesis Topic 📖

Deep learning for automated sleep staging using instantaneous heart rate

---

## Exploring The Algorithm metioned in this thesis
### With Deep Learning Method
- Current: CNN
- Future: RNN

---

## The Current Method: CNN 🌪

- Not engineer any features
- Only Convolutional layers

---

## First Part about CNN 🌪

- 2 $Hz$ Time Series 72000 -> 1200 segments(30 sec slice)
- 1-D convolutional layers
- 1-d Convolution kernel=7 with dilation = 2, 4, 8, 16, 32
- `Droptout(rate=0.2)`
- `Leaky ReLU (α=0.15)`
- (1, 1200, 4) -> (1, 1200, 128)


---

## Second Part about CNN 🌪

- Kernel size still on 1
- Atrous or dilated convolutional blocks
- 1-d Convolution kernel=7 with dilation = 2, 4, 8, 16, 32
- two such dilated convolutional blocks without any pooling layers
- 1200 x 4


---

## The Future Method: RNN

Recurrent Structure -> **Memory**

---

## What I have learned yesterday?

- We can also use 1-D convolutional layer!
- the importance of Dealing with time series data is recalling -> **how to keep to memory**

---

## What I want to Solve today?

- Explore how to Build Convolutional layer with 1-D layer.
- Explore the potential of RNN.

---

# Reference

- [Deep learning for automated sleep staging using instantaneous heart rate](https://www.nature.com/articles/s41746-020-0291-x)

