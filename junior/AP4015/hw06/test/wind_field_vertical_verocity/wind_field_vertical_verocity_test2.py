import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

class WindFieldPlotter:
    def __init__(self, data_file):
        self.data = np.fromfile(data_file, dtype='>f4')
        self.rows = 252
        self.cols = 252
        self.levels = 10
        self.vars = 4
        self.lat = np.linspace(4, 43, self.rows)
        self.lon = np.linspace(95, 145, self.cols)
        self.lonx, self.laty = np.meshgrid(self.lon, self.lat, indexing='xy')
        self.hgt = [1000, 900, 850, 800, 700, 600, 500, 400, 300, 250]
        self.h = [2, 6, 8]

    def replace_above_threshold(self, matrix, threshold):
        mask = matrix > threshold
        matrix[mask] = np.nan
        return matrix

    def plot_wind_field_vertical_velocity(self):
        data = self.data.reshape(self.vars, self.levels, self.rows, self.cols)
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
            ax = fig.add_subplot(1, 1, 1)
            m = Basemap(projection='cyl', llcrnrlon=95, llcrnrlat=4, urcrnrlon=145, urcrnrlat=43, resolution='l')
            m.drawcoastlines()
            m.drawparallels(np.arange(0, 45, 5), labels=[1, 0, 0, 0], linewidth=0.5)
            m.drawmeridians(np.arange(90, 155, 10), labels=[0, 0, 0, 1], linewidth=0.5)
            m.contourf(self.lonx, self.laty, w[i, :, :], cmap='gist_ncar', latlon=True)
            m.quiver(self.lonx, self.laty, u[i, :, :], v[i, :, :],
                     scale=60, scale_units='xy', units='xy', latlon=True)
            plt.colorbar()
            plt.grid("--")
            plt.title(str(self.hgt[i]) + "mb wind field & vertical velocity")
            plt.savefig("./imgs/wind_field_vertical_verocity/" +
                        str(self.hgt[i]) + "mb wind field & vertical velocity.jpg", dpi=400)
            plt.show()


def main():
    data_file = './data/fanapid.dat'
    plotter = WindFieldPlotter(data_file)
    plotter.plot_wind_field_vertical_velocity()


if __name__ == "__main__":
    main()
