import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

minLat, maxLat = 21.75, 25.5
minLon, maxLon = 119.25, 122.5

fig = plt.figure(figsize=(6, 9))
ax = fig.add_axes([0.025, 0.025, 0.925, 0.925])

m = Basemap(projection='cyl',resolution='h',llcrnrlat=minLat, \
    urcrnrlat=maxLat, llcrnrlon=minLon, urcrnrlon=maxLon, ax=ax)
m.drawcoastlines(color='k')
m.drawcountries(color='k')

parallels = np.arange(21., 26.1, 1.)
m.drawparallels(parallels, labels=[1, 0, 0, 0], fontsize=14, linewidth=0.5)

meridians = np.arange(119., 123.1, 1.)
m.drawmeridians(meridians, labels=[0, 0, 0, 1], fontsize=14, linewidth=0.5)

plt.title('Taiwan')
fig.savefig("Taiwan",dpi=600)
plt.show()