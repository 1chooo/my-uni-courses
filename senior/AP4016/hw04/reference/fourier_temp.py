import numpy as np  # 匯入NumPy套件，用於處理數值數據
import matplotlib.pyplot as plt  # 匯入Matplotlib套件，用於繪圖
import math

def read_file(filename):
    # 定義函數用於讀取文件，將每一行轉換為數值並存入列表
    # 假設文件中只包含數值，沒有其他文本
    # 返回包含數值的列表
    data = []
    with open(filename, 'r') as file:
        for line in file:
            # 將每一行的內容轉換為浮點數
            number = float(line.strip())
            data.append(number)
    return data

temparature = read_file("./data/T.dat.txt")  # 讀取文件並將數值存入名為temparature的列表

def fourier_trapezoidal(data):
    # 定義梯形法進行傅立葉分析的函數
    # 返回a0、an、bn
    n = 243
    pi = np.pi
    h = 2 * pi / (len(data)-1)
    a0 = 0
    an = []
    bn = []

    # 計算a0
    for i in range(len(data)-1):
        # 使用梯形法計算積分近似值
        a0 += ((data[i] + data[i+1])/2) * h / (2 * pi)

    # 計算an
    for i in range(n):
        value = 0
        x = np.linspace(-pi, pi, len(data))
        for j in range(len(data)-1):
            # 使用梯形法計算an的積分近似值
            value += ((data[j] * np.cos((i+1) * x[j]) + data[j+1] * np.cos((i+1) * x[j+1])) / 2) * h / pi
        an.append(value)

    # 計算bn
    for i in range(n):
        value = 0
        x = np.linspace(-pi, pi, len(data))
        for j in range(len(data)-1):
            # 使用梯形法計算bn的積分近似值
            value += ((data[j] * np.sin((i+1) * x[j]) + data[j+1] * np.sin((i+1) * x[j+1])) / 2) * h / pi
        bn.append(value)

    return a0, an, bn


def fourier_simpson(data):
    # 定義辛普森法進行傅立葉分析的函數
    # 返回a0、an、bn
    n = 243
    pi = np.pi
    h = 2 * pi / (len(data)-1)
    a0 = 0
    an = []
    bn = []
    
    # 計算a0
    for i in range(0, len(data)-2, 2):
        a0 += ((data[i] + 4*data[i+1] + data[i+2])/3) * h / (2 * pi)
    
    # 計算an
    for i in range(n):
        value = 0
        x = np.linspace(-pi, pi, len(data))
        for j in range(0, len(data)-2, 2):
            value += (data[j] * np.cos((i+1)*x[j]) + 4*data[j+1] * np.cos((i+1)*x[j+1]) + data[j+2] * np.cos((i+1)*x[j+2]))/3 * h/pi
        an.append(value)
    
    # 計算bn
    for i in range(n):
        value = 0
        x = np.linspace(-pi, pi, len(data))
        for j in range(0, len(data)-2, 2):
            value += (data[j] * np.sin((i+1)*x[j]) + 4*data[j+1] * np.sin((i+1)*x[j+1]) + data[j+2] * np.sin((i+1)*x[j+2]))/3 * h/pi
        bn.append(value)
    
    return a0, an, bn

def fourier_leoticks(data):
    # 定義Leoticks方法進行傅立葉分析的函數
    # 返回a0、an、bn
    n = 243
    pi = np.pi
    h = 2 * pi / (len(data)-1)
    a0 = 0
    an = []
    bn = []
    
    # 計算a0
    for i in range(0, len(data)-2, 2):
        a0 += ((data[i] + 4*data[i+1] + data[i+2])/3) * h / (2 * pi)
    
    # 計算an
    for i in range(n):
        value = 0
        x = np.linspace(-pi, pi, len(data))
        for j in range(0, len(data)-2, 2):
            value += (1.0752*data[j] * np.cos((i+1)*x[j]) + 3.8496*data[j+1] * np.cos((i+1)*x[j+1]) + 1.0752*data[j+2] * np.cos((i+1)*x[j+2]))/3 * h/pi
        an.append(value)
    
    # 計算bn
    for i in range(n):
        value = 0
        x = np.linspace(-pi, pi, len(data))
        for j in range(0, len(data)-2, 2):
            value += (1.0752*data[j] * np.sin((i+1)*x[j]) + 3.8496*data[j+1] * np.sin((i+1)*x[j+1]) + 1.0752*data[j+2] * np.sin((i+1)*x[j+2]))/3 * h/pi
        bn.append(value)
    
    return a0, an, bn
    
a0t, ant, bnt = fourier_trapezoidal(temparature)  # 使用梯形法進行傅立葉分析
a0s, ans, bns = fourier_simpson(temparature)  # 使用辛普森法進行傅立葉分析
a0l, anl, bnl = fourier_leoticks(temparature)  # 使用Leoticks方法進行傅立葉分析

def power_spectral(an, bn, title):
    # 定義函數用於計算功率頻譜，並繪製頻譜圖
    # 返回功率頻譜
    x = np.linspace(1,243,243)
    fx = np.zeros(len(an))
    for n in range(243):
        fx[n] = (an[n]**2+bn[n]**2)**0.5
    plt.figure(dpi=400)
    plt.xticks(np.arange(min(x)-1, max(x), 30))
    plt.title(title + " for temperature")
    plt.xlabel("wave number")
    plt.ylabel("amplitude")
    plt.plot(x[1:],fx[1:])
    plt.grid('--')
    plt.savefig("temperature/t_spec " + title + ".jpg")
    plt.show()
    return fx

spectral_trapezoidal = power_spectral(ant, bnt, "trapezoidal")  # 計算梯形法的功率頻譜
spectral_simpson = power_spectral(ans, bns, "simpson")  # 計算辛普森法的功率頻譜
spectral_leoticks = power_spectral(anl, bnl, "leoticks")  # 計算Leoticks方法的功率頻譜

def half(a0, an, bn, data, title):
    # 定義函數用於繪製原始數據和傅立葉分析的前兩項的波形
    # 包括全年和半年的結果
    # 將圖片保存為文件
    pi = np.pi
    time = np.linspace(1, 729, 729)
    plt.figure(dpi=400)
    x = np.linspace(-pi, pi, 729)
    plt.plot(time, data, label='original', color="black")
    fx = np.zeros((2, 729))

    for i in range(2):
        for j in range(729):
            value = a0 + an[i]*np.cos((i+1)*x[j]) + bn[i]*np.sin((i+1)*x[j])
            fx[i, j] = value

    plt.plot(time, fx[0, :], color='blue', label="year")
    plt.plot(time, fx[1, :], color='red', label="half")
    plt.legend()
    plt.ylabel("temperature (C)")
    plt.xlabel("time")
    plt.title("temperature period " + title)
    plt.grid('--')
    plt.savefig("temperature/t_period " + title + ".jpg")
    plt.show()

half(a0t, ant, bnt, temparature, "trapezoidal")  # 繪製梯形法的波形圖
half(a0s, ans, bns, temparature, "simpson")  # 繪製辛普森法的波形圖
half(a0l, anl, bnl, temparature, "leoticks")  # 繪製Leoticks方法的波形圖

def extreme(fx,an,bn):
    # 計算振幅、相位、時間
    # 創建一個包含元素和索引的元組列表
    indexed_lst = list(enumerate(fx))
    
    # 使用sorted將元組列表按值進行降序排序
    sorted_lst = sorted(indexed_lst, key=lambda x: x[1], reverse=True)
    
    top_five_indices = [index for index, value in sorted_lst[:5]]
    incremented_indices = [index + 1 for index in top_five_indices]
    print(incremented_indices)
    amplitude = []
    phase = []
    date = []
    for i in top_five_indices:
        amplitude.append(round(np.sqrt(an[i]**2+bn[i]**2),2))
        if np.arctan(-bn[i]/an[i])>0:
            phase.append(round(np.arctan(-bn[i]/an[i])-2*np.pi,2))
        else:
            phase.append(round(np.arctan(-bn[i]/an[i]),2))
        if np.arctan(-bn[i]/an[i])>0:
            value = -(np.arctan(-bn[i]/an[i])-2*np.pi)/(i+1)/(2*np.pi)*365/(i+1)
        else:
            value = -(np.arctan(-bn[i]/an[i]))/(i+1)/(2*np.pi)*365/(i+1)
        date.append(math.ceil(value))
    
    print(amplitude)
    print(phase)
    print(date)
    
extreme(spectral_trapezoidal,ant,bnt)
extreme(spectral_simpson,ans,bns)
extreme(spectral_leoticks,anl,bnl)

def reduction(a0,an,bn,data,title):
    #使用傅立葉分析還原原始數據
    time = np.linspace(1,729,729)
    pi = np.pi
    plt.figure(dpi=400)
    x = np.linspace(-pi,pi,729)
    plt.plot(time,data,label='original',color="black")
    fx =  np.zeros(729)+a0

    for i in range(243):
        for j in range(729):
            value = an[i]*np.cos((i+1)*x[j])+bn[i]*np.sin((i+1)*x[j])
            fx[j] += value

    plt.plot(time,fx,color='red',label='fourier', linestyle="--")
    plt.legend()
    plt.ylabel("temparature (hpa)")
    plt.xlabel("time")
    plt.title("temparature retuction "+title)
    plt.grid('--')
    plt.savefig("reduction/t_period "+title+".jpg")
    plt.show()

reduction(a0t, ant, bnt, temparature, "trapezoidal")  # 繪製梯形法的波形圖
reduction(a0s, ans, bns, temparature, "simpson")  # 繪製辛普森法的波形圖
reduction(a0l, anl, bnl, temparature, "leoticks")  # 繪製Leoticks方法的波形圖