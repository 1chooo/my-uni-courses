import numpy as np
import netCDF4
import matplotlib.pyplot as plt
from netCDF4 import Dataset as NetCDFFile 
import pandas as pd

#----------------regression------------------------
def coefficient(x,y,order,n):
    a = np.zeros((order+1,order+2)) #augmented matrix
    for i in range(0,order+1):
        for j in range(0,i+1):
            k = i + j #for example,i=0,j=0, the coeffient is n
            summ = 0
            for l in range(n):
                summ = summ + x[l]**(k) 
                #print(summ)
            a[i][j]=summ
            a[j][i]=summ
        summ = 0
        for l in range(n):#determine the final column of the augmented matrix (b) 
            summ = summ +y[l]*x[l]**(i)
        a[i][order+1] = summ
    return a
episilon = 1
while (episilon+1>1):#computer consider the value is 0,exit the loop
    episilon = episilon/2
episilon = episilon*2 #when we exit the loop，the value is already zero,the lart value is the machine episilon
#print(episilon)

def Pivot(a,b,s,n,k):
    p = k
    big = abs(a[k,k]/s[k]) #normalize
    for ii in range(k+1,n):
        dummy = abs(a[ii,k]/s[ii])#other element need to be normolized,too
        if dummy>big: # we first determine whether use pivoting
            big = dummy #exchange the pivot
            p = ii      #record which row we will exchange
    if p!=k:#other element should be exchanged,too
        for jj in range(k,n):
            dummy = a[p,jj]
            a[p,jj]=a[k,jj]
            a[k,jj]=dummy 
        dummy = b[p]
        b[p] = b[k]
        b[k] = dummy
        dummy = s[p]#element of the matrix which stored maximum should be exchanged,too
        s[p] = s[k]
        s[k] = dummy
        #print(a)
        #print(b)
def Elimate(a,s,n,b,tol,er):
    for k in range(0,n-1):#before elimanation,call pivot function
        Pivot(a,b,s,n,k)
        if abs(a[k,k]/s[k])<tol:#if a is too small(The computer judges as 0),er=-1
            er = -1
            break
        for i in range(k+1,n):#calculate the coefficient of elimation
            factor = a[i,k]/a[k,k]
            for j in range(k,n):#minus the coefficient of the elimination multiply the value 
                a[i,j] = a[i,j] - factor*a[k,j]
            b[i] = b[i] - factor*b[k]
        if abs(a[n-1,n-1]/s[n-1])<tol:#if the value too small(The computer judges as 0),er=-1
            er = -1
        #print(a)
        #print(b)
def Substitute(a,n,b,x):
    x[n-1]=b[n-1]/a[n-1,n-1]#in the final row, we just need to transposition,then can find the solution 
    for i in range(n-2,-1,-1):#Substitute
        sum1 = 0
        for j in range(i+1,n):
            sum1 = sum1 +a[i,j]*x[j]
        x[i] = (b[i]-sum1)/a[i,i]
    return x
def Gauss(a,b,n,x,tol,er):#a is the matrix of coefficent of the linear system,b is the matrix of the term which on the RHS of the equation,n is the size of matrix A, x is the unkown,，tol is a very small value,er is used to decide whether the program run 
    s = np.empty([n], dtype = float)
    er = 0 
    for i in range(n):#store the maximum row in the matrix s
        s[i]=abs(a[i,0])
        for j in range(1,n):
            if abs(a[i,j])>s[i]:
                s[i]=abs(a[i,j])
    Elimate(a,s,n,b,tol,er)#call
    if er!=-1:
        xg =Substitute(a,n,b,x)#call Substitute function
        return xg #return the result
def polynomialreg(x,y,order,n):
    a = coefficient(x,y,order,n)
    anew = Gauss(a[0:order+1,0:order+1],a[:,order+1],order+1,np.empty([order+1], dtype = float),episilon,0)
    st = 0
    sr = 0
    for i in range(n):
        st = st + (y[i]-a[0,order+1]/n)**2. #order=2,because we specify a is an augmented matrix,a[0,3]=Σyi
        sr = sr + (y[i]-anew[0]-anew[1]*x[i]-anew[2]*(x[i]**2))**2
    syx = (sr/(n-(order+1)))**0.5
    r2 = (st-sr)/st
    r = ((st-sr)/st)**0.5
    return anew,syx,r2,r
#anew,syx,r2,r = polynomialreg([1,2,3,4,5,6,7,8,9],[1,1.5,2,3,4,5,8,10,13],2,9)

#----------plot------------------
def plot_data(area3mean_sst, fishnew1, a0, a1, a2, r2, i):
    ax = plt.figure()
    month_list = ["JFM", "FMA", "MAM", "AMJ", "MJJ", "JJA", "JAS", "ASO", "SON", "OND", "NDJ", "DJF"]
    
    plt.scatter(area3mean_sst,fishnew1)
    xx = np.arange(np.min(area3mean_sst),np.max(area3mean_sst),0.1)
    yre = a0+a1*xx+a2*xx**2
    plt.plot(xx,yre)
    plt.xlabel('SST')
    plt.ylabel('catch')
    plt.title('polynomial regression of %s SST and the yearly Sardine catch' % month_list[i])
    plt.text(np.min(area3mean_sst), 500000, "y= {:.2f} + {:.2f}x +{:.2f}x$^2$\n r$^2$={:.2f}".format(a0, a1, a2, r2), fontsize = 9)
    plt.savefig('%s poly.jpg'%month_list[i],dpi=100)
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
a0_arr,a1_arr,a2_arr,syx_arr,r2_arr,r_arr  = [], [], [], [], [], []
for i in range(len(area3mean_sst_list)):
    anew,syx,r2,r = polynomialreg(area3mean_sst_list[i],fishnew1,2,27)
    a0_arr.append(anew[0])
    a1_arr.append(anew[1])
    a2_arr.append(anew[2])
    syx_arr.append(syx)
    r2_arr.append(r2)
    r_arr.append(r)
#print(a0_arr)
#print(a1_arr)
for i in range(12):
    print("regression equation is y=%f+%fx+%f^2,standard error of the estimate is %f,coefficient of correlation is %f"%(a0_arr[i],a1_arr[i],a2_arr[i],syx_arr[i],r_arr[i]))
    plot_data(area3mean_sst_list[i], fishnew1, a0_arr[i], a1_arr[i], a2_arr[i], r2_arr[i], i)