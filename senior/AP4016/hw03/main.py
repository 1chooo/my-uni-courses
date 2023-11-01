# -*- coding: utf-8 -*-
'''
Created Date: 2023/10/31
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

import numpy as np
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
import os

def load_data(filename):
    data = np.fromfile(filename, dtype='<f4')
    var, nlev, nlat, mlon = 3, 3, 46, 91
    data = data.reshape(var, nlev, nlat, mlon)
    return data

def configure_parameters(data):
    nlat, mlon = 46, 91
    lon = np.linspace(80, 170, mlon)
    lat = np.linspace(20, 65, nlat)
    h = data[0, :, :, :]
    u = data[1, :, :, :]
    v = data[2, :, :, :]
    return lon, lat, h, u, v

def geowind(h, lat, lon):
    nlev, nlat, mlon = h.shape
    nlat = 46
    mlon = 91
    omega = 7.29 * (10 ** -5)
    dy = 6378000 * np.pi / 180
    geo_windU = np.zeros([nlev, nlat, mlon])
    geo_windV = np.zeros([nlev, nlat, mlon])

    for i in range(nlev):
        for j in range(nlat):
            for k in range(mlon):
                f = 2 * omega * np.sin(lat[j] * np.pi / 180)
                dx = dy * np.cos(lat[j] * np.pi / 180)

                if 1 <= j < nlat - 1 and 1 <= k < mlon - 1:
                    xvalue = -(h[i, j + 1, k] - h[i, j - 1, k]) / (2 * dy * f)
                    yvalue = (h[i, j, k + 1] - h[i, j, k - 1]) / (2 * dx * f)
                else:
                    if j == 0:
                        xvalue = -(h[i, j + 1, k] - h[i, j, k]) / (dy * f)
                    elif j == nlat - 1:
                        xvalue = -(h[i, j, k] - h[i, j - 1, k]) / (dy * f)
                    else:
                        xvalue = -(h[i, j + 1, k] - h[i, j - 1, k]) / (2 * dy * f)

                    if k == 0:
                        yvalue = (h[i, j, k + 1] - h[i, j, k]) / (dx * f)
                    elif k == mlon - 1:
                        yvalue = (h[i, j, k] - h[i, j, k - 1]) / (dx * f)
                    else:
                        yvalue = (h[i, j, k + 1] - h[i, j, k - 1]) / (2 * dx * f)

                geo_windU[i, j, k] = 9.8 * xvalue
                geo_windV[i, j, k] = 9.8 * yvalue

    return geo_windU, geo_windV

def nonageowind(u, v, ug, vg):
    ua = u - ug
    va = v - vg
    return ua, va

def Divergence(u, v, lat, dy):
    nlev, nlat, mlon = u.shape
    div = np.zeros([nlev, nlat, mlon])

    for i in range(nlev):
        for j in range(nlat):
            for k in range(mlon):
                dx = dy * np.cos(lat[j] * np.pi / 180)

                if 1 <= j < nlat - 1 and 1 <= k < mlon - 1:
                    xvalue = (u[i, j, k + 1] - u[i, j, k - 1]) / (2 * dx)
                    yvalue = (v[i, j + 1, k] - v[i, j - 1, k]) / (2 * dy)
                    div[i, j, k] = xvalue + yvalue
                else:
                    dx = dy * np.cos(lat[j] * np.pi / 180)

                    if k == 0:
                        xvalue = (u[i, j, k + 1] - u[i, j, k]) / dx
                    elif k == mlon - 1:
                        xvalue = (u[i, j, k] - u[i, j, k - 1]) / dx
                    else:
                        xvalue = (u[i, j, k + 1] - u[i, j, k - 1]) / (2 * dx)

                    if j == 0:
                        yvalue = (v[i, j + 1, k] - v[i, j, k]) / dy
                    elif j == nlat - 1:
                        yvalue = (v[i, j, k] - v[i, j - 1, k]) / dy
                    else:
                        yvalue = (v[i, j + 1, k] - v[i, j - 1, k]) / (2 * dy)

                    div[i, j, k] = xvalue + yvalue

    return div

def plot_wind_vector(lon, lat, u, v, title):
    os.makedirs(title[6:], exist_ok=True)
    wspd = (u ** 2 + v ** 2) ** 0.5

    plt.figure(dpi=400)
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_extent([80, 170, 20, 65], crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS)
    ax.set_title(title)

    contourf = plt.contourf(lon, lat, wspd, cmap='jet')
    cbar = plt.colorbar(contourf, location='bottom', orientation='horizontal')
    cbar.set_label("wind speed (m/s)")

    contour = plt.contour(lon, lat, h[0, :, :], levels=np.linspace(10600, 12800, 12), colors='white')
    plt.clabel(contour, inline=True, fontsize=8, colors='white')

    ax.gridlines(draw_labels=[True, "x", "y", "bottom", "left"], linewidth=0.5, color='gray', alpha=0.5, linestyle='--')

    plt.quiver(lon[::2], lat[::2], u[::2, ::2], v[::2, ::2], scale_units='xy', scale=12, color='black')

    plt.savefig(title[6:] + "/" + title + ".png")

    # plt.show()

def plot_wind_divergence(lon, lat, div, u, v, title):
    os.makedirs(title[6:], exist_ok=True)

    plt.figure(dpi=400)
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_extent([80, 170, 20, 65], crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS)
    ax.set_title(title)

    contourf = plt.contourf(lon, lat, div, cmap='jet')
    cbar = plt.colorbar(contourf, location='bottom', orientation='horizontal')
    cbar.ax.tick_params(labelsize=7)
    cbar.set_label("divergence")

    contour = plt.contour(lon, lat, h[0, :, :], colors='white')
    plt.clabel(contour, inline=True, fontsize=8, colors='white')

    ax.gridlines(draw_labels=[True, "x", "y", "bottom", "left"], linewidth=0.5, color='gray', alpha=0.5, linestyle='--')

    plt.quiver(lon[::2], lat[::2], u[::2, ::2], v[::2, ::2], scale_units='xy', scale=4, color='black')

    plt.savefig(title[6:] + "/" + title + ".png")

    # plt.show()

def plot_data(lon, lat, h, u, v, title):
    pressure = [200, 500, 1000]
    os.makedirs(title, exist_ok=True)
    wspd = (u ** 2 + v ** 2) ** 0.5

    for i in range(len(pressure)):
        wind_level = 20 - 5 * i
        plt.figure(dpi=400)
        ax = plt.axes(projection=ccrs.PlateCarree())
        ax.set_extent([80, 170, 20, 65], crs=ccrs.PlateCarree())
        ax.add_feature(cfeature.LAND)
        ax.add_feature(cfeature.COASTLINE)
        ax.add_feature(cfeature.BORDERS)
        titles = str(pressure[i]) + title
        ax.set_title(titles)

        contourf = plt.contourf(lon, lat, wspd[i, :, :], cmap='jet')
        cbar = plt.colorbar(contourf, location='bottom', orientation='horizontal')
        cbar.set_label("wind speed (m/s)")

        contour = plt.contour(lon, lat, h[i, :, :], colors='white')
        plt.clabel(contour, inline=True, fontsize=8, colors='white')

        ax.gridlines(draw_labels=[True, "x", "y", "bottom", "left"], linewidth=0.5, color='gray', alpha=0.5, linestyle='--')

        q = plt.quiver(lon[::2], lat[::2], u[i, ::2, ::2], v[i, ::2, ::2], scale_units='xy', scale=10 - 3 * i, color='black')
        qk = plt.quiverkey(q, 0.8, 1.05, wind_level, str(wind_level) + ' m/s', labelpos='E', coordinates='axes',
                          fontproperties={'size': 8})

        plt.savefig(title + "/" + titles + ".png")

        # plt.show()

if __name__ == "__main__":
    dy = 6378000 * np.pi/180
    filename = './data/fnldata.dat'
    data = load_data(filename)
    lon, lat, h, u, v = configure_parameters(data)
    ug, vg = geowind(h, lat, lon)
    plot_wind_vector(lon, lat, ug[0, :, :], vg[0, :, :], "200mb geostrophic wind and height")
    div = Divergence(u, v, lat, dy)
    ua, va = nonageowind(u, v, ug, vg)
    plot_wind_divergence(lon, lat, div[0, :, :], ua[0, :, :], va[0, :, :], "200mb geostrophic wind, height and divergence")
    plot_data(lon, lat, h, u, v, "wind and height")
