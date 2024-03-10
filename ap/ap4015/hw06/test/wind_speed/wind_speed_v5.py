import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Set the latitudinal and longitudinal limits of the map.
minLat, maxLat = 17, 30
minLon, maxLon = 114, 130

# Load wind speed data
# ...
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

WS = np.sqrt(u ** 2 + v ** 2)

# Create a figure and axes object.
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

# Define latitude and longitude grids
lat = np.linspace(minLat, maxLat, nlat)
lon = np.linspace(minLon, maxLon, mlon)
lon, lat = np.meshgrid(lon, lat)

# Add the coastline and country boundaries.
ax.coastlines()
ax.add_feature(cfeature.BORDERS, linestyle=':', edgecolor='gray')

# Add the parallels and meridians.
parallels = np.arange(16., 31.1, 2.)
meridians = np.arange(110., 131.1, 4.)
ax.set_xticks(meridians, crs=ccrs.PlateCarree())
ax.set_yticks(parallels, crs=ccrs.PlateCarree())
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
ax.gridlines(draw_labels=True, linestyle=':', color='gray')

# Plot wind speed using contourf
levels = np.arange(0, 50, 5)
c = ax.contourf(lon, lat, WS[0, :, :], levels=levels, cmap='rainbow', transform=ccrs.PlateCarree())
plt.contourf(lon, lat, WS[0, :, :], levels=levels,
             transform=ccrs.PlateCarree(),
             cmap='rainbow')
cbar = plt.colorbar(c, ax=ax)
cbar.set_label('Wind Speed (m/s)')

# Set the title of the plot.
ax.set_title('Wind Speed Field', fontsize=20)

# Save the figure and display it.
fig.savefig("./img/Taiwan_wind_speed_v5.jpg", dpi=600)
plt.show()
