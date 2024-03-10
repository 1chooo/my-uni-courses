# %% [markdown]
# # [2022 Fall] Assignment4-9
# 
# > Course: AP3021

# %% [markdown]
# ### 4-9
# 
# Please write Python codes to determine the height of temperature inversion? (data is in the eeclass)

# %%
import os
import pandas as pd
import matplotlib.pyplot as plt

# %%
""" Data type:
stno: Observation's Number (Length: 6 digits)
yyyymmddhh: UTC Time, yyyy: year, mm: month, dd: day, hh: hour (Length: 11 digits)
Si: Significant Code (Length: 3 digits)
Press: Pressure (Uint: hpa, Length: 7 digits)
Heigh: Geopotential Height (Unit: gpm, Length: 6 digits)
Tx: Temperature (Unit: degrees Celsius, Length: 6 digits)
Td: Dew Point (Unit: degrees Celsius, Length: 6 digits)
Wd: Wind Direction (Unit: degrees 360, Length: 4 digits)
Ws: Wind Speed (Unit: m/s, Length: 6 digits)
RH: Relative Humidity (Unit: %, Length: 4 digits)
"""

# Fetch the local path to read the info of the file.
data_path = os.getcwd()
file = "/src/data/20210101_upair.txt"
file_path = f"{data_path}/{file}"


data = pd.read_csv(file_path, skiprows=13, sep="\s+")
data = data.replace(-0.99, 0)
data = data.replace(-9.99, 0)
data = data.replace(-1   , 0)
# stno yyyymmddhh Si  Press Heigh    Tx    Td  Wd    Ws  RH
data.columns = ["stno", "date", "Si", "press", "heigh", "Tx", "Td", "Wd", "Ws", "Rh"]

print(data)

# %%
# At first we observe the realtionship between height and temperature

plt.plot(data["Tx"], data["heigh"])

plt.xlabel("Temperature(˚c)")
plt.ylabel("Height(gpm)")
plt.title("the realtionship between height and temperature")

plt.grid()
plt.legend(["temperature"], loc ="upper right")
plt.savefig("src/imgs/A4_9_1.jpg", dpi = 300)

plt.show()

# %%
# the key point we need is height and the temperature

data_num = len(data)
inversion_happen = []
x = []
y = []

for i in range(0, data_num) :
    if (i == data_num - 1) :
        break

    if (data["Tx"][i] < data["Tx"][i + 1]) :
        inversion_happen.append(i)
        print("Height:", data["heigh"][i], "Temperature inversion:", data["Tx"][i])
        x.append(data["Tx"][i])
        y.append(data["heigh"][i])


plt.plot(data["Tx"], data["heigh"])
plt.scatter(x, y, c='red')

plt.xlabel("Temperature(˚c)")
plt.ylabel("Height(gpm)")
plt.title("the realtionship between height and temperature")

plt.grid()
plt.legend(["temperature", "temperature inversion"], loc ="upper right")
plt.savefig("src/imgs/A4_9_2.jpg", dpi = 300)

plt.show()

# %%
y = data["press"].iloc[::-1]
plt.plot(data["Tx"], y)
plt.xlabel("Temperature(˚c)")
plt.ylabel("Pressure(hPa)")
plt.title("SkewT")

plt.grid()
plt.legend(["temperature", "temperature inversion"], loc ="upper right")
plt.savefig("src/imgs/A4_9_3.jpg", dpi = 300)

plt.show()


