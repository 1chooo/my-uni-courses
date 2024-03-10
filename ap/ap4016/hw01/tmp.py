# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/05
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

import numpy as np  
import cartopy.crs as ccrs  
import matplotlib.pyplot as plt 
import cartopy.feature as cfeature
import os

def horizental_temparature_advection(
        u,
        v,
        t,
        dy,
        nlev,
        nlat,
        mlon,
        lat,
    ):
    # 計算水平溫度平流
    t_adv = np.zeros([nlev, nlat, mlon])  # 創建一個全零數組來存儲水平溫度平流
    for i in range(nlev):  # 遍歷垂直層
        for j in range(nlat):  # 遍歷緯度
            for k in range(mlon):  # 遍歷經度
                if 1 <= j < nlat - 1 and 1 <= k < mlon - 1:  # 檢查經度和緯度的範圍
                    dx = dy * np.cos(lat[j] * np.pi / 180)  # 計算經度間距
                    xvalue = u[i, j, k] * (t[i, j, k + 1] - t[i, j, k - 1]) / (2 * dx)  # 計算x方向上的差分
                    yvalue = v[i, j, k] * (t[i, j + 1, k] - t[i, j - 1, k]) / (2 * dy)  # 計算y方向上的差分
                    t_adv[i, j, k] = -xvalue - yvalue  # 計算水平溫度平流
                else:
                    # 單邊插植
                    dx = dy * np.cos(lat[j] * np.pi / 180)  # 計算經度間距
                    if k == 0:
                        xvalue = u[i, j, k] * (t[i, j, k + 1] - t[i, j, k]) / dx  # 計算x方向上的差分
                    elif k == mlon - 1:
                        xvalue = u[i, j, k] * (t[i, j, k] - t[i, j, k - 1]) / dx  # 計算x方向上的差分
                    else:
                        xvalue = (u[i, j, k + 1] - u[i, j, k - 1]) / (2 * dx)  # 計算x方向上的差分

                    if j == 0:
                        yvalue = v[i, j, k] * (t[i, j + 1, k] - t[i, j, k]) / dy  # 計算y方向上的差分
                    elif j == nlat - 1:
                        yvalue = v[i, j, k] * (t[i, j, k] - t[i, j - 1, k]) / dy  # 計算y方向上的差分
                    else:
                        yvalue = v[i, j, k] * (t[i, j + 1, k] - t[i, j - 1, k]) / (2 * dy)  # 計算y方向上的差分

                    t_adv[i, j, k] = xvalue + yvalue  # 計算水平溫度平流

    return t_adv

def Divergence(
        u,
        v,
        dy,
        nlev,
        nlat,
        mlon,
        lat,
    ):
    # 計算散度
    div = np.zeros([nlev, nlat, mlon])  # 創建一個全零數組來存儲散度
    for i in range(nlev):  # 遍歷垂直層
        for j in range(nlat):  # 遍歷緯度
            for k in range(mlon):  # 遍歷經度
                if 1 <= j < nlat - 1 and 1 <= k < mlon - 1:  # 檢查經度和緯度的範圍
                    dx = dy * np.cos(lat[j] * np.pi / 180)  # 計算經度間距
                    xvalue = (u[i, j, k + 1] - u[i, j, k - 1]) / (2 * dx)  # 計算x方向上的差分
                    yvalue = (v[i, j + 1, k] - v[i, j - 1, k]) / (2 * dy)  # 計算y方向上的差分
                    div[i, j, k] = xvalue + yvalue  # 計算散度
                else:
                    # 單邊插植
                    dx = dy * np.cos(lat[j] * np.pi / 180)  # 計算經度間距
                    if k == 0:
                        xvalue = (u[i, j, k + 1] - u[i, j, k]) / dx  # 計算x方向上的差分
                    elif k == mlon - 1:
                        xvalue = (u[i, j, k] - u[i, j, k - 1]) / dx  # 計算x方向上的差分
                    else:
                        xvalue = (u[i, j, k + 1] - u[i, j, k - 1]) / (2 * dx)  # 計算x方向上的差分

                    if j == 0:
                        yvalue = (v[i, j + 1, k] - v[i, j, k]) / dy  # 計算y方向上的差分
                    elif j == nlat - 1:
                        yvalue = (v[i, j, k] - v[i, j - 1, k]) / dy  # 計算y方向上的差分
                    else:
                        yvalue = (v[i, j + 1, k] - v[i, j - 1, k]) / (2 * dy)  # 計算y方向上的差分

                    div[i, j, k] = xvalue + yvalue  # 計算散度

    return div


def Relative_Vorticity(
        u,
        v,
        dy,
        nlev,
        nlat,
        mlon,
        lat,
    ):
    # 計算相對渦度
    rv = np.zeros([nlev,  nlat,mlon])  # 創建一個全零數組來存儲相對渦度
    for i in range(nlev):  # 遍歷垂直層
        for j in range(nlat):  # 遍歷緯度
            for k in range(mlon):  # 遍歷經度，
                if 1 <= j < nlat - 1 and 1 <= k < mlon - 1:  # 檢查經度和緯度的範圍
                    dx = dy * np.cos(lat[j] * np.pi / 180)  # 計算經度間距
                    xvalue = (v[i, j, k + 1] - v[i, j, k - 1]) / (2 * dx)  # 計算x方向上的差分
                    yvalue = (u[i, j + 1, k] - u[i, j - 1, k]) / (2 * dy)  # 計算y方向上的差分
                    rv[i, j, k] = xvalue - yvalue  # 計算相對渦度
                else:
                    # 單邊插植
                    dx = dy * np.cos(lat[j] * np.pi / 180)  # 計算經度間距
                    if k == 0:
                        xvalue = (v[i, j, k + 1] - v[i, j, k]) /  dx  # 計算x方向上的差分
                    elif k == mlon - 1:
                        xvalue = (v[i, j, k] - v[i, j, k - 1]) / dx  # 計算x方向上的差分
                    else:
                        xvalue = (v[i, j, k + 1] - v[i, j, k - 1]) / (2 * dx)  # 計算x方向上的差分
                    
                    if j == 0:
                        yvalue = (u[i, j + 1, k] - u[i, j, k]) / dy  # 計算y方向上的差分
                    elif j == nlat - 1:
                        yvalue = (u[i, j, k] - u[i, j - 1, k]) / dy  # 計算y方向上的差分
                    else:
                        yvalue = (u[i, j + 1, k] - u[i, j - 1, k]) / (2 * dy)  # 計算y方向上的差分
                    
                    rv[i, j, k] = xvalue - yvalue  # 計算相對渦度
    return rv

def Absolute_Vorticity_Advection(
        vor,
        u,
        v,
        dy,
        nlev,
        nlat,
        mlon,
        lat,
    ):
        # 計算絕對渦度平流
        Vor_adv = np.zeros([nlev,  nlat,mlon])  # 創建一個全零數組來存儲絕對渦度平流
        for i in range(nlev):  # 遍歷垂直層
            for j in range(nlat):  # 遍歷緯度
                for k in range(mlon):  # 遍歷經度
                    if 1 <= j < nlat - 1 and 1 <= k < mlon - 1:  # 檢查經度和緯度的範圍
                        dx = dy * np.cos(lat[j] * np.pi / 180)  # 計算經度間距
                        xvalue = u[i, j, k] * (vor[i, j, k + 1] - vor[i, j, k - 1]) / (2 * dx)  # 計算x方向上的差分
                        yvalue = v[i, j, k] * (vor[i, j + 1, k] - vor[i, j - 1, k] + 2 * 7.29 * (10 ** -5) * np.sin(lat[j + 1] * np.pi / 180) - 2 * 7.29 * (10 ** -5) * np.sin(lat[j - 1] * np.pi / 180)) / (2 * dy)  # 計算y方向上的差分
                    else:
                        # 單邊插植
                        dx = dy * np.cos(lat[j] * np.pi / 180)  # 計算經度間距
                        if k == 0:
                            xvalue = (u[i, j, k] * (vor[i, j, k + 1] - vor[i, j, k])) /  dx  # 計算x方向上的差分
                        elif k == mlon - 1:
                            xvalue = (u[i, j, k] * (vor[i, j, k] - vor[i, j, k - 1])) / dx  # 計算x方向上的差分
                        else:
                            xvalue = u[i, j, k] * (vor[i, j, k + 1] - vor[i, j, k - 1]) / (2 * dx)  # 計算x方向上的差分
                        
                        if j == 0:
                            yvalue = v[i, j, k] * (vor[i, j + 1, k] - vor[i, j, k] + 2 * 7.29 * (10 ** -5) * np.sin(lat[j + 1] * np.pi / 180) - 2 * 7.29 * (10 ** -5) * np.sin(lat[j] * np.pi / 180)) / dy  # 計算y方向上的差分
                        elif j == nlat - 1:
                            yvalue = v[i, j, k] * (vor[i, j, k] - vor[i, j - 1, k] + 2 * 7.29 * (10 ** -5) * np.sin(lat[j] * np.pi / 180) - 2 * 7.29 * (10 ** -5) * np.sin(lat[j - 1] * np.pi / 180)) / dy  # 計算y方向上的差分
                        else:
                            yvalue = v[i, j, k] * (vor[i, j + 1, k] - vor[i, j - 1, k] + 2 * 7.29 * (10 ** -5) * np.sin(lat[j + 1] * np.pi / 180) - 2 * 7.29 * (10 ** -5) * np.sin(lat[j - 1] * np.pi / 180)) / (2 * dy)  # 計算y方向上的差分
                    Vor_adv[i, j, k] = -xvalue - yvalue  # 計算絕對渦度平流
        return Vor_adv

def plot_data(
        factor, 
        title, 
        label,
        lon,
        lat,
    ):
        # 繪製資料
        levels = [1000, 850, 700, 500, 300]  # 設定繪圖的層面
        os.makedirs(title[4:], exist_ok=True)  # 創建保存繪圖結果的目錄，去掉文件名的前4個字符
        for level in range(factor.shape[0]):  # 遍歷層面
            plt.figure(figsize=(6, 3), dpi=400)  # 創建一個繪圖窗口
            ax = plt.axes(projection=ccrs.PlateCarree())  # 使用PlateCarree地圖投影
            ax.set_extent([90, 180, 15, 60], crs=ccrs.PlateCarree())  # 設定地圖的範圍
            ax.add_feature(cfeature.LAND)  # 添加陸地特徵
            ax.add_feature(cfeature.COASTLINE)  # 添加海岸線特徵
            ax.add_feature(cfeature.BORDERS)  # 添加國界特徵
            var = factor[level, :, :]
            contour = ax.contourf(lon, lat, var, cmap='jet')  # 使用色塊表示資料
            file = str(levels[level]) + title  # 構建保存文件的名稱
            ax.set_title(file)  # 設定圖表的標題
            ax.gridlines(draw_labels=[True, "x", "y", "bottom", "left"], linewidth=0.5, color='gray', alpha=0.5, linestyle='--')  # 添加網格線

            cbar = plt.colorbar(contour, ax=ax, orientation='vertical', shrink=0.7, label=label)  # 添加色標
            plt.savefig(title[4:] + "/" + file + ".png")  # 保存圖表為圖片文件
            plt.show()  # 顯示圖表