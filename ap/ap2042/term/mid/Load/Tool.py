import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import glob
from PIL import Image


class Tool :

    def load_data(data_path, type, skip_rows, data_type) :

        os.chdir(data_path)
        for file in os.listdir() :
            if file.startswith(f"{type}") :
                file_path = f"{data_path}/{file}"
                data = pd.read_csv(file_path, skiprows=skip_rows, sep="\s+")
                data = data.replace(-0.99, 0)
                data = data.replace(-9.99, 0)
                data = data.replace(-1   , 0)
                data.columns = data_type

        return data

    def add_water_mark(imgs_path) :
        os.chdir(imgs_path)

        imgs = glob.glob('./*.jpg')
        icon = Image.open('../1chooo/icon.png')
        icon_w, icon_h = icon.size

        for i in imgs:
            name = i.split('/')[::-1][0]   
            img = Image.open(i)    
            img_w, img_h = img.size
            x = int(img_w - icon_w)
            y = int(img_h - icon_h)
            img.paste(icon, (x, y), icon)   
            img.save(f'../watermark/{name}')

        return