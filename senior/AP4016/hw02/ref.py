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
    
    def Vertical_Speed(self,div):
        vs = np.zeros([self.nlev,  self.nlat,self.mlon])  # 創建一個全零數組來存儲垂直風速
        p = [85,150,175,200,300]  # 高度層壓力值的列表
        #initial vertical speed
        for i in range(self.nlev):  # 遍歷垂直層
            for j in range(self.nlat):  # 遍歷緯度
                for k in range(self.mlon):  # 遍歷經度
                    if i == 0:
                        vs[i, j, k] = div[i, j, k]*p[i]  # 初始化垂直風速
                    elif i > 0:
                        vs[i, j, k] = vs[i-1, j, k]+div[i, j, k]*p[i]  # 計算垂直風速

        # #correction error
        # # 創建一個形狀為 [5, 25, 49] 的全零的 3D 數組
        expanded_error = np.zeros([5, 25, 49])
        for i in range(self.nlev):  # 遍歷垂直層
            for j in range(self.nlat):  # 遍歷緯度
                for k in range(self.mlon):  # 遍歷經度
                    expanded_error[i,j,k] = vs[4,j,k]/910  # 計算擴展錯誤

        div_new = div - expanded_error  # 修正相對渦度
        # # correction div
        vs_new =  np.zeros([self.nlev,  self.nlat,self.mlon], dtype=float)  # 創建一個全零數組來存儲新的垂直風速
        for i in range(self.nlev):  # 遍歷垂直層
            for j in range(self.nlat):  # 遍歷緯度
                for k in range(self.mlon):  # 遍歷經度                   
                    if i == 0:
                        vs_new [i, j, k] = div_new[i, j, k]*p[i]  # 初始化新的垂直風速
                    elif i > 0:
                        vs_new [i, j, k] = vs_new[i-1, j, k]+div_new[i, j, k]*p[i]  # 計算新的垂直風速
        np.save('w_new.npy', vs_new)  # 將新的垂直風速保存到文件中

        return vs_new
    
    def plot_data(self, factor, title, label):
        # 繪製資料
        level = [1010, 925, 775, 600, 400,100]  # 高度層壓力值的列表
        # os.makedirs(title[5:], exist_ok=True)
        plt.figure(figsize=(6, 3), dpi=400)  # 創建一個畫布，設置圖形大小和DPI
        var = np.zeros((6,25))
        var[1:,:] = factor[:, :, 16]  # 提取指定經度上的數據
        contour = plt.contour(self.lat, level, var, cmap='jet',levels = np.linspace(-0.002,0.002,9))  # 繪製等壓線，用色塊表示資料
        plt.title(title)  # 設置圖形標題
        plt.xticks(np.linspace(15,60,10))  # 設置x軸刻度
        plt.yscale('log')  # 設置 y 軸為對數尺度
        plt.yticks(np.linspace(1000,100,10))  # 設置y軸刻度
        # 設置 y 軸刻度標籤格式為指數形式
        plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.0f'))
        cbar = plt.colorbar(contour, orientation='vertical', shrink=0.7, label=label)  # 添加色標，顯示數據對應的色標
        plt.gca().invert_yaxis()  # 倒轉 y 軸，使得壓力降低時y軸上升
        plt.ylim(1010, 100)  # 設置 y 軸範圍
        # 添加格線
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.savefig(title + ".png")
        plt.show()  # 顯示圖形


if __name__ == "__main__":
    filename = 'output.bin'  # 資料文件的名稱
    data_plotter = MyDataPlotter(filename)  # 創建MyDataPlotter類的實例
    data_plotter.load_data()  # 載入資料
    data_plotter.configure_parameters()  # 配置參數
    div = data_plotter.Divergence()  # 計算相對渦度
    vs = data_plotter.Vertical_Speed(div)  # 計算垂直風速
    data_plotter.plot_data(vs, "120E vetical velocity", "m/s)")  # 繪製資料並顯示
    