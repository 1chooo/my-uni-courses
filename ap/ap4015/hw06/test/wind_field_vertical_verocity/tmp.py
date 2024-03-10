import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
# 定義矩陣的維度
rows = 252
cols = 252
levels = 10
vars = 4
# 讀取二進制文件的數據
file_name = './data/fanapid.dat'  # 二進制文件的路徑
data = np.fromfile(file_name, dtype='>f4')

# 重新組織數據為矩陣
data = data.reshape(vars, levels, rows, cols)
lat = np.linspace(4, 43, 252)
lon = np.linspace(95, 145, 252)
lonx, laty = np.meshgrid(lon, lat, indexing='xy')
hgt = [1000, 900, 850, 800, 700, 600, 500, 400, 300, 250]
h = [2, 6, 8]
# 提取各個變數的數據
u = np.array(data[0])
v = np.array(data[1])
w = np.array(data[2])
t = np.array(data[3])


def replace_above_threshold(matrix, threshold):
    mask = matrix > threshold
    matrix[mask] = np.nan
    return matrix


threshold = 10**10
u = replace_above_threshold(u, threshold)
v = replace_above_threshold(v, threshold)
w = replace_above_threshold(w, threshold)
t = replace_above_threshold(t, threshold)


# 打印各個變數的矩陣形狀
# print("U shape:", u.shape)
# print("V shape:", v.shape)
# print("W shape:", w.shape)
# print("T shape:", t.shape)

for i in h:
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent([118, 128, 18, 28], crs=ccrs.PlateCarree())
    level = np.linspace(-2.5, 3, 23)
    ax.coastlines()
    ax.set_xticks(np.linspace(114, 130, 11), crs=ccrs.PlateCarree())
    ax.set_yticks(np.linspace(17, 30, 11), crs=ccrs.PlateCarree())
    ax.set_xlabel("E")
    ax.set_ylabel("N")
    p = ax.contourf(lonx, laty, w[i, :, :], level,
                    transform=ccrs.PlateCarree(), cmap="gist_ncar")
    ax.quiver(lonx, laty, u[i, :, :], v[i, :, :],
              scale=60, scale_units='xy', units='xy')
    plt.colorbar(p)
    plt.grid("--")
    plt.title(str(hgt[i])+"mb wind field & vertical velocity")
    plt.savefig("./imgs/wind_field_vertical_verocity/" +
                str(hgt[i])+"mb wind field & vertical velocity.jpg", dpi=400)
    plt.show()
