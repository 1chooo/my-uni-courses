# %% [markdown]
# # The **Weekly Mean Growth** Analysis.
# 
# ## Import the package we need.

# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import glob
from PIL import Image

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
data_type = "weekly_mean"

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
                data = data.replace(-999.99, 0)
                data = data.replace(-9.99, 0)
                data = data.replace(-1   , 0)
                data.columns = data_title

        return data

# %%
type = "co2"
skip_rows = 48
data_title = ["year", "month", "day", "date", "mol", "days", "one", "ten", "inc"]
co2_weekly_mean_data = load_data(data_path, type, skip_rows, data_title)

print(co2_weekly_mean_data)

# %% [markdown]
# ### Plot for the Annaul mean.
# 
# After we load the data what we need. Then we plot the relationship between the data. First, we pick up the diversity of season and the average change of the year.

# %%
plt.figure(figsize=(20, 15))
plt.plot(co2_weekly_mean_data["year"], co2_weekly_mean_data["mol"], "-o")
plt.plot(co2_weekly_mean_data["year"], co2_weekly_mean_data["one"], "-o")
plt.plot(co2_weekly_mean_data["year"], co2_weekly_mean_data["ten"], "-o")

plt.xlabel("Year", fontsize=20)
plt.ylabel("CO2 mole fraction (ppm)", fontsize=20)
plt.ylim(300, 450)
plt.title("Globaly Weekly Mean CO2", fontsize=24)

# plt.tick_params(axis="both", labelsize=16, color="red")
plt.tick_params(axis="both", labelsize=16)
plt.legend(["CO2 weekly mean", "data in one year ago", "data in ten years ago"], loc ="lower right")

plt.grid()
plt.savefig(f"../../imgs/weekly_mean/co2_weekly_mean.jpg", dpi=300)
plt.show()

# %% [markdown]
# ## ecent Year

# %%
type = "co2"
skip_rows = 2326
data_title = ["year", "month", "day", "date", "mol", "days", "one", "ten", "inc"]
co2_recent_weekly_mean_data = load_data(data_path, type, skip_rows, data_title)

print(co2_recent_weekly_mean_data)

# %%
plt.figure(figsize=(20, 15))
plt.plot(co2_recent_weekly_mean_data["year"], co2_recent_weekly_mean_data["mol"], "-o")
plt.plot(co2_recent_weekly_mean_data["year"], co2_recent_weekly_mean_data["one"], "-o")
plt.plot(co2_recent_weekly_mean_data["year"], co2_recent_weekly_mean_data["ten"], "-o")

plt.xlabel("Year", fontsize=20)
plt.ylabel("CO2 mole fraction (ppm)", fontsize=20)
plt.ylim(300, 450)
plt.title("Globaly Recent Weekly Mean CO2", fontsize=24)

# plt.tick_params(axis="both", labelsize=16, color="red")
plt.tick_params(axis="both", labelsize=16)
plt.legend(["CO2 weekly mean", "data in one year ago", "data in ten years ago"], loc ="lower right")

plt.grid()
plt.savefig(f"../../imgs/weekly_mean/co2_recent_weekly_mean.jpg", dpi=300)
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
type = "weekly_mean"

imgs_path = get_imgs_path(type)

os.chdir(imgs_path)

add_water_mark(imgs_path, type)

# %%



