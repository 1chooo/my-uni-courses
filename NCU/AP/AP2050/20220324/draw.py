# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

m = Basemap(projection='ortho', lon_0=120, lat_0=-90, resolution="l",
           llcrnrlon=105, urcrnrlon=135)#, llcrnrlat=30, urcrnrlat=60

#projection:mill––miller,cyl––cylindrical,ortho––orthographic
#lon_0,lat_0:畫面中心的經度(-180~180)、緯度(-90~90)
#llcrnrlon,urcrnrlon:左右邊界經度；llcrnrlat=,urcrnrlat:下上邊界緯度
#resolution:解析度。c<l<h<f

m.drawcoastlines()#繪製海岸線
#m.drawcountries(color="red")#繪製國家邊界
#m.drawrivers(color="blue")#繪製河流
#m.drawmapboundary(color="pink", linewidth="10", fill_color="aqua")#繪製地圖邊框
#m.drawlsmask(land_color='lightgreen', ocean_color='aqua', lakes=True)#繪製高解析度的海陸影象，指定陸地和海洋的顏色
#m.fillcontinents(color='lightgreen', lake_color='bule')#通過填充海岸線多邊形為地圖著色
m.drawparallels(np.arange(-90, 90, 30), labels=[True, True, False, False])#繪製緯度線，是否在[左、右、上、下]加上標籤
m.drawmeridians(np.arange(-180, 180, 30), labels=[0, 0, 0, 1])#繪製經度線，是否在[左、右、上、下]加上標籤
m.etopo()#地形高度、海洋深度資料
#m.bluemarble()#地球是藍大理石
plt.title('109601005', fontsize=20)

fig = plt.gcf()
fig.savefig('hihi.png', dpi=400)

plt.show()#要放在最後一行