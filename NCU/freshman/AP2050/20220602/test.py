import numpy as np
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt

import cartopy.crs as ccrs
import cartopy.mpl.ticker as cticker
from cartopy.util import add_cyclic_point

ds = xr.open_dataset(r'air.sfc.2021.nc')
#ds1985 = xr.open_dataset(r'air.sfc.1985.nc')

lats = ds.variables['lat'][:]
lons = ds.variables['lon'][:]
#print (lons)
time = ds.variables['time'][:]
temp = ds.variables['air'][:]

temp1985 = ds1985.variables['air'][:]

temp, lons = add_cyclic_point(temp, coord=ds['lon']) # add a cyclic boundary after 357.5;

fig = plt.figure(figsize=(12,9))

ax = plt.axes(projection=ccrs.PlateCarree())

cs = ax.contourf(lons, lats, temp[0, :, :], cmap='coolwarm', extend='both')

temp1d=np.zeros(365) # for 2021;
temp1d1985=np.zeros(365) # for 1985;
x1d=np.zeros(365)
ix = int(120./2.5)
jy = int((90.-23.5)/2.5)
print (f'ix jy= ',{ix}, {jy})

for i in range(365):
    x1d[i]=i
    temp1d[i]=temp[i, jy, ix] # extract 2021 data;
    temp1d1985[i]=temp1985[i, jy, ix] # extract 1985 data;

# Add coastlines;
ax.coastlines()

# Add gridlines;
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=False,
                 linewidth=2, color='black', alpha=0.5, linestyle='--')

gl.xlines = True
gl.ylines = True

ax.scatter(lons[ix], lats[jy], marker="*", color='b', s=75, transform=ccrs.PlateCarree())

# Define the xticks for longitudes;
ax.set_xticks(np.arange(-180, 181, 60), crs=ccrs.PlateCarree())
lon_formatter = cticker.LongitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)

# Define the yticks for latitudes;
ax.set_yticks(np.arange(-90, 91, 30), crs=ccrs.PlateCarree())
lat_formatter = cticker.LatitudeFormatter()
ax.yaxis.set_major_formatter(lat_formatter)

# Add color bar;
cbar = plt.colorbar(cs, shrink=0.9, orientation='horizontal', label='Surface Air Temperature (K)')

# Add figure title;
plt.title('Global Surface Temperature 2021 from NCEP')
fig.savefig('ttrobinson.png', dpi=300)

plt.show()