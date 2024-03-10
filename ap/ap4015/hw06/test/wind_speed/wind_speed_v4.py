import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

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
        x[v, :, :, :] = np.fromfile(
            f, 
            dtype=np.float32, 
            count=nlev * nlat * mlon).reshape(nlev, nlat, mlon)

u = x[0, :, :, :]
v = x[1, :, :, :]
w = x[2, :, :, :]
t = x[3, :, :, :]

WS = np.sqrt(u ** 2 + v ** 2)


# Create a figure and axes object.
fig = plt.figure(figsize=(8, 8))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# Create a Basemap object with the specified projection and limits.
m = Basemap(
    projection='cyl',
    resolution='h',
    llcrnrlat=minLat,
    urcrnrlat=maxLat,
    llcrnrlon=minLon,
    urcrnrlon=maxLon,
    ax=ax
)



# Draw the blue marble background.
m.bluemarble()

# Add the coastline and country boundaries.
m.drawcoastlines(color='k')
m.drawcountries(color='k')

# Add the parallels and meridians.
parallels = np.arange(16., 31.1, 2.)
meridians = np.arange(110., 131.1, 4.)
m.drawparallels(
    parallels, 
    labels=[1, 0, 0, 0], 
    fontsize=14, linewidth=0.5
)
m.drawmeridians(
    meridians, 
    labels=[0, 0, 0, 1], 
    fontsize=14, 
    linewidth=0.5
)

# Plot wind speed
lat = np.linspace(17, 30, nlat)
lon = np.linspace(114, 130, mlon)
lon, lat = np.meshgrid(lon, lat)

# Customize the colorbar
levels = np.arange(0, 50, 5)
c = m.contourf(lon, lat, WS[1, :, :], levels=levels, cmap='rainbow', latlon=True)
cbar = plt.colorbar(c, ax=ax)
cbar.set_label('Wind Speed (m/s)')

# Set the title of the plot.
plt.title('Map of Taiwan with Wind Speed Data', fontsize=20)

# Save the figure and display it.
fig.savefig("./img/Taiwan_wind_speed_v4.jpg", dpi=600)
plt.show()
