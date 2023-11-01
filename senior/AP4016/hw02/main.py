# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/06
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

from typing import Any
import numpy as np  
import matplotlib.pyplot as plt 
import os

def load_data(
        file_name: str,
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


def count_divergence(
        u,
        v,
        dy,
        nlev,
        nlat,
        mlon,
        lat,
    ) -> np.ndarray[np.float64]:
    divergence = np.zeros(
        [nlev, nlat, mlon]
    )
    
    for i in range(nlev):
        for j in range(nlat):
            for k in range(mlon):
                dx = dy * np.cos(lat[j] * np.pi / 180)
                if 1 <= j < nlat - 1 and 1 <= k < mlon - 1:
                    # 計算x方向上的差分
                    x_value = (
                        (u[i, j, k + 1] - u[i, j, k - 1]) / 
                        (2 * dx)
                    )
                    # 計算y方向上的差分
                    y_value = (
                        (v[i, j + 1, k] - v[i, j - 1, k]) / 
                        (2 * dy)
                    )
                    
                    divergence[i, j, k] = x_value + y_value
                else:
                    # 單邊插植
                    # 計算 x 方向上的差分
                    if k == 0:
                        x_value = (
                            (u[i, j, k + 1] - u[i, j, k]) / 
                            dx
                        )
                    elif k == mlon - 1:
                        x_value = (
                            (u[i, j, k] - u[i, j, k - 1]) / 
                            dx
                        )
                    else:
                        x_value = (
                            (u[i, j, k + 1] - u[i, j, k - 1]) / 
                            (2 * dx)
                        )

                    # 計算 y 方向上的差分
                    if j == 0:
                        y_value = (v[i, j + 1, k] - v[i, j, k]) / dy 
                    elif j == nlat - 1:
                        y_value = (v[i, j, k] - v[i, j - 1, k]) / dy 
                    else:
                        y_value = (v[i, j + 1, k] - v[i, j - 1, k]) / (2 * dy)  

                    divergence[i, j, k] = x_value + y_value

    return divergence

def count_vertical_speed(
        divergence,
        nlev,
        nlat,
        mlon,
        pressure_values,
    ) -> np.ndarray[np.float64]:

    init_vertical_speed = np.zeros(
        [nlev, nlat, mlon]
    )
    for i in range(nlev):
        for j in range(nlat):
            for k in range(mlon):
                if i == 0:
                    init_vertical_speed[i, j, k] = (
                        divergence[i, j, k] * pressure_values[i]
                    )
                elif i > 0:
                    init_vertical_speed[i, j, k] = (
                        init_vertical_speed[i - 1, j, k] + 
                        divergence[i, j, k] * pressure_values[i]
                    )

    # 5 * 25 * 49
    # nlev=5,
    # nlat=25,
    # mlon=49, 

    expanded_error = np.zeros(
        [5, 25, 49]
    )
    for i in range(nlev):
        for j in range(nlat):
            for k in range(mlon):
                expanded_error[i, j, k] = (
                    init_vertical_speed[4, j, k] / 910
                )

    # 修正相對渦度
    fixed_divergence = divergence - expanded_error

    # 計算新的垂直風速
    new_vertical_speed =  np.zeros(
        [nlev, nlat, mlon],
        dtype=float,
    )
    for i in range(nlev):
        for j in range(nlat):
            for k in range(mlon):
                if i == 0:
                    new_vertical_speed[i, j, k] = (
                        fixed_divergence[i, j, k] * pressure_values[i]
                    )
                elif i > 0:
                    new_vertical_speed[i, j, k] = (
                        new_vertical_speed[i - 1, j, k] + 
                        fixed_divergence[i, j, k] * 
                        pressure_values[i]
                    )  

    return new_vertical_speed

def check_output_dir() -> None:
    os.makedirs("imgs", exist_ok=True)

def visualize_results(
        factor, 
        lat,
    ) -> None:
    levels = [
        1010, 
        925, 
        775, 
        600, 
        400, 
        100
    ]
    plt.figure(
        figsize=(6, 3), 
        dpi=300,
    )
    var = np.zeros(
        (6, 25)
    )
    var[1:,:] = factor[:, :, 16]

    contour = plt.contour(
        lat, 
        levels, 
        var, 
        cmap='coolwarm',
        levels = np.linspace(-0.002, 0.002, 9)
    )
    plt.title("120E vetical velocity")
    plt.xlabel("Latitude (degrees)")
    plt.ylabel("Pressure (hPa)")
    plt.clabel(
        contour, 
        inline=1, 
        fontsize=5, 
        fmt='%1.4f',
    )

    plt.xticks(np.linspace(15, 60, 10))
    plt.yscale('log')
    plt.yticks(np.linspace(1000, 100, 10))

    plt.gca().yaxis.set_major_formatter(
        plt.FormatStrFormatter('%.0f')
    )
    plt.colorbar(
        contour, 
        orientation='vertical', 
        shrink=0.7, 
        label="(m/s)",
    )
    plt.gca().invert_yaxis()
    plt.ylim(1010, 99.99)
    plt.grid(
        visible=True, 
        linestyle='--', 
        alpha=0.5,
    )
    plt.savefig("120E_vetical_velocity.png")

    # plt.show()

def main() -> None:
    file_name = "./output.bin"
    dy = 6378000 * 1.875 * np.pi / 180
    pressure_values = [
        85, 
        150, 
        175, 
        200, 
        300,
    ]  # 高度層壓力值的列表

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

    divergence = count_divergence(
        u=u,
        v=v,
        dy=dy,
        nlev=5,
        nlat=25,
        mlon=49,
        lat=lat,
    )
    vertical_speed = count_vertical_speed(
        divergence=divergence,
        nlev=5,
        nlat=25,
        mlon=49,
        pressure_values=pressure_values,
    )

    visualize_results(
        factor=vertical_speed,
        lat=lat,
    )

if __name__ == '__main__':
    main()
