import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeat

fig = plt.figure(figsize = 10.8)
lonl = 90 # longitude left
lonr = 150 # longitude right
latb = 0 # latitude button
latt = 50 # latitude top
ngrids = 25
c_lon = 120
c_lat = 20
para_latt = 45
para_latb = 30
lon = np.linspace(lonl, lonr, ngrids) # ngrids grid points
lat = np.linspace(latb, latt, ngrids) # ngrids grid points
lon2d, lat2d = np.meshgrid(lon, lat) # two dimension