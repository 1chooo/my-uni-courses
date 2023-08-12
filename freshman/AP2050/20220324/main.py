import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from mpl_toolkits.basemap import Basemap
from matplotlib.colors import LinearSegmentedColormap

pallete_name = "husl" #定義畫板格式
colors = sns.color_palette(pallete_name, 8)

colors.reverse()
cmap = mpl.colors.LinearSegmentedColormap.from_list(pallete_name, colors)
(y, x) = np.mgrid[-2:2.1:0.2, -2:2.2:0.2] #下界:上界:網格間距

z = x * np.exp(-x**2 - y**2)
(dx, dy) = np.gradient(z)

plt.title("1096001005", fontsize=20)
plt.quiver(x, y, dx, dy, z, cmap=cmap)#箭頭
plt.contour(x, y, z, 10, cmap=cmap)#輪廓
fig2 = plt.gcf()
fig2.savefig('hihi3.png', dpi=500)