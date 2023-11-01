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

def count_horizental_temparature_advection(
        u,
        v,
        t,
        dy,
        nlev,
        nlat,
        mlon,
        lat,
    ) -> np.ndarray[np.float64]:
    horizental_temparature_advection = np.zeros(
        [nlev, nlat, mlon]
    )
    
    for i in range(nlev):
        for j in range(nlat):
            for k in range(mlon):
                # 計算經度間距
                dx = dy * np.cos(lat[j] * np.pi / 180)

                # 檢查經度和緯度的範圍
                if 1 <= j < nlat - 1 and 1 <= k < mlon - 1:
                    # 計算 x 方向上的差分
                    x_value = (
                        u[i, j, k] * (t[i, j, k + 1] - t[i, j, k - 1]) / 
                        (2 * dx)
                    )  
                    # 計算 y 方向上的差分
                    y_value = (
                        v[i, j, k] * (t[i, j + 1, k] - t[i, j - 1, k]) / 
                        (2 * dy)
                    )  
                    
                    horizental_temparature_advection[i, j, k] = -x_value - y_value
                else:
                    # 單邊插植
                    # 計算 x 方向上的差分
                    if k == 0:
                        x_value = (
                            u[i, j, k] * (t[i, j, k + 1] - t[i, j, k]) / 
                            dx
                        )  
                    elif k == mlon - 1:
                        x_value = (
                            u[i, j, k] * (t[i, j, k] - t[i, j, k - 1]) / 
                            dx
                        )
                    else:
                        x_value = (
                            (u[i, j, k + 1] - u[i, j, k - 1]) / 
                            (2 * dx)
                        )

                    # 計算 y 方向上的差分
                    if j == 0:
                        y_value = (
                            v[i, j, k] * (t[i, j + 1, k] - t[i, j, k]) / 
                            dy
                        )  
                    elif j == nlat - 1:
                        y_value = (
                            v[i, j, k] * (t[i, j, k] - t[i, j - 1, k]) / 
                            dy
                        )
                    else:
                        y_value = (
                            v[i, j, k] * (t[i, j + 1, k] - t[i, j - 1, k]) / 
                            (2 * dy)
                        )

                    horizental_temparature_advection[i, j, k] = x_value + y_value

    return horizental_temparature_advection

def check_output_dir() -> None:
    os.makedirs("imgs", exist_ok=True)

def visualize_results(
        isobaric_surface_levels: list,
        horizental_temparature_advection: np.ndarray[np.float64], 
        lon,
        lat,
    ):
        check_output_dir()

        for level in range(horizental_temparature_advection.shape[0]):
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

            var = horizental_temparature_advection[level, :, :]
            contour = ax.contourf(
                lon, 
                lat, 
                var, 
                cmap='coolwarm',
            )

            output_file_name = f"{isobaric_surface_levels[level]}hpa_horizental_temparature_advection"
            figure_title = f"{isobaric_surface_levels[level]}hpa Horizental Temparature Advection"
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
                label="(10^-4/s)"
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

    horizental_temparature_advection = count_horizental_temparature_advection(
        u=u,
        v=v,
        t=t,
        dy=dy,
        nlev=5,
        nlat=25,
        mlon=49,
        lat=lat,
    )

    visualize_results(
        isobaric_surface_levels,
        horizental_temparature_advection * 10000, 
        lon=lon,
        lat=lat,
    )

if __name__ == '__main__':
    main()
