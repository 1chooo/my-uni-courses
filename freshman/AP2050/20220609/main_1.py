import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from getmac import get_mac_address as gma
mac = gma()

fig = plt.figure()
ax = Axes3D(fig)
def z_func(x, y):
    return x * np.exp(-x**2 - y**2)
x = y = np.arange(-2, 2.1, 0.2) #-2 to 2.1 每一點間隔0.2
X, Y = np.meshgrid(x, y) #生成網格
Z = z_func(X, Y)
ec = ax.plot_surface(X, Y, Z, cmap='plasma') #X, Y:用網格矩陣畫圖
                                             #cmap:plot_surface上顏色映射的組合方式，ex:plasma, coolwarm……
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z', fontsize=10, rotation=0)

cbar = plt.colorbar(ec, orientation='horizontal', shrink=0.5)# 定義colorbar(顏色條)是水平or垂直, 長度
cbar.set_label('Z')

plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='109601005 '+mac) #圖例，
fig.savefig('test3d__.png', dpi=300)
plt.show()





fig = plt.figure(figsize=(6, 6))
CS = plt.contour(X, Y, Z, 20)
cbar = plt.colorbar(CS, orientation = 'horizontal', shrink =0.7, )
plt.xlabel('X')
plt.ylabel('Y')
plt.title('109601005 '+mac)
fig.savefig('test2d____.png', dpi=300)
plt.show()