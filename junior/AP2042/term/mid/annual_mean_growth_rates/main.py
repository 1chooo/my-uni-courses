# %% [markdown]
# # The **Annual Mean Growth** Analysis.
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
data_type = "annual_mean_growth_rates"

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
skip_rows = 59
data_title = ["year", "ann_inc", "unc"]
co2_annual_mean_growth_rates_data = load_data(data_path, type, skip_rows, data_title)

print(co2_annual_mean_growth_rates_data)

# %% [markdown]
# ### Plot for the Annaul mean.
# 
# After we load the data what we need. Then we plot the relationship between the data. First, we pick up the diversity of season and the average change of the year.

# %%
plt.figure(figsize=(20, 15))
plt.plot(co2_annual_mean_growth_rates_data["year"], co2_annual_mean_growth_rates_data["ann_inc"], "-o")

plt.xlabel("Year", fontsize=20)
plt.ylabel("CO2 annual growth rates", fontsize=20)
plt.title("Globaly Annual Mean Growth Rates CO2", fontsize=24)

# plt.tick_params(axis="both", labelsize=16, color="red")
plt.tick_params(axis="both", labelsize=16)
plt.legend(["CO2 growth rates"], loc ="lower right")

plt.grid()
plt.savefig(f"../../imgs/annual_mean_growth_rates/co2_annual_mean_growth_rates.jpg", dpi=300)
plt.show()

# %% [markdown]
# ### Observe Uncertainty

# %%
plt.figure(figsize=(20, 15))
plt.plot(co2_annual_mean_growth_rates_data["year"], co2_annual_mean_growth_rates_data["unc"], "-o")

plt.xlabel("Year", fontsize=20)
plt.ylabel("Uncertainty", fontsize=20)
plt.title("Globaly Annual Mean Growth Rates CO2 Uncertainty", fontsize=24)

# plt.tick_params(axis="both", labelsize=16, color="red")
plt.tick_params(axis="both", labelsize=16)
plt.legend(["CO2 growth rates unc"], loc ="lower right")

plt.grid()
plt.savefig(f"../../imgs/annual_mean_growth_rates/co2_annual_mean_growth_rates_unc.jpg", dpi=300)
plt.show()

# %% [markdown]
# ### Plot for the Recent Annaul mean.
# 
# After we load the data what we need. Then we plot the relationship between the data. First, we pick up the diversity of season and the average change of the year.

# %%
type = "co2"
skip_rows = 118
data_title = ["year", "ann_inc", "unc"]
co2_recent_annual_mean_growth_rates_data = load_data(data_path, type, skip_rows, data_title)

print(co2_recent_annual_mean_growth_rates_data)

# %%
plt.figure(figsize=(20, 15))
plt.plot(co2_recent_annual_mean_growth_rates_data["year"], co2_recent_annual_mean_growth_rates_data["ann_inc"], "-o")

plt.xlabel("Year", fontsize=20)
plt.ylabel("CO2 annual growth rates", fontsize=20)
plt.title("Recent Globaly Annual Mean Growth Rates CO2", fontsize=24)

# plt.tick_params(axis="both", labelsize=16, color="red")
plt.tick_params(axis="both", labelsize=16)
plt.legend(["CO2 growth rates"], loc ="lower right")

plt.grid()
plt.savefig(f"../../imgs/annual_mean_growth_rates/co2_recent_annual_mean_growth_rates.jpg", dpi=300)
plt.show()

# %%
plt.figure(figsize=(20, 15))
plt.plot(co2_recent_annual_mean_growth_rates_data["year"], co2_recent_annual_mean_growth_rates_data["unc"], "-o")

plt.xlabel("Year", fontsize=20)
plt.ylabel("Uncertainty", fontsize=20)
plt.title("Recent Globaly Annual Mean Growth Rates CO2 Uncertainty", fontsize=24)

# plt.tick_params(axis="both", labelsize=16, color="red")
plt.tick_params(axis="both", labelsize=16)
plt.legend(["CO2 growth rates unc"], loc ="lower right")

plt.grid()
plt.savefig(f"../../imgs/annual_mean_growth_rates/co2_recent_annual_mean_growth_rates_unc.jpg", dpi=300)
plt.show()

# %% [markdown]
# ## $CH_4$
# 
# ### Load data
# 
# First, we read the data and observe the type of the data.

# %%
type = "ch4"
skip_rows = 62
data_title = ["year", "ann_inc", "unc"]
ch4_annual_mean_growth_rates_data = load_data(data_path, type, skip_rows, data_title)

print(ch4_annual_mean_growth_rates_data)

# %% [markdown]
# ## Plot for the Annaul mean.
#  
#  After we load the data what we need. Then we plot the relationship between the data. First, we pick up the diversity of season and the average change of the year.

# %%
plt.figure(figsize=(20, 15))
plt.plot(ch4_annual_mean_growth_rates_data["year"], ch4_annual_mean_growth_rates_data["ann_inc"], "-o")

plt.xlabel("Year", fontsize=20)
plt.ylabel("CH4 annual growth rates", fontsize=20)
plt.title("Globaly Annual Mean Growth Rates CH4", fontsize=24)

# plt.tick_params(axis="both", labelsize=16, color="red")
plt.tick_params(axis="both", labelsize=16)
plt.legend(["CH4 growth rates"], loc ="lower right")

plt.grid()
plt.savefig(f"../../imgs/annual_mean_growth_rates/ch4_annual_mean_growth_rates.jpg", dpi=300)
plt.show()

# %%
plt.figure(figsize=(20, 15))
plt.plot(ch4_annual_mean_growth_rates_data["year"], ch4_annual_mean_growth_rates_data["unc"], "-o")

plt.xlabel("Year", fontsize=20)
plt.ylabel("Uncertainty", fontsize=20)
plt.title("Globaly Annual Mean Growth Rates CH4 Uncertainty", fontsize=24)

# plt.tick_params(axis="both", labelsize=16, color="red")
plt.tick_params(axis="both", labelsize=16)
plt.legend(["CH4 growth rates unc"], loc ="lower right")

plt.grid()
plt.savefig(f"../../imgs/annual_mean_growth_rates/ch4_annual_mean_growth_rates_unc.jpg", dpi=300)
plt.show()

# %%
type = "ch4"
skip_rows = 97
data_title = ["year", "ann_inc", "unc"]
ch4_recent_annual_mean_growth_rates_data = load_data(data_path, type, skip_rows, data_title)

print(ch4_recent_annual_mean_growth_rates_data)

# %%
plt.figure(figsize=(20, 15))
plt.plot(ch4_recent_annual_mean_growth_rates_data["year"], ch4_recent_annual_mean_growth_rates_data["ann_inc"], "-o")

plt.xlabel("Year", fontsize=20)
plt.ylabel("CH4 annual growth rates", fontsize=20)
plt.title("Recent Globaly Annual Mean Growth Rates CH4", fontsize=24)

# plt.tick_params(axis="both", labelsize=16, color="red")
plt.tick_params(axis="both", labelsize=16)
plt.legend(["CH4 growth rates"], loc ="lower right")

plt.grid()
plt.savefig(f"../../imgs/annual_mean_growth_rates/ch4_recent_annual_mean_growth_rates.jpg", dpi=300)
plt.show()

# %%
plt.figure(figsize=(20, 15))
plt.plot(ch4_recent_annual_mean_growth_rates_data["year"], ch4_recent_annual_mean_growth_rates_data["unc"], "-o")

plt.xlabel("Year", fontsize=20)
plt.ylabel("Uncertainty", fontsize=20)
plt.title("Recent Globaly Annual Mean CH4 Uncertainty", fontsize=24)

# plt.tick_params(axis="both", labelsize=16, color="red")
plt.tick_params(axis="both", labelsize=16)
plt.legend(["CH4 growth rates unc"], loc ="lower right")

plt.grid()
plt.savefig(f"../../imgs/annual_mean_growth_rates/ch4_recent_annual_mean_unc.jpg", dpi=300)
plt.show()

# %% [markdown]
# ## $N_{2}O$
# 
# ### Load data
# 
# First, we read the data and observe the type of the data.

# %%
type = "n2o"
skip_rows = 62
data_title = ["year", "ann_inc", "unc"]
n2o_annual_mean_growth_rates_data = load_data(data_path, type, skip_rows, data_title)

print(n2o_annual_mean_growth_rates_data)

# %%
plt.figure(figsize=(20, 15))
plt.plot(n2o_annual_mean_growth_rates_data["year"], n2o_annual_mean_growth_rates_data["ann_inc"], "-o")

plt.xlabel("Year", fontsize=20)
plt.ylabel("N2O annual growth rates", fontsize=20)
plt.title("Globaly Annual Mean Growth Rates N2O", fontsize=24)

# plt.tick_params(axis="both", labelsize=16, color="red")
plt.tick_params(axis="both", labelsize=16)
plt.legend(["N2O growth rates"], loc ="lower right")

plt.grid()
plt.savefig(f"../../imgs/annual_mean_growth_rates/n2o_annual_mean_growth_rates.jpg", dpi=300)
plt.show()

# %%
plt.figure(figsize=(20, 15))
plt.plot(n2o_annual_mean_growth_rates_data["year"], n2o_annual_mean_growth_rates_data["unc"], "-o")

plt.xlabel("Year", fontsize=20)
plt.ylabel("Uncertainty", fontsize=20)
plt.title("Globaly Annual Mean Growth Rates N2O Uncertainty", fontsize=24)

# plt.tick_params(axis="both", labelsize=16, color="red")
plt.tick_params(axis="both", labelsize=16)
plt.legend(["N2O growth rates unc"], loc ="lower right")

plt.grid()
plt.savefig(f"../../imgs/annual_mean_growth_rates/n2o_annual_mean_growth_rates_unc.jpg", dpi=300)
plt.show()

# %%
type = "n2o"
skip_rows = 80
data_title = ["year", "ann_inc", "unc"]
n2o_recent_annual_mean_growth_rates_data = load_data(data_path, type, skip_rows, data_title)

print(n2o_recent_annual_mean_growth_rates_data)

# %%
plt.figure(figsize=(20, 15))
plt.plot(n2o_recent_annual_mean_growth_rates_data["year"], n2o_recent_annual_mean_growth_rates_data["ann_inc"], "-o")

plt.xlabel("Year", fontsize=20)
plt.ylabel("N2O annual growth rates", fontsize=20)
plt.title("Recent Globaly Annual Mean Growth Rates N2O", fontsize=24)

# plt.tick_params(axis="both", labelsize=16, color="red")
plt.tick_params(axis="both", labelsize=16)
plt.legend(["N2O growth rates"], loc ="lower right")

plt.grid()
plt.savefig(f"../../imgs/annual_mean_growth_rates/n2o_recent_annual_mean_growth_rates.jpg", dpi=300)
plt.show()

# %%
plt.figure(figsize=(20, 15))
plt.plot(n2o_recent_annual_mean_growth_rates_data["year"], n2o_recent_annual_mean_growth_rates_data["unc"], "-o")

plt.xlabel("Year", fontsize=20)
plt.ylabel("Uncertainty", fontsize=20)
plt.title("Recent Globaly Annual Mean N2O Uncertainty", fontsize=24)

# plt.tick_params(axis="both", labelsize=16, color="red")
plt.tick_params(axis="both", labelsize=16)
plt.legend(["N2O growth rates unc"], loc ="lower right")

plt.grid()
plt.savefig(f"../../imgs/annual_mean_growth_rates/n2o_recent_annual_mean_growth_rates_unc.jpg", dpi=300)
plt.show()

# %% [markdown]
# ## $SF_{6}$
# 
# ### Load data
# 
# First, we read the data and observe the type of the data.

# %%
type = "sf6"
skip_rows = 62
data_title = ["year", "ann_inc", "unc"]
sf6_annual_mean_growth_rates_data = load_data(data_path, type, skip_rows, data_title)

print(sf6_annual_mean_growth_rates_data)

# %%
plt.figure(figsize=(20, 15))
plt.plot(sf6_annual_mean_growth_rates_data["year"], sf6_annual_mean_growth_rates_data["ann_inc"], "-o")

plt.xlabel("Year", fontsize=20)
plt.ylabel("SF6 annual growth rates", fontsize=20)
plt.title("Globaly Annual Mean Grwoth Rates SF6", fontsize=24)

# plt.tick_params(axis="both", labelsize=16, color="red")
plt.tick_params(axis="both", labelsize=16)
plt.legend(["SF6 growth rates"], loc ="lower right")

plt.grid()
plt.savefig(f"../../imgs/annual_mean_growth_rates/sf6_annual_mean_growth_rates.jpg", dpi=300)
plt.show()

# %%
plt.figure(figsize=(20, 15))
plt.plot(sf6_annual_mean_growth_rates_data["year"], sf6_annual_mean_growth_rates_data["unc"], "-o")

plt.xlabel("Year", fontsize=20)
plt.ylabel("Uncertainty", fontsize=20)
plt.title("Globaly Annual Mean Growth Rates SF6 Uncertainty", fontsize=24)

# plt.tick_params(axis="both", labelsize=16, color="red")
plt.tick_params(axis="both", labelsize=16)
plt.legend(["SF6 growth rates unc"], loc ="lower right")

plt.grid()
plt.savefig(f"../../imgs/annual_mean_growth_rates/sf6_annual_mean_growth_rates_unc.jpg", dpi=300)
plt.show()

# %%
type = "sf6"
skip_rows = 83
data_title = ["year", "ann_inc", "unc"]
sf6_recent_annual_mean_growth_rates_data = load_data(data_path, type, skip_rows, data_title)

print(sf6_recent_annual_mean_growth_rates_data)

# %%
plt.figure(figsize=(20, 15))
plt.plot(sf6_recent_annual_mean_growth_rates_data["year"], sf6_recent_annual_mean_growth_rates_data["ann_inc"], "-o")

plt.xlabel("Year", fontsize=20)
plt.ylabel("SF6 annual growth rates", fontsize=20)
plt.title("Recent Globaly Annual Mean Growth Rates SF6", fontsize=24)

# plt.tick_params(axis="both", labelsize=16, color="red")
plt.tick_params(axis="both", labelsize=16)
plt.legend(["SF6 growth rates"], loc ="lower right")

plt.grid()
plt.savefig(f"../../imgs/annual_mean_growth_rates/sf6_recent_annual_mean_growth_rates.jpg", dpi=300)
plt.show()

# %%
plt.figure(figsize=(20, 15))
plt.plot(n2o_recent_annual_mean_growth_rates_data["year"], n2o_recent_annual_mean_growth_rates_data["unc"], "-o")

plt.xlabel("Year", fontsize=20)
plt.ylabel("Uncertainty", fontsize=20)
plt.title("Recent Globaly Annual Mean Growth Rates N2O Uncertainty", fontsize=24)

# plt.tick_params(axis="both", labelsize=16, color="red")
plt.tick_params(axis="both", labelsize=16)
plt.legend(["N2O growth rates unc"], loc ="lower right")

plt.grid()
plt.savefig(f"../../imgs/annual_mean_growth_rates/n2o_recent_annual_mean_growth_rates_unc.jpg", dpi=300)
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
def get_imgs_path(type) :
    
    imgs_path = os.getcwd().split("/")
    temp = ""

    imgs_path[6] = 'imgs'
    imgs_path[7] = type

    for i in range(0, len(imgs_path)) :
        temp += imgs_path[i] + "/"
    
    imgs_path = temp
    
    # print(imgs_path)

    return imgs_path

# %%
type = "annual_mean_growth_rates"

imgs_path = get_imgs_path(type)

os.chdir(imgs_path)

add_water_mark(imgs_path, type)

# %% [markdown]
# 


