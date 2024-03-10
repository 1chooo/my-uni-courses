# -*- coding: utf-8 -*-
'''
Created Date: 2023/10/31
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

import numpy as np  # 引入NumPy庫，用於數值計算
import cartopy.crs as ccrs  # 引入Cartopy庫，用於地圖投影和地理資料可視化
import matplotlib.pyplot as plt  # 引入Matplotlib庫，用於繪圖
import cartopy.feature as cfeature  # 引入Cartopy的特徵模組，用於地圖特徵的添加
import os  # 引入os模組，用於操作文件路徑和目錄

class MyDataPlotter:
    def __init__(self, filename):
        self.filename = filename  # 初始化類的實例，設定資料檔案的文件名稱
        self.nlat = 46  # 緯度格點數，指定緯度方向上的格點數量
        self.mlon = 91  # 經度格點數，指定經度方向上的格點數量
        self.nlev = 3   # 垂直層數，指定垂直層數量
        self.var = 3    # 變數數量，指定資料中的變數數量
        self.dy = 6378000 * np.pi/180  # 經度間距對應的米數，計算經度方向上的距離
        self.omega = 7.29*(10**-5)  # 地球自轉速率

    def load_data(self):
        # 載入資料
        self.data = np.fromfile(self.filename, dtype='<f4')  # 從二進制文件讀取數據，並指定數據類型為32位浮點數
        self.data = self.data.reshape(self.var, self.nlev,  self.nlat, self.mlon)  # 重塑數據形狀為指定的維度
        print(self.data)

    def configure_parameters(self):
        # 設定參數
        self.lon = np.linspace(80, 170, self.mlon)  # 經度範圍，生成經度的範圍數據
        self.lat = np.linspace(20, 65, self.nlat)   # 緯度範圍，生成緯度的範圍數據
        self.h = self.data[0, :, :, :]  # 高度場，提取數據中的高度場信息
        self.u = self.data[1, :, :, :]  # 東向風場，提取數據中的東向風場信息
        self.v = self.data[2, :, :, :]  # 北向風場，提取數據中的北向風場信息

    def geowind(self):
        geo_windU = np.zeros([self.nlev,  self.nlat,self.mlon]) #初始化 地轉U風
        geo_windV = np.zeros([self.nlev,  self.nlat,self.mlon]) #初始化 地轉V風
        for i in range(self.nlev):
            for j in range(self.nlat):  # 遍歷緯度
                for k in range(self.mlon):  # 遍歷經度
                    f = 2*self.omega*np.sin(self.lat[j]* np.pi / 180) #計算科氏力
                    dx = self.dy * np.cos(self.lat[j] * np.pi / 180)  # 計算經度間距
                    if 1 <= j < self.nlat - 1 and 1 <= k < self.mlon - 1:  # 檢查經度和緯度的範圍
                        xvalue = -(self.h[i, j+1, k] - self.h[i, j-1, k]) / (2 * self.dy * f)  # 計算x方向上的差分
                        yvalue = (self.h[i, j, k+1] - self.h[i, j , k-1]) / (2 * dx * f)  # 計算y方向上的差分
                    else:
                        # 單邊插植
                        if j == 0:
                            xvalue = -(self.h[i, j+1, k ] - self.h[i, j, k]) / (self.dy * f)  # 計算x方向上的差分
                        elif j == self.nlat - 1:
                            xvalue = -(self.h[i, j, k] - self.h[i, j-1, k]) / (self.dy * f)  # 計算x方向上的差分
                        else:
                            xvalue = -(self.h[i, j+1, k] - self.h[i, j-1, k]) / (2 * self.dy * f)  # 計算x方向上的差分

                        if k == 0:
                            yvalue = (self.h[i, j, k+1] - self.h[i, j, k]) / (dx * f)  # 計算y方向上的差分
                        elif k == self.mlon - 1:
                            yvalue = (self.h[i, j, k] - self.h[i, j, k-1]) / (dx * f)  # 計算y方向上的差分
                        else:
                            yvalue = (self.h[i, j , k+1] - self.h[i, j, k-1]) / (2 * dx * f) # 計算y方向上的差分

                    geo_windU[i,j,k] = 9.8*xvalue  #將X方向計算結果加入資料地轉風矩陣
                    geo_windV[i,j,k] = 9.8*yvalue  #將Y方向計算結果加入資料地轉風矩陣
        
        return geo_windU,geo_windV
    def nonageowind(self,ug,vg):
        ua = self.u - ug   #計算非地轉風
        va = self.v - vg
        return ua,va

        


        


    def Divergence(self):
        # 計算相對渦度
        div = np.zeros([self.nlev,  self.nlat,self.mlon])  # 創建一個全零數組來存儲相對渦度
        # i:level j:lat m:lon
        
        for i in range(self.nlev):  # 遍歷垂直層
            for j in range(self.nlat):  # 遍歷緯度
                for k in range(self.mlon):  # 遍歷經度
                    if 1 <= j < self.nlat - 1 and 1 <= k < self.mlon - 1:  # 檢查經度和緯度的範圍
                        dx = self.dy * np.cos(self.lat[j] * np.pi / 180)  # 計算經度間距
                        xvalue = (self.u[i, j, k + 1] - self.u[i, j, k - 1]) / (2 * dx)  # 計算x方向上的差分
                        yvalue = (self.v[i, j + 1, k] - self.v[i, j - 1, k]) / (2 * self.dy)  # 計算y方向上的差分
                        div[i, j, k] = xvalue + yvalue  # 計算相對渦度
                    else:
                        # 單邊插植
                        dx = self.dy * np.cos(self.lat[j] * np.pi / 180)  # 計算經度間距
                        if k == 0:
                            xvalue = (self.u[i, j, k + 1] - self.u[i, j, k]) / dx  # 計算x方向上的差分
                        elif k == self.mlon - 1:
                            xvalue = (self.u[i, j, k] - self.u[i, j, k - 1]) / dx  # 計算x方向上的差分
                        else:
                            xvalue = (self.u[i, j, k + 1] - self.u[i, j, k - 1]) / (2 * dx)  # 計算x方向上的差分

                        if j == 0:
                            yvalue = (self.v[i, j + 1, k] - self.v[i, j, k]) / self.dy  # 計算y方向上的差分
                        elif j == self.nlat - 1:
                            yvalue = (self.v[i, j, k] - self.v[i, j - 1, k]) / self.dy  # 計算y方向上的差分
                        else:
                            yvalue = (self.v[i, j + 1, k] - self.v[i, j - 1, k]) / (2 * self.dy)  # 計算y方向上的差分

                        div[i, j, k] = xvalue + yvalue  # 計算相對渦度

        return div
    
    def plot_wind_vector(self, u, v, title):
        # 創建保存繪圖結果的目錄，去掉文件名的前6個字元
        os.makedirs(title[6:], exist_ok=True)

        # 計算風速
        wspd = (u**2 + v**2)**0.5

        # 創建風標圖
        plt.figure(dpi=400)  # 創建一個新的圖形，設置DPI（每英寸點數）為400
        ax = plt.axes(projection=ccrs.PlateCarree())  # 使用PlateCarree地圖投影
        ax.set_extent([80, 170, 20, 65], crs=ccrs.PlateCarree())  # 設定地圖的範圍
        ax.add_feature(cfeature.LAND)  # 添加陸地特徵
        ax.add_feature(cfeature.COASTLINE)  # 添加海岸線特徵
        ax.add_feature(cfeature.BORDERS)  # 添加國界特徵
        ax.set_title(title)  # 設置圖形標題

        # 繪制風速等值線
        contourf = plt.contourf(self.lon, self.lat, wspd, cmap='jet')  # 繪制風速的等值線圖
        cbar = plt.colorbar(contourf, location='bottom', orientation='horizontal')  # 添加顏色條
        cbar.set_label("wind speed (m/s)")  # 顏色條的標籤

        # 繪制地形等值線
        contour = plt.contour(self.lon, self.lat, self.h[0, :, :], levels=np.linspace(10600, 12800, 12), colors='white')
        plt.clabel(contour, inline=True, fontsize=8, colors='white')  # 添加地形等值線標籤

        # 添加網格線
        ax.gridlines(draw_labels=[True, "x", "y", "bottom", "left"], linewidth=0.5, color='gray', alpha=0.5, linestyle='--')

        # 繪制風矢量
        plt.quiver(self.lon[::2], self.lat[::2], u[::2, ::2], v[::2, ::2], scale_units='xy', scale=12, color='black')

        # 保存圖形為文件
        plt.savefig(title[6:] + "/" + title+".png")

        # 顯示圖形
        plt.show()
    
    def plot_wind_divergence(self, div, u, v, title):
        
        # 創建保存繪圖結果的目錄，去掉文件名的前6個字元
        os.makedirs(title[6:], exist_ok=True)
        # 創建風標圖
        plt.figure(dpi=400)  # 創建一個新的圖形，設置DPI（每英寸點數）為400
        ax = plt.axes(projection=ccrs.PlateCarree())  # 使用PlateCarree地圖投影
        ax.set_extent([80, 170, 20, 65], crs=ccrs.PlateCarree())  # 設定地圖的範圍
        ax.add_feature(cfeature.LAND)  # 添加陸地特徵
        ax.add_feature(cfeature.COASTLINE)  # 添加海岸線特徵
        ax.add_feature(cfeature.BORDERS)  # 添加國界特徵
        ax.set_title(title)  # 設置圖形標題

        # 繪制風速等值線
        contourf = plt.contourf(self.lon, self.lat, div, cmap='jet')  # 繪制風速的等值線圖
        cbar = plt.colorbar(contourf, location='bottom', orientation='horizontal')  # 添加顏色條
        cbar.ax.tick_params(labelsize=7)
        cbar.set_label("divergence")  # 顏色條的標籤

         # 繪制地形等值線
        contour = plt.contour(self.lon, self.lat, self.h[0, :, :], levels=np.linspace(10600, 12800, 12), colors='white')
        plt.clabel(contour, inline=True, fontsize=8, colors='white')  # 添加地形等值線標籤

        # 添加網格線
        ax.gridlines(draw_labels=[True, "x", "y", "bottom", "left"], linewidth=0.5, color='gray', alpha=0.5, linestyle='--')

         # 繪制風矢量
        plt.quiver(self.lon[::2], self.lat[::2], u[::2, ::2], v[::2, ::2], scale_units='xy', scale=4, color='black')

        # 保存圖形為文件
        plt.savefig(title[6:] + "/" + title+".png")

        # 顯示圖形
        plt.show()

    def plot_data(self,title):
        # 創建保存繪圖結果的目錄，去掉文件名的前6個字元
        pressure =  [200, 500, 1000]  # 設定繪圖的層面

        os.makedirs(title, exist_ok=True)
        # 計算風速
        wspd = (self.u**2 + self.v**2)**0.5

        # 創建風標圖
        for i in range(len(pressure)):
            wind_level = 20-5*i #風標風速
            plt.figure(dpi=400)  # 創建一個新的圖形，設置DPI（每英寸點數）為400
            ax = plt.axes(projection=ccrs.PlateCarree())  # 使用PlateCarree地圖投影
            ax.set_extent([80, 170, 20, 65], crs=ccrs.PlateCarree())  # 設定地圖的範圍
            ax.add_feature(cfeature.LAND)  # 添加陸地特徵
            ax.add_feature(cfeature.COASTLINE)  # 添加海岸線特徵
            ax.add_feature(cfeature.BORDERS)  # 添加國界特徵
            titles = str(pressure[i])+title
            ax.set_title(titles)  # 設置圖形標題

            # 繪制風速等值線
            contourf = plt.contourf(self.lon, self.lat, wspd[i,:,:], cmap='jet')  # 繪制風速的等值線圖
            cbar = plt.colorbar(contourf, location='bottom', orientation='horizontal')  # 添加顏色條
            # cbar.ax.tick_params(labelsize=7)
            cbar.set_label("wind speed(m/s)")  # 顏色條的標籤

            # 繪制地形等值線
            contour = plt.contour(self.lon, self.lat, self.h[i, :, :],  colors='white')
            plt.clabel(contour, inline=True, fontsize=8, colors='white')  # 添加地形等值線標籤

            # 添加網格線
            ax.gridlines(draw_labels=[True, "x", "y", "bottom", "left"], linewidth=0.5, color='gray', alpha=0.5, linestyle='--')

            # 繪制風矢量
            q = plt.quiver(self.lon[::2], self.lat[::2], self.u[i,::2, ::2], self.v[i,::2, ::2], scale_units='xy', scale=10-3*i, color='black')
            qk = plt.quiverkey(q, 0.8, 1.05, wind_level, str(wind_level)+' m/s', labelpos='E', coordinates='axes', fontproperties={'size': 8})#圖例

            # 保存圖形為文件
            plt.savefig(title + "/" + titles+".png")

            # 顯示圖形
            plt.show()
       


if __name__ == "__main__":
    filename = '../data/fnldata.dat'  # 資料文件的名稱
    data_plotter = MyDataPlotter(filename)  # 創建MyDataPlotter類的實例
    data_plotter.load_data()  # 載入資料
    data_plotter.configure_parameters()  # 配置參數
    ug,vg = data_plotter.geowind() # 計算地轉風
    data_plotter.plot_wind_vector(ug[0,:,:],vg[0,:,:],"200mb geostrophic wind and height") #繪製200mb高度圖表
    div = data_plotter.Divergence()
    ua,va = data_plotter.nonageowind(ug,vg)  # 計算散度
    data_plotter.plot_wind_divergence(div[0,:,:], ua[0,:,:], va[0,:,:],"200mb geostrophic wind,height and divergence")
    data_plotter.plot_data("wind and height")