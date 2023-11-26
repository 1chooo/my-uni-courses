# %% [markdown]
# # [2022 Fall] Final Exam - Example of Reading Data
# 
# This is the example code to read the data from TAs.

# %%
import matplotlib.pyplot as plt
import numpy as np

### 颱風半徑和風速
radius, velocity = np.loadtxt("./data/TCVt.txt", unpack="true")

## 畫個圖
fig = plt.figure(figsize=(16, 12))
plt.plot(radius, velocity)

plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np

# T : environment virtual temperature
# Tv : virtual temperature
# Height : m
Height,T,Tv = np.loadtxt("./data/Sounding_data.txt",unpack="true")


fig = plt.figure(figsize=(16,12))
plt.plot(T,Height)
plt.title("Temperature Profile")
plt.ylabel("Height")
plt.xlabel("Temperature (K)")
plt.show()

# %%
import scipy.io as sio
import matplotlib.pyplot as plt

#讀資料
mat_contents = sio.loadmat("./data/cceqs.mat")
sorted(mat_contents.keys())
Tc = mat_contents['Tc'][0]
e = mat_contents['e'][0]

#確認資料
plt.scatter(Tc,e)
plt.title("Vapor Pressure vs Temperature")
plt.ylabel("Vapor Pressure (Pa)")
plt.xlabel("Temperature (degree Celsius)")

# %%
import matplotlib.pyplot as plt
import numpy as np

# T : Parcel virtual temperature
# Tv : Environment virtual temperature
# Height : 0--LFC(Level of free convection)  top--EL(Equilibrium level)
Height,T,Tv = np.loadtxt("./data/Sounding_data.txt",unpack="true")


fig = plt.figure(figsize=(16,12))
plt.plot(T,Height)
plt.title("Temperature Profile")
plt.ylabel("Height")
plt.xlabel("Temperature (K)")
plt.show()


