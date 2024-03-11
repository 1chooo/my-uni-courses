---
type: slide
title: 06/26 Report        # 簡報的名稱
tags: GS4524   # 簡報的標籤
slideOptions:        # 簡報相關的設定
  theme: solarized   # 顏色主題
  slideNumber: true
  # transition: 'fade' # 換頁動畫
keyboard: true
---

# 06/27 Briefing 📝
### Dataset Analysis

Third-Year @ Dept. ATM

Group1 109601003 林群賀

---

## The Problem We Solved

- Upload the dataset to kaggle
- Successfully link with **RTX3080**
- Rewrite the **sumo** `Installation Guide`
- Helping partner build the environment

---

### Dataset in kaggle

![](https://hackmd.io/_uploads/rJSnjoPun.png)


---

### Successfully link with **RTX3080**

![](https://hackmd.io/_uploads/SykZg2Pd2.png)


---


### Installation Guide 

with `pip virtualenv`

![](https://hackmd.io/_uploads/ByzEhiv_n.png)


---

### Installation Guide 

with `pip virtualenv`

```vim
git clone https://github.com/dslaborg/sumo.git
cd sumo    # enter the project root

virtualenv venv --python=python3.9.10    # Create the virtual env with pip
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

pip install ipykernel    # With jupyter notebook
pip install ipywidgets
```

---

## What I have learned yesterday?

- How to build the virtual env on Windows OS to adapt the new DEV ENV

---

## Difference in profession makes one feel worlds apart

---

## What I want to Solve today?

- Visualize the dataset formally
- Analyze the source code

---

# Reference

- [Part Physionet](https://www.kaggle.com/datasets/lchooo/part-physionet)
- [update: Installation Guide #6](https://github.com/dslaborg/sumo/pull/6)