---
type: slide
title: 06/28 Report        # 簡報的名稱
tags: GS4524   # 簡報的標籤
slideOptions:        # 簡報相關的設定
  theme: solarized   # 顏色主題
  slideNumber: true
  # transition: 'fade' # 換頁動畫
keyboard: true
---

# 06/28 Briefing 📝
### Dataset Visualization

Third-Year @ Dept. ATM

Group1 109601003 林群賀

---

## The Problem We Solved

- Visualization the source dataset

---

### The training data

- `tr03-1010/`
    - `tr03-1010-arousal.mat`
    - `tr03-1010.arousal`
    - `tr03-1010.hea`
    - `tr03-1010.mat`

---

### Visualization ECG

Load data

```python=
import wfdb
import os
import matplotlib.pyplot as plt

record_name = 'tr03-1010'
record_path = os.path.join(train_path, record_name, record_name)
record = wfdb.rdrecord(record_path)
```

---

### Visualization ECG

```python=
ecg_data = record.p_signal[:, -1]

import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 200
time = np.arange(len(ecg_data)) / sampling_rate

plt.figure(figsize=(10, 4))
plt.plot(time, ecg_data)
plt.title('ECG')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
```

---

### Visualization ECG

![](https://hackmd.io/_uploads/r1j0JWFun.png)

---

### Visualization Sleep Stages

Load data

```python
import wfdb
import os
import matplotlib.pyplot as plt

record_name = 'tr03-1010'
record_path = os.path.join(train_path, record_name, record_name)
arousal = wfdb.rdann(record_path, 'arousal')
```

---

### Visualization Sleep Stages

Observe data

```py
set(arousal.__dict__.get('aux_note'))
```

```console=
{'(arousal_rera',
 '(resp_centralapnea',
 '(resp_hypopnea',
 '(resp_mixedapnea',
 '(resp_obstructiveapnea',
 'N1',
 'N2',
 'N3',
 'R',
 'W',
 'arousal_rera)',
 'resp_centralapnea)',
 'resp_hypopnea)',
 'resp_mixedapnea)',
 'resp_obstructiveapnea)'}
```


---

### Visualization Sleep Stages

```py
import mat73
import scipy.io

record_name = 'tr03-1010'

record_path = os.path.join(train_path, record_name, f'{record_name}-arousal.mat')
aasmlabel = mat73.loadmat(record_path)
```

---

### Visualization Sleep Stages

```python=
import matplotlib.pyplot as plt
import numpy as np

# Define the sleep stages of interest
sleep_stages = ['wake', 'nonrem1', 'nonrem2', 'nonrem3', 'rem',]

# Get the sleep stage labels
stage_labels = aasmlabel['data']['sleep_stages']

# Create a list to store the sleep stage values
stage_values = []

# Iterate over the sleep stages of interest and extract their values
for stage in sleep_stages:
    stage_values.append(stage_labels[stage])

# Combine the sleep stage values into a single array
sleep_data = np.vstack(stage_values)

# Plot the sleep stages
plt.figure(figsize=(10, 4))
plt.imshow(sleep_data, cmap='cool', aspect='auto')
plt.xlabel('Time')
plt.ylabel('Sleep Stage')
plt.title('Sleep Stages')
plt.yticks(np.arange(len(sleep_stages)), sleep_stages)
plt.colorbar(label='Stage Value')
plt.show()
```

---

### Visualization Sleep Stages

![](https://hackmd.io/_uploads/SJgnYbY_n.png)


---

## What I have learned yesterday?

- use `wfdb` to load data
- use `.mat` type data

---

## What I want to Solve today?

- ECG -> Heart Rate and BBI
- BBI -> Heart Rate
- Heart Rate, HRV v.s. Sleep Stage (Correlation?)

---

# Reference

- [awerdich/physionet](https://github.com/awerdich/physionet)
- [Heart Murmur Detection from Phonocardiogram Recordings: The George B. Moody PhysioNet Challenge 2022](https://moody-challenge.physionet.org/2022/)
- [physionet-visualization](https://www.kaggle.com/code/lchooo/physionet-visualization)