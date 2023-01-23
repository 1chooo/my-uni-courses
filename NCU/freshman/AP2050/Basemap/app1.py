'''
20210610 this code shows how to read and plot a 2-D surface
temperature distribution from a NCEP surface analysis data.
'''

from netCDF4 import Dataset
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# read in the data
data = Dataset(r"./air.sfc.2021.nc")
print(data.variables)
print(data.variables.keys())


latitude = data.variables['lat'][:]
print(latitude)

longitude = data.variables['lon'][:]
print(longitude)

time = data.variables['time'][:]
print(time)

temp = data.variables['air'][:]

fig = plt.figure(figsize=(12,9))

mp = Basemap(projection = 'mill',
             llcrnrlon = 0.,
             llcrnrlat = -90.,
             urcrnrlon = 360.,
             urcrnrlat = 90.,
             resolution = 'c')

lon, lat = np.meshgrid(longitude,latitude)
x, y = mp(lon,lat)

c_scheme =mp.pcolor(x,y,np.squeeze(temp[0, :, :]), cmap='jet')
mp.drawcoastlines()
mp.drawcountries()
cbar = mp.colorbar(c_scheme, location='bottom', pad='10%')

plt.title("global surface temperature (K)")
fig.savefig("global_surface_temperature", dpi=600)

plt.show()
