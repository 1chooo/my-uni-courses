#===========套件===========
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#==========讀資料==========
df=pd.read_csv('./202101_upair.txt',sep='\s+',header=11)   #讀資料,
df=df[1:]
df['yyyymmddhh']=df['yyyymmddhh'].astype('int').astype('str')   #換為整數再換為字串
#print(df['yyyymmddhh'])

#設定條件，只讀取單一測站單一時間的資料。
filt=(df['stno']=='466920')&(df['yyyymmddhh']=='2021010100')
#取出列名相對應的資料。
p1=df.loc[filt,'Press']
t1=df.loc[filt,'Tx']    
h1=df.loc[filt,'Heigh']

filt=(df['stno']=='466920')&(df['yyyymmddhh']=='2021010200')  
p2=df.loc[filt,'Press']
t2=df.loc[filt,'Tx']
h2=df.loc[filt,'Heigh']


#==========繪圖==========
plt.figure(figsize=(6,8))       #繪圖區域長寬比、解析度
plt.plot(t1,p1,'r.-',label="2021010100")	#繪製函數圖
plt.plot(t2,p2,'b-',label="2021010200")


plt.gca().invert_yaxis()                #將y軸反轉，壓力從(0~1000)變成(1000~0)
plt.xlabel('$Temperature\ (^\circ C)$',fontsize=15)	#X軸名稱
plt.ylabel('$Pressure\ (hPa)$',fontsize=15)		#Y軸名稱
plt.title("Title",fontsize=25)		
plt.legend(loc='upper right', fontsize=15)
#plt.grid()   				#設置網格線
plt.show()