# %% [markdown]
# # 2023 Final Exam 
# 
# ### Course: AP3021
# 
# ## Question 4

# %%
import matplotlib.pyplot as plt
import numpy as np

# %%
stnno,yyyymmddhh,Pressure,Rain,Temp,Wind = np.loadtxt("ground_station_data.txt",unpack="true")

# %%
fig = plt.figure(figsize=(16,12))
plt.plot(Temp)
plt.title("Month Temperature")
plt.ylabel("Temperature")
plt.xlabel("Data_perhour")
plt.legend(['Original'])
plt.grid()

plt.show()

# %% [markdown]
# ### The given data is the hourly surface data of February 2019. Please apply FFT to remove the diurnal component of this data set.

# %%
from scipy.fft import fft, fftfreq, ifft

# %% [markdown]
# ### Temperature

# %%
xs = np.arange(0, 672, 0.1)
Y = np.fft.fft(Temp)

fig = plt.figure(figsize=(16,12))
plt.plot(Temp)
plt.plot(Y)
plt.title("Month Temperature")
plt.ylabel("Temperature")
plt.xlabel("Data_perhour")
plt.legend(['Original', 'with FFT'])
plt.grid()

plt.show()

# %% [markdown]
# ### Pressure

# %%
xs = np.arange(0, 672, 1)
ys = Pressure[xs]
Y = np.fft.fft((ys))

fig = plt.figure(figsize=(16,12))
plt.plot(xs, ys)
plt.plot(Y)
plt.title("Month Pressure")
plt.ylabel("Pressure")
plt.xlabel("Data_perhour")
plt.legend(['Original', 'with FFT'])
plt.grid()

plt.show()

# %% [markdown]
# ### Rain

# %%
xs = np.arange(0, 672, 1)
ys = Rain[xs]
Y = np.fft.fft((ys))

fig = plt.figure(figsize=(16,12))
plt.plot(xs, ys)
plt.plot(Y)
plt.title("Month Rain")
plt.ylabel("Rain")
plt.xlabel("Data_perhour")
plt.legend(['Original', 'with FFT'])
plt.grid()

plt.show()

# %% [markdown]
# ### Wind

# %%
xs = np.arange(0, 672, 1)
ys = Wind[xs]
Y = np.fft.fft((ys))

fig = plt.figure(figsize=(16,12))
plt.plot(xs, ys)
plt.plot(Y)
plt.title("Month Wind")
plt.ylabel("Wind")
plt.xlabel("Data_perhour")
plt.legend(['Original', 'with FFT'])
plt.grid()

plt.show()

# %%



