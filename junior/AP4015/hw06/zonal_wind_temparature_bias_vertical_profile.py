import numpy as np
import matplotlib.pyplot as plt


rows = 252
cols = 252
levels = 10
vars = 4

file_name = './data/fanapid.dat'
data = np.fromfile(file_name, dtype='>f4')

data = data.reshape(vars, levels, rows, cols)
lat = np.linspace(4, 43, 252)
lon = np.linspace(95, 145, 252)
hgt = [1000, 900, 850, 800, 700, 600, 500, 400, 300, 250]

laty, hgt = np.meshgrid(lat, hgt, indexing='xy')

u = np.array(data[0])
v = np.array(data[1])
w = np.array(data[2])
t = np.array(data[3])


def replace_above_threshold(matrix, threshold):
    mask = matrix > threshold
    matrix[mask] = np.nan
    return matrix


threshold = 10**30
u = replace_above_threshold(u, threshold)
v = replace_above_threshold(v, threshold)
w = replace_above_threshold(w, threshold)
t = replace_above_threshold(t, threshold)


def find_closest_value(array, target):
    idx = np.abs(array - target).argmin()
    closest_value = array[idx]
    arg = np.argmin(abs(array-closest_value))
    return arg


level = np.linspace(-5, 15, 21)

target = 122.3
arg = find_closest_value(lon, target)
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1)
p = ax.contourf(laty, hgt, t[:, :, arg], cmap="rainbow", levels=level)
contour = ax.contour(laty, hgt, u[:, :, arg], colors="black")
plt.xlim(15, 35)
ax.set_xlabel("N")
ax.set_ylabel("hpa")
ax.set_ylim(ax.get_ylim()[::-1])
plt.grid("--")
cb = plt.colorbar(p)
cb.set_label("temparature bias")
plt.clabel(contour, inline=True, fontsize=8, colors="black")
plt.title("zonal wind & temparature bias vertical profile")
plt.savefig(
    f"./imgs/zonal_meridian/zonal_wind_temparature_bias_vertical_profile.jpg", dpi=600)
plt.show()
