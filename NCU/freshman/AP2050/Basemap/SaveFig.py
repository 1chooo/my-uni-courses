'''
20210610 this code shows how to read and plot a 2d surface
temperature distribution from a NCEP surface analysis data.
to output results for each day to a jpeg file
'''

from netCDF4 import Dataset
import numpy as np
import matplotlib as mpl
mpl.use('TKAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#read in the data
data = Dataset(r'/Users/linchunho/basemap/air.sfc.2021.nc')
print(data.variables)
print(data.variables.keys())

lats = data.variables['lat'][:]
print(lats)

lons = data.variables['lon'][:]
print(lons)

time = data.variables['time'][:]
print(time)

temp = data.variables['air'][:]

fig = plt.figure(figsize=(12, 9))

mp = Basemap(projection='mill',
             llcrnrlon = 0., llcrnrlat = -90., urcrnrlon = 360., urcrnrlat = 90.,
             resolution = 'c')
lon, lat = np.meshgrid(lons, lats)
x, y =mp(lon, lat)

days = np.arange(0, 159)
print(days)
#exit()
day = 0
for i in days:
    c_scheme = mp.pcolor(x, y, np.squeeze(temp[i, :, :]), cmap = 'jet')
    mp.drawcoastlines()
    mp.drawstates()
    mp.drawcountries()
    cbar = mp.colorbar(c_scheme, location = 'bottom', pad = '10%')
    day += 1
    plt.title('Global Surface Temperature (K) '+'Day'+str(day)+'of 2021')
    plt.clim(200., 310.)
    #plt.show()
    #fig.savefig('global_surface_temperature', dpi = 680)
    fig.savefig(r'jpeg/'+ str(day)+'.jpg')