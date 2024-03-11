---
type: slide
title: 06/29 Report        # 簡報的名稱
tags: GS4524   # 簡報的標籤
slideOptions:        # 簡報相關的設定
  theme: solarized   # 顏色主題
  slideNumber: true
  # transition: 'fade' # 換頁動畫
keyboard: true
---

# 06/29 Briefing 📝
### Dataset Analysis

Third-Year @ Dept. ATM

Group1 109601003 林群賀

---

### Previously on `SUMO` PRs

Merged!!!

![](https://hackmd.io/_uploads/rJepW6KOh.png)

---

### Build Windows DEV ENV (RTX3080)

- Brave Browser
- Visual Studio Code
- Git
- Python Intepreter
- Conda

---

### Conda Virtual ENV

```vim
conda create -n py39 python=3.9
pip install ipykernel
pip install numpy
pip install matplotlib
pip install wfdb
pip install mat73
pip install biosppy
pip install scipy
```

---

### Build Physionet project

![](https://hackmd.io/_uploads/H1hJ6LcOh.png)

---

### 💥 We are ready to train Physionet Dataset 💥


---

## What I have learned yesterday?

- In sum up the previous work

---

## What I want to Solve today?

- Keep finding the relationship between the dataset
- Modify the existing code to facilitate comprehensive model training

---

# Reference

- [我在 Conda 常用的指令](https://1chooo.github.io/2023/02/10/conda_command/)
- [part-physionet](https://www.kaggle.com/datasets/lchooo/part-physionet)