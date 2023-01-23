import numpy as np
import netCDF4
import matplotlib.pyplot as plt
from netCDF4 import Dataset as NetCDFFile 
import pandas as pd

#----------------regression------------------------
def Regression(x,y,n):
    sumx = 0 #the sum of x
    sumy = 0 # the sum of y
    sumxy = 0 # the sum of x*y
    sumx2 = 0 # the sum of x^2
    st = 0    # sum of squares of residual between y and the mean
    sr = 0    # sum of squares of residual between data y and the y calculated with the linear model
    for i in range(n):
        sumx = sumx + x[i]
        sumy = sumy + y[i]
        sumxy = sumxy +x[i]*y[i]
        sumx2 = sumx2 +x[i]*x[i]
    xm = sumx/n # the mean of x
    ym = sumy/n # the mean of y
    #print(ym)
    a1 = (n*sumxy - sumx*sumy)/(n*sumx2 - sumx*sumx)
    a0 = ym -a1*xm
    for i in range(n):
        st = st + (y[i]-ym)**2.
        sr = sr + (y[i]-a0-a1*x[i])**2
    #print(sr)
    #print(n)
    syx = (sr/(n-2))**0.5 #standard error of the estimate 
    r2 = (st-sr)/st       #coefficient of determination
    r = ((st-sr)/st)**0.5 #coefficient of correlation
    return a0,a1,syx,r2,r


#----------plot------------------
def plot_data(area3mean_sst, fishnew1, a0, a1, r2, i):
    ax = plt.figure()
    month_list = ["JFM", "FMA", "MAM", "AMJ", "MJJ", "JJA", "JAS", "ASO", "SON", "OND", "NDJ", "DJF"]
    
    plt.scatter(area3mean_sst,fishnew1)
    xx = np.arange(np.min(area3mean_sst),np.max(area3mean_sst),0.1)
    yre = a0+a1*xx
    plt.plot(xx,yre)
    plt.xlabel('SST')
    plt.ylabel('catch')
    plt.title('Linear regression of %s SST and the yearly Sardine catch' % month_list[i])
    plt.text(np.min(area3mean_sst), 500000, "y= {:.2f} + {:.2f}x\n r$^2$={:.2f}".format(a0, a1, r2), fontsize = 12)
    plt.savefig('%s.jpg'%month_list[i],dpi=100)
    plt.show()
    
nc = NetCDFFile('sst.mon.mean.nc')
#print(nc.variables)
lats = nc.variables['lat'][:]#89.5、88.5....-89.5
lons = nc.variables['lon'][:]#0.5、1.5...359.5
dtime = netCDF4.num2date(nc['time'][:], nc['time'].units)#tranform to datetime
print(dtime[1259])
print(dtime[1571])

#---------area mean sst data-----------
area3mean_sst_list = []

for i in range(1248, 1260):
    print(i)
    area3mean_sst = []
    if i == 1258:
        for j in range(i,i+313,12):
            sst = (np.mean(nc.variables['sst'][j,47:64,126:145])+np.mean(nc.variables['sst'][j+1,47:64,126:145])+np.mean(nc.variables['sst'][j-10,47:64,126:145]))/3.
            area3mean_sst.append(sst)
    elif i == 1259:
        for j in range(i,i+313,12):
            sst = (np.mean(nc.variables['sst'][j,47:64,126:145])+np.mean(nc.variables['sst'][j+1,47:64,126:145])+np.mean(nc.variables['sst'][j-11,47:64,126:145]))/3.
            area3mean_sst.append(sst)
    else:
        for j in range(i,i+313,12):#i in range(1248,1561,12),the final i is 1560
            sst = (np.mean(nc.variables['sst'][j,47:64,126:145])+np.mean(nc.variables['sst'][j+1,47:64,126:145])+np.mean(nc.variables['sst'][j+2,47:64,126:145]))/3.
            area3mean_sst.append(sst)
    area3mean_sst_list.append(area3mean_sst)
    
#-----------catching data-----------
data = pd.read_csv("./sardine.csv", header=None)
#print(data)
new = data.values.tolist()
fish=[]
n = len(new)
for i in range (1,n):
    a = new[i]
    fish.append(a)
#print(fish)
fishnew = []
for i in fish:
    fishnew.append(float(i[0]))
#print(fishnew)
fishnew1 = fishnew[::-1]#reorganize the martix,2021 to 1995,transfrom to 1995-2021
#print(fishnew1)

a0_arr,a1_arr,syx_arr,r2_arr,r_arr  = [], [], [], [], []
#print(len(area3mean_sst_list))
for i in range(len(area3mean_sst_list)):
    a0,a1,syx,r2,r = Regression(area3mean_sst_list[i],fishnew1,27)
    a0_arr.append(a0)
    a1_arr.append(a1)
    syx_arr.append(syx)
    r2_arr.append(r2)
    r_arr.append(r)
#print(a0_arr)
#print(a1_arr)
for i in range(12):
    print("regression equation is y=%f+%fx,standard error of the estimate is %f,coefficient of correlation is %f"%(a0_arr[i],a1_arr[i],syx_arr[i],r_arr[i]))
    plot_data(area3mean_sst_list[i], fishnew1, a0_arr[i], a1_arr[i], r2_arr[i], i)