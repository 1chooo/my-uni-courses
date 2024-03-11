---
type: slide
title: 06/26 Report        # 簡報的名稱
tags: GS4524   # 簡報的標籤
slideOptions:        # 簡報相關的設定
  theme: solarized   # 顏色主題
  slideNumber: true
  transition: 'fade' # 換頁動畫
keyboard: true
---

# 06/26 Briefing 📝
### Dataset Analysis

Third-Year @ Dept. ATM

Group1 109601003 林群賀

---

## The problems We have met

- Cannot download the data
- The process of unzip is too slow 
- How to analyze the source dataset

---

## How to download Dataset?
```python
import requests

def download_file(url, save_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)
    print("Download Successfully!!!")

url = "https://ncu365-my.sharepoint.com/personal/ckchang_office365_ncu_edu_tw/_layouts/15/download.aspx?SourceUrl=%2Fpersonal%2Fckchang%5Foffice365%5Fncu%5Fedu%5Ftw%2FDocuments%2Fchallenge%2D2018%2D1%2E0%2E0%2Ephysionet%2Eorg%2Ezip"
save_path = "path/to/save/location/file.zip"  

download_file(url, save_path)
```

---

## How to unzip Dataset?

```python
import zipfile

def unzip_file(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print("Unzip Successfully!!!")

zip_path = '/Volumes/HoHo\'s SSD/GS4524/challenge-2018-1.0.0.physionet.org.zip'  
extract_path = '/Volumes/HoHo\'s SSD/GS4524/'  

unzip_file(zip_path, extract_path)
```

---

### The source dataset too messy.

![](https://hackmd.io/_uploads/rJDSIP8d2.png)


---

### Cleanup the source code
![](https://hackmd.io/_uploads/r1rD8vId3.png)

---

### Divide the Dataset into Small One

286 GB -> 56 GB

![](https://hackmd.io/_uploads/r1q3IDUu3.png)


---

### The tools that we can train the model

- RTX 3080
- Kaggle 
    - afordable for **100 GB** dataset
    - need to be **public**

![](https://hackmd.io/_uploads/ryR5cDIO2.png)

---

## What I have learned yesterday?

- How to use **Web Crawler** wisely
- Analyze the source code
- Divide the huge dataset

---

## What I want to Solve today?

- Visualize the source dataset with the materials supplied by Teacher

---

# Reference

- [Deep learning for automated sleep staging using instantaneous heart rate](https://www.nature.com/articles/s41746-020-0291-x)
- [AUPRC vs. AUC-ROC? [duplicate]](https://stats.stackexchange.com/questions/338826/auprc-vs-auc-roc)
- [Index of /physiobank/database/challenge/2018/](https://physionet.org/physiobank/database/challenge/2018/#files)