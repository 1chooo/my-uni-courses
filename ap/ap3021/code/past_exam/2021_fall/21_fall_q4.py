# %% [markdown]
# # [2021 Fall] Final Exam - Question 4
# 
# > Course: AP3021

# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.fft import fft, fftfreq, ifft

# %% [markdown]
# 讀檔

# %%
df = pd.read_fwf('./data/test.dat.rtf',skiprows=8)

# %%
time=df.iloc[:, 1]
data=df.iloc[:, 7]
#print(df)
data=data.to_numpy()
#print(time)
#print(data)
n=48 #data amount
x = np.arange(0, n, 1)

plt.plot(data)
plt.title("zenith total delay")
plt.ylabel("zenith total delay")
plt.xlabel("Time (30min interval)")
plt.show()

# %%
y1= np.zeros(n, dtype=complex)  #轉完的資料為complex形式
yf = fft(data)

k=1                #晝、夜
y1[0]=yf[0]
y1[1:1+k-1]=yf[1:1+k-1]
y1[n-k:n]=yf[n-k:n]         
yt = ifft(y1,n)          

plt.title('Zenith total delay')
plt.ylabel('Zenith total delay')
plt.xlabel('Time (30min interval)')
#plt.axis([0.0, 20.0, 0.0, 6.0])
plt.plot(data, label = "Origional")
plt.plot(yt, label = "FFT")
plt.grid(True)
#plt.xticks(range(0, 21, 1))
#plt.yticks(range(0, 7, 1))
plt.legend()
#plt.savefig('Windspeed_High_Relation_fft.png')
plt.show()


