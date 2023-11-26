# %% [markdown]
# # [2021 Fall] Final Exam - Example of Reading Data
# 
# This is the example code to read the data from TAs.

# %% [markdown]
# (1) 以下為一探空資料，T矩陣是溫度(攝氏)，P矩陣是氣壓層(hPa)。

# %%
import numpy as np
import matplotlib.pyplot as plt

#讀資料
with open("./data/obs_2021-03-18_12_00_00.sound") as a:
    for i in range(2):
        head=a.readline()
    data=a.readlines()
    T,P=np.zeros((len(data)))*np.nan,np.zeros((len(data)))*np.nan
    for i,tmp in enumerate(data):
        T[i]=tmp.split()[3]
        P[i]=tmp.split()[0]

#確認資料
plt.figure(figsize=(3,9))      
#plt.plot(x,y)  
plt.scatter(T,P)
plt.gca().invert_yaxis()
plt.title("Temperature Profile")
plt.ylabel("Pressure (hPa)")
plt.xlabel("Temperature (degree Celsius)")

# %% [markdown]
# (3)以下資料為溫度(Tc,攝氏)與水氣(e,Pa)的資料

# %%
from os.path import dirname, join as pjoin
import scipy.io as sio
import matplotlib.pyplot as plt

#讀資料
mat_contents = sio.loadmat(r"./data/cceqs.mat")
sorted(mat_contents.keys())
#print(mat_contents)
Tc = mat_contents['Tc'][0]
e = mat_contents['e'][0]

#確認資料
#plt.plot(Tc,e)
plt.scatter(Tc,e)
plt.title("Vapor Pressure vs Temperature")
plt.ylabel("Vapor Pressure (Pa)")
plt.xlabel("Temperature (degree Celsius)")

# %% [markdown]
# (4)以下為一組GNSS zenith total delay的資料，data是zenith total delay， time是時間(string type)

# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.fft import fft, fftfreq, ifft

#讀檔
df = pd.read_fwf(r'./data/test.dat.rtf',skiprows=8)
time=df.iloc[:, 1]
data=df.iloc[:, 7]
#print(df)
data=data.to_numpy()
#print(time)
#print(data)
n=48 #data amount

plt.plot(data)
plt.title("zenith total delay")
plt.ylabel("zenith total delay")
plt.xlabel("Time (30min interval)")




