# %% [markdown]
# # The **Monthly Mean** Analysis.
# 
# ## Import the package we need.

# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import glob
from PIL import Image

# %% [markdown]
# ## Locate the local file. 

# %%
# print(os.getcwd().split("/"))

def get_data_path(data_type) :

    data_path = os.getcwd()

    data_path = data_path.split("/")
    # print(data_path)
    data_path[5] = 'src'
    data_path[6] = 'data'
    data_path.append("")
    data_path[7] = data_type

    temp = ""

    for i in range(0, len(data_path)) :
        temp += data_path[i] + "/"
    
    data_path = temp
    # print(data_path)

    return data_path

# %%
data_path = ""
data_type = "monthly_mean"

data_path = get_data_path(data_type)
print(data_path)

os.chdir(data_path)

# %% [markdown]
# ## $CO_2$
# 
# ### Load data
# 
# First, we read the data and observe the type of the data.

# %%
def load_data(data_path, type, skip_rows, data_title) :
    
        for file in os.listdir() :
            if file.startswith(f"{type}") :
                file_path = f"{data_path}/{file}"
                data = pd.read_csv(file_path, skiprows=skip_rows, sep="\s+")
                data = data.replace(-0.99, 0)
                data = data.replace(-9.99, 0)
                data = data.replace(-1   , 0)
                data.columns = data_title

        return data

# %%
type = "co2"
skip_rows = 53
data_title = ["year", "month", "date", "avg", "de-s", "day", "std", "unc"]
co2_monthly_mean_data = load_data(data_path, type, skip_rows, data_title)

print(co2_monthly_mean_data)

# %% [markdown]
# ### Plot for the monthly mean.
# 
# After we load the data what we need. Then we plot the relationship between the data. First, we pick up the diversity of season and the average change of the month.

# %%
plt.figure(figsize=(20, 15))
plt.plot(co2_monthly_mean_data["date"], co2_monthly_mean_data["de-s"], "k-o")
plt.plot(co2_monthly_mean_data["date"], co2_monthly_mean_data["avg"], "r-o")

plt.xlabel("Year", fontsize=20)
plt.ylabel("CO2 mole fraction (ppm)", fontsize=20)
plt.title("Atomospheric CO2 at Mauna Loa Observatory", fontsize=24)

# plt.tick_params(axis="both", labelsize=16, color="red")
plt.tick_params(axis="both", labelsize=16)
plt.legend(["CO2 average", "CO2 season"], loc ="lower right")

plt.grid()
# plt.savefig("../../imgs/CO2/co2_monthly_mean.jpg", dpi=300)
plt.savefig("../../imgs/monthly_mean/co2_monthly_mean.jpg", dpi=300)
plt.show()

# %%
plt.figure(figsize=(20, 15))
plt.plot(co2_monthly_mean_data["date"], co2_monthly_mean_data["unc"], "-o")
# plt.plot(co2_monthly_mean_data["date"], co2_monthly_mean_data["avg"], "r-o")

plt.xlabel("Year", fontsize=20)
plt.ylabel("Uncertainty", fontsize=20)
plt.title("Atomospheric CO2 at Mauna Loa Observatory (Uncertainty)", fontsize=24)

# plt.tick_params(axis="both", labelsize=16, color="red")
plt.tick_params(axis="both", labelsize=16)
plt.legend(["Uncertainty", "CO2 season"], loc ="lower right")

plt.grid()
# plt.savefig("../../imgs/CO2/co2_monthly_mean.jpg", dpi=300)
plt.savefig("../../imgs/monthly_mean/co2_monthly_mean_uncertainty.jpg", dpi=300)
plt.show()

# %% [markdown]
# ### Plot for the recent monthly mean.

# %%
type = "co2"
skip_rows = 771
data_title = ["year", "month", "date", "avg", "de-s", "day", "std", "unc"]
co2_recent_monthly_mean_data = load_data(data_path, type, skip_rows, data_title)

print(co2_recent_monthly_mean_data)

# %% [markdown]
# ### Plot for the monthly mean.
# 
# After we load the data what we need. Then we plot the relationship between the data. First, we pick up the diversity of season and the average change of the month.

# %%
plt.figure(figsize=(20, 15))
plt.plot(co2_recent_monthly_mean_data["date"], co2_recent_monthly_mean_data["de-s"], "k-o")
plt.plot(co2_recent_monthly_mean_data["date"], co2_recent_monthly_mean_data["avg"], "r-o")

plt.xlabel("Year", fontsize=20)
plt.ylabel("CO2 mole fraction (ppm)", fontsize=20)
plt.title("Recent Monthly Mean CO2 at Mauna Loa Observatory", fontsize=24)

# plt.tick_params(axis="both", labelsize=16, color="red")
plt.tick_params(axis="both", labelsize=16)
plt.legend(["CO2 average", "CO2 season"], loc ="lower right")

plt.grid()
# plt.savefig("../../imgs/CO2/co2_recent_monthly_mean.jpg", dpi=300)
plt.savefig("../../imgs/monthly_mean/co2_recent_monthly_mean.jpg", dpi=300)
plt.show()

# %%
plt.figure(figsize=(20, 15))
plt.plot(co2_recent_monthly_mean_data["date"], co2_recent_monthly_mean_data["unc"], "-o")
# plt.plot(co2_recent_monthly_mean_data["date"], co2_recent_monthly_mean_data["avg"], "r-o")

plt.xlabel("Year", fontsize=20)
plt.ylabel("Uncertainty", fontsize=20)
plt.title("Recent Monthly Mean CO2 at Mauna Loa Observatory (Uncertainty)", fontsize=24)

# plt.tick_params(axis="both", labelsize=16, color="red")
plt.tick_params(axis="both", labelsize=16)
plt.legend(["Uncertainty", "CO2 season"], loc ="lower right")

plt.grid()
# plt.savefig("../../imgs/CO2/co2_monthly_mean.jpg", dpi=300)
plt.savefig("../../imgs/monthly_mean/co2_recent_monthly_mean_uncertainty.jpg", dpi=300)
plt.show()

# %% [markdown]
# ## $CH_4$
# 
# ### Load data
# 
# First, we read the data and observe the type of the data.

# %%
type = "ch4"
skip_rows = 64
data_title = ["year", "month", "date", "avg", "avg_unc", "trend", "trend_unc"]
ch4_monthly_mean_data = load_data(data_path, type, skip_rows, data_title)

print(ch4_monthly_mean_data)

# %% [markdown]
# ### Plot for the monthly mean.
# 
# After we load the data what we need. Then we plot the relationship between the data. First, we pick up the trend and the average change of the month.

# %%
plt.figure(figsize=(20, 15))
plt.plot(ch4_monthly_mean_data["date"], ch4_monthly_mean_data["avg"], "k-o")
plt.plot(ch4_monthly_mean_data["date"], ch4_monthly_mean_data["trend"], "r-o")


plt.xlabel("Year", fontsize=20)
plt.ylabel("CH4 mole fraction (ppb)", fontsize=20)
plt.title("Globaly Monthly Mean CH4", fontsize=24)

plt.tick_params(axis="both", labelsize=16)
plt.legend(["CH4 average", "CH4 trend"], loc ="lower right")

plt.grid()
# plt.savefig("../../imgs/CH4/ch4_monthly_mean.jpg", dpi=300)
plt.savefig("../../imgs/monthly_mean/ch4_monthly_mean.jpg", dpi=300)
plt.show()

# %%
plt.figure(figsize=(20, 15))
plt.plot(ch4_monthly_mean_data["date"], ch4_monthly_mean_data["avg_unc"], "k-o")
plt.plot(ch4_monthly_mean_data["date"], ch4_monthly_mean_data["trend_unc"], "r-o")


plt.xlabel("Year", fontsize=20)
plt.ylabel("Uncertainty", fontsize=20)
plt.title("Globaly Monthly Mean CH4 Uncertainty", fontsize=24)

plt.tick_params(axis="both", labelsize=16)
plt.legend(["CH4 average uncertainty", "CH4 trend uncertainty"], loc ="lower right")

plt.grid()
# plt.savefig("../../imgs/CH4/ch4_monthly_mean.jpg", dpi=300)
plt.savefig("../../imgs/monthly_mean/ch4_monthly_mean_uncertainty.jpg", dpi=300)
plt.show()

# %%
type = "ch4"
skip_rows = 478
data_title = ["year", "month", "date", "avg", "avg_unc", "trend", "trend_unc"]
ch4_recent_monthly_mean_data = load_data(data_path, type, skip_rows, data_title)

print(ch4_recent_monthly_mean_data)

# %% [markdown]
# ## Plot for the recent monthly mean.

# %%
plt.figure(figsize=(20, 15))
plt.plot(ch4_recent_monthly_mean_data["date"], ch4_recent_monthly_mean_data["avg"], "r-o")
plt.plot(ch4_recent_monthly_mean_data["date"], ch4_recent_monthly_mean_data["trend"], "k-o")


plt.xlabel("Year", fontsize=20)
plt.ylabel("CH4 mole fraction (ppb)", fontsize=20)
plt.title("Recent Global Monthly Mean CH4", fontsize=24)

plt.tick_params(axis="both", labelsize=16)
plt.legend(["CH4 average", "CH4 trend"], loc ="lower right")

plt.grid()
# plt.savefig("../../imgs/CH4/ch4_recent_monthly_mean.jpg", dpi=300)
plt.savefig("../../imgs/monthly_mean/ch4_recent_monthly_mean.jpg", dpi=300)
plt.show()

# %%
plt.figure(figsize=(20, 15))
plt.plot(ch4_recent_monthly_mean_data["date"], ch4_recent_monthly_mean_data["avg_unc"], "k-o")
plt.plot(ch4_recent_monthly_mean_data["date"], ch4_recent_monthly_mean_data["trend_unc"], "r-o")


plt.xlabel("Year", fontsize=20)
plt.ylabel("Uncertainty", fontsize=20)
plt.title("Recent Globaly Monthly Mean CH4 Uncertainty", fontsize=24)

plt.tick_params(axis="both", labelsize=16)
plt.legend(["CH4 average uncertainty", "CH4 trend uncertainty"], loc ="lower right")

plt.grid()
# plt.savefig("../../imgs/CH4/ch4_monthly_mean.jpg", dpi=300)
plt.savefig("../../imgs/monthly_mean/ch4_recent_monthly_mean_uncertainty.jpg", dpi=300)
plt.show()

# %% [markdown]
# ## $N_{2}O$
# 
# ### Load data
# 
# First, we read the data and observe the type of the data.

# %%
type = "n2o"
skip_rows = 64
data_title = ["year", "month", "date", "avg", "avg_unc", "trend", "trend_unc"]
n2o_monthly_mean_data = load_data(data_path, type, skip_rows, data_title)

print(n2o_monthly_mean_data)

# %% [markdown]
# ### Plot for the monthly mean.
# 
# After we load the data what we need. Then we plot the relationship between the data. First, we pick up the trend and the average change of the month.

# %%
plt.figure(figsize=(20, 15))
plt.plot(n2o_monthly_mean_data["date"], n2o_monthly_mean_data["avg"], "r-o")
plt.plot(n2o_monthly_mean_data["date"], n2o_monthly_mean_data["trend"], "k-o")


plt.xlabel("Year", fontsize=20)
plt.ylabel("N2O mole fraction (ppb)", fontsize=20)
plt.title("Globaly Monthly Mean N2O", fontsize=24)

plt.tick_params(axis="both", labelsize=16)
plt.legend(["N2O average", "N2O trend"], loc ="lower right")

plt.grid()
# plt.savefig("../../imgs/N2O/n2o_monthly_mean.jpg", dpi=300)
plt.savefig("../../imgs/monthly_mean/n2o_monthly_mean.jpg", dpi=300)
plt.show()

# %%
plt.figure(figsize=(20, 15))
plt.plot(n2o_monthly_mean_data["date"], n2o_monthly_mean_data["avg_unc"], "r-o")
plt.plot(n2o_monthly_mean_data["date"], n2o_monthly_mean_data["trend_unc"], "k-o")


plt.xlabel("Year", fontsize=20)
plt.ylabel("Uncertainty", fontsize=20)
plt.title("Globaly Monthly Mean N2O Uncertainty", fontsize=24)

plt.tick_params(axis="both", labelsize=16)
plt.legend(["N2O average uncertainty", "N2O trend uncertainty"], loc ="lower right")

plt.grid()
# plt.savefig("../../imgs/N2O/n2o_monthly_mean.jpg", dpi=300)
plt.savefig("../../imgs/monthly_mean/n2o_monthly_mean_uncertainty.jpg", dpi=300)
plt.show()

# %%
type = "n2o"
skip_rows = 268
data_title = ["year", "month", "date", "avg", "avg_unc", "trend", "trend_unc"]
n2o_recent_monthly_mean_data = load_data(data_path, type, skip_rows, data_title)

print(n2o_recent_monthly_mean_data)

# %% [markdown]
# ### Plot for the recent monthly mean.

# %%
plt.figure(figsize=(20, 15))
plt.plot(n2o_recent_monthly_mean_data["date"], n2o_recent_monthly_mean_data["avg"], "r-o")
plt.plot(n2o_recent_monthly_mean_data["date"], n2o_recent_monthly_mean_data["trend"], "k-o")


plt.xlabel("Year", fontsize=20)
plt.ylabel("n2o mole fraction (ppb)", fontsize=20)
plt.title("Recent Global Monthly Mean N2O", fontsize=24)

plt.tick_params(axis="both", labelsize=16)
plt.legend(["N2O average", "N2O trend"], loc ="lower right")

plt.grid()
# plt.savefig("../../imgs/n2o/n2o_recent_monthly_mean.jpg", dpi=300)
plt.savefig("../../imgs/monthly_mean/n2o_recent_monthly_mean.jpg", dpi=300)
plt.show()

# %%
plt.figure(figsize=(20, 15))
plt.plot(n2o_recent_monthly_mean_data["date"], n2o_recent_monthly_mean_data["avg_unc"], "r-o")
plt.plot(n2o_recent_monthly_mean_data["date"], n2o_recent_monthly_mean_data["trend_unc"], "k-o")


plt.xlabel("Year", fontsize=20)
plt.ylabel("Uncertainty", fontsize=20)
plt.title("Recent Globaly Monthly Mean N2O Uncertainty", fontsize=24)

plt.tick_params(axis="both", labelsize=16)
plt.legend(["N2O average uncertainty", "N2O trend uncertainty"], loc ="lower right")

plt.grid()
# plt.savefig("../../imgs/N2O/n2o_monthly_mean.jpg", dpi=300)
plt.savefig("../../imgs/monthly_mean/n2o_recent_monthly_mean_uncertainty.jpg", dpi=300)
plt.show()

# %% [markdown]
# ## $SF_{6}$
# 
# ### Load data
# 
# First, we read the data and observe the type of the data.

# %%
type = "sf6"
skip_rows = 63
data_title = ["year", "month", "date", "avg", "avg_unc", "trend", "trend_unc"]
sf6_monthly_mean_data = load_data(data_path, type, skip_rows, data_title)

print(sf6_monthly_mean_data)

# %%
plt.figure(figsize=(20, 15))
plt.plot(sf6_monthly_mean_data["date"], sf6_monthly_mean_data["avg"], "r-o")
plt.plot(sf6_monthly_mean_data["date"], sf6_monthly_mean_data["trend"], "k-o")


plt.xlabel("Year", fontsize=20)
plt.ylabel("SF6 mole fraction (ppb)", fontsize=20)
plt.title("Globaly Monthly Mean SF6", fontsize=24)

plt.tick_params(axis="both", labelsize=16)
plt.legend(["SF6 average", "SF6 trend"], loc ="lower right")

plt.grid()
# plt.savefig("../../imgs/SF6/sf6_monthly_mean.jpg", dpi=300)
plt.savefig("../../imgs/monthly_mean/sf6_monthly_mean.jpg", dpi=300)
plt.show()

# %%
plt.figure(figsize=(20, 15))
plt.plot(sf6_monthly_mean_data["date"], sf6_monthly_mean_data["avg_unc"], "r-o")
plt.plot(sf6_monthly_mean_data["date"], sf6_monthly_mean_data["trend_unc"], "k-o")


plt.xlabel("Year", fontsize=20)
plt.ylabel("Uncertainty", fontsize=20)
plt.title("Globaly Monthly Mean SF6 Uncertainty", fontsize=24)

plt.tick_params(axis="both", labelsize=16)
plt.legend(["SF6 average uncertainty", "SF6 trend certainty"], loc ="lower right")

plt.grid()
# plt.savefig("../../imgs/SF6/sf6_monthly_mean.jpg", dpi=300)
plt.savefig("../../imgs/monthly_mean/sf6_monthly_mean_certainty.jpg", dpi=300)
plt.show()

# %% [markdown]
# ### Plot for the monthly mean.
# 
# After we load the data what we need. Then we plot the relationship between the data. First, we pick up the trend and the average change of the month.

# %% [markdown]
# ### Plot for the recent monthly mean.

# %%
type = "sf6"
skip_rows = 310
data_title = ["year", "month", "date", "avg", "avg_unc", "trend", "trend_unc"]
sf6_recent_monthly_mean_data = load_data(data_path, type, skip_rows, data_title)

print(sf6_recent_monthly_mean_data)

# %%
plt.figure(figsize=(20, 15))
plt.plot(sf6_recent_monthly_mean_data["date"], sf6_recent_monthly_mean_data["avg"], "r-o")
plt.plot(sf6_recent_monthly_mean_data["date"], sf6_recent_monthly_mean_data["trend"], "k-o")


plt.xlabel("Year", fontsize=20)
plt.ylabel("SF6 mole fraction (ppb)", fontsize=20)
plt.title("Recent Global Monthly Mean SF6", fontsize=24)

plt.tick_params(axis="both", labelsize=16)
plt.legend(["SF6 average", "SF6 trend"], loc ="lower right")

plt.grid()
# plt.savefig("../../imgs/SF6/sf6_recent_monthly_mean.jpg", dpi=300)
plt.savefig("../../imgs/monthly_mean/sf6_recent_monthly_mean.jpg", dpi=300)
plt.show()

# %%
plt.figure(figsize=(20, 15))
plt.plot(sf6_monthly_mean_data["date"], sf6_monthly_mean_data["avg_unc"], "r-o")
plt.plot(sf6_monthly_mean_data["date"], sf6_monthly_mean_data["trend_unc"], "k-o")


plt.xlabel("Year", fontsize=20)
plt.ylabel("Uncertainty", fontsize=20)
plt.title("Recent Globaly Monthly Mean SF6 Uncertainty", fontsize=24)

plt.tick_params(axis="both", labelsize=16)
plt.legend(["SF6 average uncertainty", "SF6 trend certainty"], loc ="lower right")

plt.grid()
# plt.savefig("../../imgs/SF6/sf6_monthly_mean.jpg", dpi=300)
plt.savefig("../../imgs/monthly_mean/sf6_recent_monthly_mean_certainty.jpg", dpi=300)
plt.show()

# %% [markdown]
# ## Add my own watermark
# 
# ![plot](../../src/imgs/1chooo/icon.png)

# %%
def add_water_mark(imgs_path, type) :
        os.chdir(imgs_path)

        imgs = glob.glob(f'./*.jpg')
        icon = Image.open('../1chooo/icon.png')
        icon_w, icon_h = icon.size

        for i in imgs:
            name = i.split('/')[::-1][0]   
            img = Image.open(i)    
            img_w, img_h = img.size

            x = int((img_w + icon_w))
            y = int((img_h + icon_h))
            # x = int(img_w - icon_w)
            # y = int(img_h - icon_h)
            img.paste(icon, (750, 550), icon)   
            img.save(f'../watermark/{type}/{name}')

        return

# %%
def get_imgs_path() :
    
    imgs_path = os.getcwd().split("/")
    temp = ""

    imgs_path[6] = 'imgs'
    imgs_path[7] = 'monthly_mean'

    for i in range(0, len(imgs_path)) :
        temp += imgs_path[i] + "/"
    
    imgs_path = temp
    
    # print(imgs_path)

    return imgs_path

# %%
imgs_path = get_imgs_path()

os.chdir(imgs_path)

type = "monthly_mean"

add_water_mark(imgs_path, type)

# %%



