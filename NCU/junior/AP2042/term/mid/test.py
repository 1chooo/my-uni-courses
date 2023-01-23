import os
import glob
from PIL import Image
from Load import Tool

data_path = r"/Users/linchunho/Developer/ATM-Chem/src/data/monthly_mean/"
imgs_path = r"/Users/linchunho/Developer/ATM-Chem/src/imgs/CO2/"
type = "co2"
skip_rows = 53
data_type = ["year", "month", "date", "avg", "de-s", "day", "std", "unc"]

data = Tool.load_data(data_path, type, skip_rows, data_type)

water_mark = Tool.add_water_mark(imgs_path)

print(data)

imgs_path = r"/Users/linchunho/Developer/ATM-Chem/src/imgs/CO2/"
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