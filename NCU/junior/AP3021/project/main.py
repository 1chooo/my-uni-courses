import csv
import requests
import numpy as np


def deal_data(station_code, station_name, report_items):
    CSV_URL = f'https://agr.cwb.gov.tw/NAGR/history/station_day/create_report?station={station_code}&start_time=2017-01-01&end_time=2021-12-31&items={report_items}&report_type=csv&level={station_name}'

    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8', "ignore")
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        i = 1
        df = []
        #print(f"{station_code} 2017-01-01 to 2021-12-31 {report_items}\n")
        for row in my_list:
            jump = [1, 2, 35, 36, 37, 38, 71, 72, 73, 74, 107, 108, 109, 110, 143, 144, 145, 146, 179, 180]
            if i not in jump:
                df.append(row)
            i += 1

    data = np.zeros((5, 12, 31))
    for i in range(len(data)):
        for j in range(len(data[i])):
            for k in range(len(data[i][j])):
                if df[32 * i + k + 1][j + 1] == '/' or df[32 * i + k + 1][j + 1] == '':
                    df[32 * i + k + 1][j + 1] = '0.'

                data[i][j][k] = float(df[32 * i + k + 1][j + 1])

    data_mean = np.zeros((12, 31))
    for j in range(len(data_mean)):
        for k in range(len(data_mean[j])):
            item = 0
            tmp_sum = 0.
            for i in range(len(data)):
                if data[i][j][k] != 0.:
                    item += 1
                    tmp_sum += data[i][j][k]
                    # print(data[i][j][k])
                else:
                    pass
            if item != 0:
                data_mean[j][k] = tmp_sum / item
            else:
                pass

    #print(data_mean)
    return data_mean

code = ['72G600', 'G2F820']
name = ['臺中農改', '農業試驗所']
number = int(input("number ="))
T_max = deal_data(code[number], name[number], 'TxMaxAbs')
T_min = deal_data(code[number], name[number], 'TxMinAbs')
Tb = float(input("Tb ="))


def MGDD_list_month(T_max, T_min, Tb):
    mgdd = []
    for i in range(12):
        mgdd.append([])
        for j in range(31):
            if T_max[i][j] == 0.:
                continue
            elif i == 1 and j == 28:
                continue
            if T_max[i][j] <= 30.:
                tmax = T_max[i][j]
            else:
                tmax = 30.
            if T_min[i][j] >= Tb:
                tmin = T_min[i][j]
            else:
                tmax = Tb
            T = (tmax + tmin) / 2
            mgdd[i].append(T - Tb)
        #print(mgdd[i])
    return mgdd

mgdd_month = MGDD_list_month(T_max, T_min, Tb)

def MGDD_list(T_max, T_min, Tb):
    mgdd = []
    for i in range(12):
        for j in range(31):
            if T_max[i][j] == 0.:
                continue
            elif i == 1 and j == 28:
                continue
            if T_max[i][j] <= 30.:
                tmax = T_max[i][j]
            else:
                tmax = 30.
            if T_min[i][j] >= Tb:
                tmin = T_min[i][j]
            else:
                tmax = Tb
            T = (tmax + tmin) / 2
            mgdd.append(T - Tb)
    return mgdd

mgdd = MGDD_list(T_max, T_min, Tb)

from datetime import datetime,timedelta
def start_day_Tsum(start_year, start_month, start_day, mgdd):
    start_time = datetime(start_year, start_month, start_day)
    delta_days = (start_time - datetime(2022,1,1)).days
    new_mgdd = mgdd[delta_days:] + mgdd[:delta_days]
    sigma_new_mgdd = []
    tsum = 0
    for i in range(len(new_mgdd)):
        tsum += new_mgdd[i]
        sigma_new_mgdd.append(tsum)
    #print(sigma_new_mgdd)
    return sigma_new_mgdd

start_year = int(input("start year(Ex:2022) ="))
start_month = int(input("start month(Ex:3) ="))
start_day = int(input("start day(Ex:14) ="))
sigma_new_mgdd = start_day_Tsum(start_year, start_month, start_day, mgdd)

def NewtInt(x, y, n, xi, yint, ea):
    fdd = np.zeros((n+1,n+1))
    for i in range(n+1):
        fdd[i][0] = y[i]
    for j in range(1,n+1):
        for i in range(n-j+1):
            fdd[i][j] = (fdd[i+1][j-1] - fdd[i][j-1]) / (x[i+j] - x[i])
    #print(fdd[0])
    xterm = 1
    yint[0] = fdd[0][0]
    for order in range(1, n+1):
        xterm = xterm * (xi - x[order-1])
        yint2 = yint[order-1] + fdd[0][order] * xterm
        ea[order - 1] = yint2 - yint[order - 1]
        yint[order] = yint2
    return yint[n]

x = np.array([0,100,200,300,364])
y = np.array([0,sigma_new_mgdd[99],sigma_new_mgdd[199],sigma_new_mgdd[299],sigma_new_mgdd[363]])
n = len(x)-1

def fdd_NewtInt(x, y, n):
    fdd = np.zeros((n+1,n+1))
    for i in range(n+1):
        fdd[i][0] = y[i]
    for j in range(1,n+1):
        for i in range(n-j+1):
            fdd[i][j] = (fdd[i+1][j-1] - fdd[i][j-1]) / (x[i+j] - x[i])
    return fdd[0]


def f_x(n, xi, yint, f, theta):
    xterm = 1
    yint[0] = f[0]
    for order in range(1, n):
        xterm = xterm * (xi - x[order-1])
        yint2 = yint[order-1] + f[order] * xterm
        yint[order] = yint2
    return yint[n-1]-theta

def f_1x(xi, f):
    tmp_sum = 0.
    tmp_sum += float(f[1])
    tmp_sum += float(f[2]) * (2*xi-100)
    tmp_sum += float(f[3]) * (3*xi**(2) - 600 * xi + 20000)
    tmp_sum += float(f[4]) * (4 * xi**(3) - 1800 * xi**(2) + 220000 * xi - 6000000)
    return tmp_sum

def output_days(theta, old_x, n, yint, f):
    while True:
        new_x = old_x - f_x(n, old_x, yint, f, theta)/f_1x(old_x, f)
        if (new_x - old_x) / new_x <= 0.0005:
            return new_x
        else:old_x = new_x

theta = float(input("theta ="))
old_x = 1
yint = np.zeros(n)
f = fdd_NewtInt(x, y, n)
days = output_days(theta, old_x, n, yint, f)
days = int(np.ceil(days))
print("預估天數 =", days)
print("實際積溫累積 =",sigma_new_mgdd[days])

start_time = datetime(start_year, start_month, start_day)
end_time = start_time + timedelta(days = days)
print(end_time)
