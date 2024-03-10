# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/05
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

from typing import Any
import numpy as np  
import cartopy.crs as ccrs  
import matplotlib.pyplot as plt 
import cartopy.feature as cfeature
import os

def load_data(
        file_name,
        var, 
        nlev,
        nlat,
        mlon,
    ) -> np.ndarray[Any]:
    data = np.fromfile(
        file_name, 
        dtype='<f4',
    )
    data = data.reshape(
        var, 
        nlev,
        nlat,
        mlon,
    )

    return data

def configure_parameters(
        mlon, 
        nlat, 
        data
    ) -> tuple[
        np.linspace,
        np.linspace,
        Any,    
        Any,    
        Any,    
        Any,
    ]:
    lon = np.linspace(90, 180, mlon)
    lat = np.linspace(15, 60, nlat)
    h = data[0, :, :, :]
    u = data[1, :, :, :]
    v = data[2, :, :, :]
    t = data[3, :, :, :]

    return (
        lon,
        lat,
        h,
        u,
        v,
        t,
    )

def count_relative_voricity(
        u,
        v,
        dy,
        nlev,
        nlat,
        mlon,
        lat,
    ) -> np.ndarray[np.float64]:
    relative_voricity = np.zeros(
        [nlev, nlat, mlon]
    )
    for i in range(nlev):  # 遍歷垂直層
        for j in range(nlat):  # 遍歷緯度
            for k in range(mlon):  # 遍歷經度，
                if 1 <= j < nlat - 1 and 1 <= k < mlon - 1:  # 檢查經度和緯度的範圍
                    dx = dy * np.cos(lat[j] * np.pi / 180)  # 計算經度間距
                    x_value = (v[i, j, k + 1] - v[i, j, k - 1]) / (2 * dx)  # 計算x方向上的差分
                    y_value = (u[i, j + 1, k] - u[i, j - 1, k]) / (2 * dy)  # 計算y方向上的差分
                    relative_voricity[i, j, k] = x_value - y_value  # 計算相對渦度
                else:
                    # 單邊插植
                    dx = dy * np.cos(lat[j] * np.pi / 180)  # 計算經度間距
                    if k == 0:
                        x_value = (v[i, j, k + 1] - v[i, j, k]) /  dx  # 計算x方向上的差分
                    elif k == mlon - 1:
                        x_value = (v[i, j, k] - v[i, j, k - 1]) / dx  # 計算x方向上的差分
                    else:
                        x_value = (v[i, j, k + 1] - v[i, j, k - 1]) / (2 * dx)  # 計算x方向上的差分
                    
                    if j == 0:
                        y_value = (u[i, j + 1, k] - u[i, j, k]) / dy  # 計算y方向上的差分
                    elif j == nlat - 1:
                        y_value = (u[i, j, k] - u[i, j - 1, k]) / dy  # 計算y方向上的差分
                    else:
                        y_value = (u[i, j + 1, k] - u[i, j - 1, k]) / (2 * dy)  # 計算y方向上的差分
                    
                    relative_voricity[i, j, k] = x_value - y_value  # 計算相對渦度

    return relative_voricity

def check_output_dir() -> None:
    os.makedirs("imgs", exist_ok=True)

def visualize_results(
        isobaric_surface_levels: list,
        relative_voricity: np.ndarray[np.float64], 
        lon,
        lat,
    ):
        check_output_dir()

        for level in range(relative_voricity.shape[0]):
            plt.figure(
                figsize=(6, 3), 
                dpi=300,
            )
            ax = plt.axes(
                projection=ccrs.PlateCarree()
            )
            ax.set_extent(
                [90, 180, 14.99, 60.01], 
                crs=ccrs.PlateCarree()
            )
            ax.add_feature(
                cfeature.LAND
            )
            ax.add_feature(
                cfeature.COASTLINE
            )
            ax.add_feature(
                cfeature.BORDERS
            )
            ax.add_feature(
                cfeature.STATES, 
                linewidth=0.5,
            )

            var = relative_voricity[level, :, :]
            contour = ax.contourf(
                lon, 
                lat, 
                var, 
                cmap='coolwarm',
            )

            output_file_name = f"{isobaric_surface_levels[level]}hpa_relative_voricity"
            figure_title = f"{isobaric_surface_levels[level]}hpa Relative Voricity"
            ax.set_title(figure_title)
            ax.gridlines(
                draw_labels=[True, "x", "y", "bottom", "left"], 
                linewidth=0.5, 
                alpha=0.5, 
                linestyle='--'
            )

            plt.colorbar(
                contour, 
                ax=ax, 
                orientation='vertical', 
                shrink=0.7, 
                label="(10^-5/s)"
            )
            plt.savefig(f"imgs/{output_file_name}.png")
            
            # plt.show()

def main() -> None:
    file_name = "../output.bin"
    dy = 6378000 * 1.875 * np.pi / 180
    omega = 7.29 * 100000
    isobaric_surface_levels = [1000, 850, 700, 500, 300]

    data = load_data(
        file_name=file_name,
        var=4,
        nlev=5,
        nlat=25,
        mlon=49, 
    )

    (
        lon,
        lat,
        h,
        u,
        v,
        t,
    ) = configure_parameters(
        mlon=49,
        nlat=25,
        data=data,
    )

    relative_voricity = count_relative_voricity(
        u=u,
        v=v,
        dy=dy,
        nlev=5,
        nlat=25,
        mlon=49,
        lat=lat,
    )

    visualize_results(
        isobaric_surface_levels,
        relative_voricity * 100000, 
        lon=lon,
        lat=lat,
    )

if __name__ == '__main__':
    main()
