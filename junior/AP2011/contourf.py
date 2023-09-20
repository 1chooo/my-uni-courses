#說明：將探空資料，內差到固定間距的網格上(每五公尺)，再畫等高線。
#note:連續的七天若超過月底，要修改程式!
#==========套件============
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import math

#參數
daytime=7 				#時間
level_wind=30				#風的層數
HH =3000 				#高度
level=600				#資料層
DD = 14                 #起始日期

#讀資料
df=pd.read_csv('./202112_upair.txt',sep='\s+',header=11)  
df=df[1:]
df['yyyymmddhh']=df['yyyymmddhh'].astype('int').astype('str')   #換為整數再換為字串

p = []
t = []
h = []
ws =[]
wd =[]
U=[]    #原來的風場
V=[]


U_int = [] #內插的風場
V_int = [] 
T_int = [] #內差的溫度


#內插的網格
x=np.linspace(DD,DD+daytime-1,7)	# x  	= [14 15 16 17 18 19 20]     #日期
y5=np.linspace(0,HH,level+1)		# y5 	= [0 5 10  ...  2995 3000] 
y100=np.linspace(0,HH,level_wind+1)	# y100  = [0 100 200  ...  2900 3000] #每100m畫一筆風場

#========設定變數==========
for i in range(0,daytime):
    #print(i)
    FT=(df['stno']=='466920')&(df['yyyymmddhh']=='202112'+str(DD+i)+'00')&(df['Heigh']<HH)&(df['Ws']<990) 	#設定條件
    
    PT= df.loc[FT,'Press']								
    TT= df.loc[FT,'Tx']    
    HT= df.loc[FT,'Heigh']
    WST=df.loc[FT,'Ws']
    WDT=df.loc[FT,'Wd']

    p=p+[PT]    # p為list，為p[0]~p[6]
    t=t+[TT]
    h=h+[HT]
    ws=ws+[WST]
    wd=wd+[WDT]

    uu = [-spd*1.943844*math.sin(math.radians(agl)) for spd,agl in zip(ws[i],wd[i])]
    vv = [-spd*1.943844*math.cos(math.radians(agl)) for spd,agl in zip(ws[i],wd[i])]
    U=U+[uu]        #unit:knot
    V=V+[vv]    
#print(U[0]) #unit:knot

#內插
    UU_int = np.interp(y5,h[i],U[i])
    VV_int = np.interp(y5,h[i],V[i])
    TT_int = np.interp(y5,h[i],t[i])
    U_int = U_int+ [UU_int]
    V_int = V_int+ [VV_int]
    T_int = T_int+ [TT_int]   


#串接起來
t_con=np.concatenate([T_int[0],T_int[1],T_int[2],T_int[3],T_int[4],T_int[5],T_int[6]])
U_con=np.concatenate([U_int[0],U_int[1],U_int[2],U_int[3],U_int[4],U_int[5],U_int[6]])
V_con=np.concatenate([V_int[0],V_int[1],V_int[2],V_int[3],V_int[4],V_int[5],V_int[6]])

#print(len(t1_inter))				
#print(len(t))				
#重新分配為contourf可以接受的矩陣			
t_con=np.reshape(t_con,(daytime,level+1)).T
u_con=np.reshape(U_con,(daytime,level+1)).T
v_con=np.reshape(V_con,(daytime,level+1)).T


#==========將網格風場每100m取點==========
Vf,Uf=[],[]
for i in range(0,level_wind+1):         #level_wind=30 (此處i=0~30)
  Uf.append(u_con[i*20])
  Vf.append(v_con[i*20])

#========================================

plt.contourf(x,y5,t_con,cmap='nipy_spectral',levels=500)   	#使用所有的顏色
plt.barbs(x,y100,Uf,Vf)
plt.title("20211214~20211220")
plt.xlabel('time (day)')
plt.ylabel('Height (m)')
plt.colorbar()						#繪製colorbar
plt.show()

