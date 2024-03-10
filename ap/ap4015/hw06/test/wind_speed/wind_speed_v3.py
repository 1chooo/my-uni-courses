import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

diri = "./"
fili = "fanapid.dat"
fName = diri + fili

nlat = 252
mlon = 252
nlev = 10
ntim = 1
vars = 4
UNDEF = 1.e30

x = np.empty((vars, nlev, nlat, mlon), dtype=np.float32)
n = 0

f = open(fName, "rb")
for nt in range(ntim):
    for v in range(vars):
        x[v, :, :, :] = np.fromfile(f, dtype=np.float32, count=nlev * nlat * mlon).reshape(nlev, nlat, mlon)

u = x[0, :, :, :]
v = x[1, :, :, :]
w = x[2, :, :, :]
t = x[3, :, :, :]

WS = np.sqrt(u ** 2 + v ** 2)

lat = np.linspace(17.0, 30.0, nlat)
lon = np.linspace(114.0, 130.0, mlon)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)

map = Basemap(
    llcrnrlon=114.0,
    llcrnrlat=17.0,
    urcrnrlon=130.0,
    urcrnrlat=30.0,
    projection='lcc', 
    resolution='c',
    lat_0=23.5, 
    lon_0=120, 
    lat_1=23.5, 
    lat_2=40,
    width=12000000, 
    height=10000000
)

map.drawcoastlines()
map.drawcountries()
map.drawparallels(np.arange(-90., 91., 10.), labels=[1, 0, 0, 0])
map.drawmeridians(np.arange(-180., 181., 10.), labels=[0, 0, 0, 1])

x, y = map(*np.meshgrid(lon, lat))

levels = np.arange(0, 50, 5)
c = ax.contourf(x, y, WS[1, :, :], levels=levels, cmap='rainbow')
cbar = plt.colorbar(c, ax=ax)
cbar.set_label('Wind Speed (m/s)')

plt.title('Wind Speed')
plt.show()