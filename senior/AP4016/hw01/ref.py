import numpy as np  # 引入NumPy庫，用於數值計算
import cartopy.crs as ccrs  # 引入Cartopy庫，用於地圖投影和地理資料可視化
import matplotlib.pyplot as plt  # 引入Matplotlib庫，用於繪圖
import cartopy.feature as cfeature  # 引入Cartopy的特徵模組，用於地圖特徵的添加
import os  # 引入os模組，用於操作文件路徑和目錄

class MyDataPlotter:
    def __init__(self, filename):
        self.filename = filename  # 初始化類的實例，設定資料檔案的文件名稱
        self.nlat = 25  # 緯度格點數，指定緯度方向上的格點數量
        self.mlon = 49  # 經度格點數，指定經度方向上的格點數量
        self.nlev = 5   # 垂直層數，指定垂直層數量
        self.var = 4    # 變數數量，指定資料中的變數數量
        self.dy = 6378000 * 1.875 * np.pi/180  # 經度間距對應的米數，計算經度方向上的距離
        self.omega = 7.29*100000  # 地球自轉速率

    def load_data(self):
        # 載入資料
        self.data = np.fromfile(self.filename, dtype='<f4')  # 從二進制文件讀取數據，並指定數據類型為32位浮點數
        self.data = self.data.reshape(self.var, self.nlev,  self.nlat, self.mlon)  # 重塑數據形狀為指定的維度

    def configure_parameters(self):
        # 設定參數
        self.lon = np.linspace(90, 180, self.mlon)  # 經度範圍，生成經度的範圍數據
        self.lat = np.linspace(15, 60, self.nlat)   # 緯度範圍，生成緯度的範圍數據
        self.h = self.data[0, :, :, :]  # 高度場，提取數據中的高度場信息
        self.u = self.data[1, :, :, :]  # 東向風場，提取數據中的東向風場信息
        self.v = self.data[2, :, :, :]  # 北向風場，提取數據中的北向風場信息
        self.t = self.data[3, :, :, :]  # 溫度場，提取數據中的溫度場信息

    def horizental_temparature_advection(self):
        # 計算水平溫度平流
        t_adv = np.zeros([self.nlev,  self.nlat,self.mlon])  # 創建一個全零數組來存儲水平溫度平流
        for i in range(self.nlev):  # 遍歷垂直層
            for j in range(self.nlat):  # 遍歷緯度
                for k in range(self.mlon):  # 遍歷經度
                    if 1 <= j < self.nlat - 1 and 1 <= k < self.mlon - 1:  # 檢查經度和緯度的範圍
                        dx = self.dy * np.cos(self.lat[j] * np.pi / 180)  # 計算經度間距
                        xvalue = self.u[i, j, k] * (self.t[i, j, k + 1] - self.t[i, j, k - 1]) / (2 * dx)  # 計算x方向上的差分
                        yvalue = self.v[i, j, k] * (self.t[i, j + 1, k] - self.t[i, j - 1, k]) / (2 * self.dy)  # 計算y方向上的差分
                        t_adv[i, j, k] = -xvalue - yvalue  # 計算水平溫度平流
                    else:
                        # 單邊插植
                        dx = self.dy * np.cos(self.lat[j] * np.pi / 180)  # 計算經度間距
                        if k == 0:
                            xvalue = self.u[i, j, k] * (self.t[i, j, k + 1] - self.t[i, j, k]) / dx  # 計算x方向上的差分
                        elif k == self.mlon - 1:
                            xvalue = self.u[i, j, k] * (self.t[i, j, k] - self.t[i, j, k - 1]) / dx  # 計算x方向上的差分
                        else:
                            xvalue = (self.u[i, j, k + 1] - self.u[i, j, k - 1]) / (2 * dx)  # 計算x方向上的差分

                        if j == 0:
                            yvalue = self.v[i, j, k] * (self.t[i, j + 1, k] - self.t[i, j, k]) / self.dy  # 計算y方向上的差分
                        elif j == self.nlat - 1:
                            yvalue = self.v[i, j, k] * (self.t[i, j, k] - self.t[i, j - 1, k]) / self.dy  # 計算y方向上的差分
                        else:
                            yvalue = self.v[i, j, k] * (self.t[i, j + 1, k] - self.t[i, j - 1, k]) / (2 * self.dy)  # 計算y方向上的差分

                        t_adv[i, j, k] = xvalue + yvalue  # 計算水平溫度平流

        return t_adv

    def Divergence(self):
        # 計算散度
        div = np.zeros([self.nlev,  self.nlat,self.mlon])  # 創建一個全零數組來存儲散度
        for i in range(self.nlev):  # 遍歷垂直層
            for j in range(self.nlat):  # 遍歷緯度
                for k in range(self.mlon):  # 遍歷經度
                    if 1 <= j < self.nlat - 1 and 1 <= k < self.mlon - 1:  # 檢查經度和緯度的範圍
                        dx = self.dy * np.cos(self.lat[j] * np.pi / 180)  # 計算經度間距
                        xvalue = (self.u[i, j, k + 1] - self.u[i, j, k - 1]) / (2 * dx)  # 計算x方向上的差分
                        yvalue = (self.v[i, j + 1, k] - self.v[i, j - 1, k]) / (2 * self.dy)  # 計算y方向上的差分
                        div[i, j, k] = xvalue + yvalue  # 計算散度
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

                        div[i, j, k] = xvalue + yvalue  # 計算散度

        return div

    def Relative_Vorticity(self):
        # 計算相對渦度
        rv = np.zeros([self.nlev,  self.nlat,self.mlon])  # 創建一個全零數組來存儲相對渦度
        for i in range(self.nlev):  # 遍歷垂直層
            for j in range(self.nlat):  # 遍歷緯度
                for k in range(self.mlon):  # 遍歷經度，
                    if 1 <= j < self.nlat - 1 and 1 <= k < self.mlon - 1:  # 檢查經度和緯度的範圍
                        dx = self.dy * np.cos(self.lat[j] * np.pi / 180)  # 計算經度間距
                        xvalue = (self.v[i, j, k + 1] - self.v[i, j, k - 1]) / (2 * dx)  # 計算x方向上的差分
                        yvalue = (self.u[i, j + 1, k] - self.u[i, j - 1, k]) / (2 * self.dy)  # 計算y方向上的差分
                        rv[i, j, k] = xvalue - yvalue  # 計算相對渦度
                    else:
                        # 單邊插植
                        dx = self.dy * np.cos(self.lat[j] * np.pi / 180)  # 計算經度間距
                        if k == 0:
                            xvalue = (self.v[i, j, k + 1] - self.v[i, j, k]) /  dx  # 計算x方向上的差分
                        elif k == self.mlon - 1:
                            xvalue = (self.v[i, j, k] - self.v[i, j, k - 1]) / dx  # 計算x方向上的差分
                        else:
                            xvalue = (self.v[i, j, k + 1] - self.v[i, j, k - 1]) / (2 * dx)  # 計算x方向上的差分
                        
                        if j == 0:
                            yvalue = (self.u[i, j + 1, k] - self.u[i, j, k]) / self.dy  # 計算y方向上的差分
                        elif j == self.nlat - 1:
                            yvalue = (self.u[i, j, k] - self.u[i, j - 1, k]) / self.dy  # 計算y方向上的差分
                        else:
                            yvalue = (self.u[i, j + 1, k] - self.u[i, j - 1, k]) / (2 * self.dy)  # 計算y方向上的差分
                        
                        rv[i, j, k] = xvalue - yvalue  # 計算相對渦度
        return rv

    def Absolute_Vorticity_Advection(self, vor):
        # 計算絕對渦度平流
        Vor_adv = np.zeros([self.nlev,  self.nlat,self.mlon])  # 創建一個全零數組來存儲絕對渦度平流
        for i in range(self.nlev):  # 遍歷垂直層
            for j in range(self.nlat):  # 遍歷緯度
                for k in range(self.mlon):  # 遍歷經度
                    if 1 <= j < self.nlat - 1 and 1 <= k < self.mlon - 1:  # 檢查經度和緯度的範圍
                        dx = self.dy * np.cos(self.lat[j] * np.pi / 180)  # 計算經度間距
                        xvalue = self.u[i, j, k] * (vor[i, j, k + 1] - vor[i, j, k - 1]) / (2 * dx)  # 計算x方向上的差分
                        yvalue = self.v[i, j, k] * (vor[i, j + 1, k] - vor[i, j - 1, k] + 2 * 7.29 * (10 ** -5) * np.sin(self.lat[j + 1] * np.pi / 180) - 2 * 7.29 * (10 ** -5) * np.sin(self.lat[j - 1] * np.pi / 180)) / (2 * self.dy)  # 計算y方向上的差分
                    else:
                        # 單邊插植
                        dx = self.dy * np.cos(self.lat[j] * np.pi / 180)  # 計算經度間距
                        if k == 0:
                            xvalue = (self.u[i, j, k] * (vor[i, j, k + 1] - vor[i, j, k])) /  dx  # 計算x方向上的差分
                        elif k == self.mlon - 1:
                            xvalue = (self.u[i, j, k] * (vor[i, j, k] - vor[i, j, k - 1])) / dx  # 計算x方向上的差分
                        else:
                            xvalue = self.u[i, j, k] * (vor[i, j, k + 1] - vor[i, j, k - 1]) / (2 * dx)  # 計算x方向上的差分
                        
                        if j == 0:
                            yvalue = self.v[i, j, k] * (vor[i, j + 1, k] - vor[i, j, k] + 2 * 7.29 * (10 ** -5) * np.sin(self.lat[j + 1] * np.pi / 180) - 2 * 7.29 * (10 ** -5) * np.sin(self.lat[j] * np.pi / 180)) / self.dy  # 計算y方向上的差分
                        elif j == self.nlat - 1:
                            yvalue = self.v[i, j, k] * (vor[i, j, k] - vor[i, j - 1, k] + 2 * 7.29 * (10 ** -5) * np.sin(self.lat[j] * np.pi / 180) - 2 * 7.29 * (10 ** -5) * np.sin(self.lat[j - 1] * np.pi / 180)) / self.dy  # 計算y方向上的差分
                        else:
                            yvalue = self.v[i, j, k] * (vor[i, j + 1, k] - vor[i, j - 1, k] + 2 * 7.29 * (10 ** -5) * np.sin(self.lat[j + 1] * np.pi / 180) - 2 * 7.29 * (10 ** -5) * np.sin(self.lat[j - 1] * np.pi / 180)) / (2 * self.dy)  # 計算y方向上的差分
                    Vor_adv[i, j, k] = -xvalue - yvalue  # 計算絕對渦度平流
        return Vor_adv

    def plot_data(self, factor, title, label):
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
            contour = ax.contourf(self.lon, self.lat, var, cmap='jet')  # 使用色塊表示資料
            file = str(levels[level]) + title  # 構建保存文件的名稱
            ax.set_title(file)  # 設定圖表的標題
            ax.gridlines(draw_labels=[True, "x", "y", "bottom", "left"], linewidth=0.5, color='gray', alpha=0.5, linestyle='--')  # 添加網格線

            cbar = plt.colorbar(contour, ax=ax, orientation='vertical', shrink=0.7, label=label)  # 添加色標
            plt.savefig(title[4:] + "/" + file + ".png")  # 保存圖表為圖片文件
            plt.show()  # 顯示圖表

if __name__ == "__main__":
    # 設定輸入檔案名稱
    filename = 'output.bin'

    # 創建一個 MyDataPlotter 的實例，並傳入檔案名稱
    data_plotter = MyDataPlotter(filename)

    # 載入資料，將檔案內容轉換為 NumPy 陣列
    data_plotter.load_data()

    # 設定模型的參數，包括經度、緯度、高度場、風場和溫度場等
    data_plotter.configure_parameters()

    # 計算水平溫度平流，並將結果乘以 10000，以表示單位為 10^-4 / s
    t_adv = data_plotter.horizental_temparature_advection()

    # 計算散度，並將結果乘以 100000，以表示單位為 10^-5 / s
    div = data_plotter.Divergence()

    # 計算相對渦度，並將結果乘以 100000，以表示單位為 10^-5 / s
    rv = data_plotter.Relative_Vorticity()

    # 計算絕對渦度平流，並將結果乘以 1000000000，以表示單位為 10^-9 / s
    Vor_adv = data_plotter.Absolute_Vorticity_Advection(rv)

    # 繪製水平溫度平流圖，以 10^-4 / s 為單位
    data_plotter.plot_data(t_adv * 10000, 'hpa horizental Temparature advection', "(10^-4/s)")

    # 繪製散度圖，以 10^-5 / s 為單位
    data_plotter.plot_data(div * 100000, 'hpa Divergence', "(10^-5/s)")

    # 繪製相對渦度圖，以 10^-5 / s 為單位
    data_plotter.plot_data(rv * 100000, 'hpa Relative Vorticity', "(10^-5/s)")  

    # 繪製絕對渦度平流圖，以 10^-9 / s 為單位
    data_plotter.plot_data(Vor_adv* 1000000000, 'hpa Absolute_Vorticity_Advection', "(10^-9/s)")

