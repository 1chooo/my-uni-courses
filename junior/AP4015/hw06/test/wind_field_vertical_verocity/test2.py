import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

class WindFieldVisualizer:
    def __init__(self):
        self.rows = 252
        self.cols = 252
        self.levels = 10
        self.vars = 4
        self.file_name = './data/fanapid.dat'
        self.lat = np.linspace(4, 43, 252)
        self.lon = np.linspace(95, 145, 252)
        self.lonx, self.laty = np.meshgrid(self.lon, self.lat, indexing='xy')
        self.hgt = [1000, 900, 850, 800, 700, 600, 500, 400, 300, 250]
        self.h = [2, 6, 8]
        
    def replace_above_threshold(self, matrix, threshold):
        mask = matrix > threshold
        matrix[mask] = np.nan
        return matrix
    
    def plot_wind_field_vertical_velocity(self):
        data = np.fromfile(self.file_name, dtype='>f4')
        data = data.reshape(self.vars, self.levels, self.rows, self.cols)
        
        u = np.array(data[0])
        v = np.array(data[1])
        w = np.array(data[2])
        t = np.array(data[3])
        
        threshold = 10**10
        u = self.replace_above_threshold(u, threshold)
        v = self.replace_above_threshold(v, threshold)
        w = self.replace_above_threshold(w, threshold)
        t = self.replace_above_threshold(t, threshold)
        
        for i in self.h:
            fig = plt.figure(figsize=(10, 10))
            m = Basemap(llcrnrlon=114, llcrnrlat=17, urcrnrlon=130, urcrnrlat=30, resolution='l')
            m.drawcoastlines()
            m.drawparallels(np.linspace(17, 30, 11), labels=[1, 0, 0, 0], linewidth=0.5)
            m.drawmeridians(np.linspace(114, 130, 11), labels=[0, 0, 0, 1], linewidth=0.5)
            x, y = m(self.lonx, self.laty)
            level = np.linspace(-2.5, 3, 23)
            p = m.contourf(x, y, w[i, :, :], level, cmap="gist_ncar")
            m.quiver(x, y, u[i, :, :], v[i, :, :],
                     scale=60, scale_units='xy', units='xy')
            plt.colorbar(p)
            plt.grid("--")
            plt.title(str(self.hgt[i]) + "mb wind field & vertical velocity")
            plt.savefig("./imgs/test/" + str(self.hgt[i]) + "mb wind field & vertical velocity.jpg", dpi=400)
            plt.show()

def main():
    visualizer = WindFieldVisualizer()
    visualizer.plot_wind_field_vertical_velocity()

if __name__ == "__main__":
    main()
