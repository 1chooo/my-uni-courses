import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#% matplotlib inline

''''''
import os
import glob

# # path = "data1"
# # path_domestic = os.path.abspath(os.getcwd()) + '/data1'
# # data = glob.glob(os.path.join(path_domestic, "*.csv"))

# # df=pd.concat((pd.read_csv(f) for f in data))
# # df

df = pd.read_csv("./1_f.csv")

# df.info()
# df.head()
# df.describe().T

# df.drop(['ObsTime','SeaPres','StnPresMaxTime','StnPresMinTime'],axis=1, inplace=True)
# df.drop(['T Max Time','T Min Time','Td dew point'], axis=1, inplace=True)
# df.drop(['RHMinTime','WGustTime'], axis=1, inplace=True)
# df.drop(['PrecpHour','PrecpMax10','PrecpMax10Time','PrecpMax60','PrecpMax60Time'], axis=1, inplace=True)
# df.drop(['SunShine','SunShineRate','GloblRad','VisbMean'], axis=1, inplace=True)
# df.drop(['EvapA','UVI Max','UVI Max Time','Cloud Amount'], axis=1, inplace=True) 
# df


# df = df.replace('...','-999')
# df = df.replace('/','-999')


# for i in range(0, 854):
#     for j in range(0,13):
#         if df.iloc[i,j] == '-999':
#             df.iloc[i,j] = 0.0

# df=pd.DataFrame(df,dtype=np.float)

# def countAverage(df,x,l):
#     count = 1
#     jump = 1
#     total = 0
#     ans = 0

#     for i in range(1, l):
#         if (df.iloc[x,i] == 0.0):
#             jump += 1
#         else:
#             temp = float(df.iloc[x,i])
#             count += 1
#             total += temp
#     ans = total / count
#     print(ans)
#     return

# countAverage(df,854,5)

# df=pd.DataFrame(df,dtype=np.float)


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# #% matplotlib inline

# ''''''
# import os
# import glob

# path = "data1"
# path_domestic = os.path.abspath(os.getcwd()) + '/data1'
# data = glob.glob(os.path.join(path_domestic, "*.csv"))

# df=pd.concat((pd.read_csv(f) for f in data))

df.info()
df.head()
df.describe().T

# Here we delete the data we don't need.
df.drop(['ObsTime','SeaPres','StnPresMaxTime','StnPresMinTime'],axis=1, inplace=True)
df.drop(['T Max Time','T Min Time','Td dew point'], axis=1, inplace=True)
df.drop(['RHMinTime','WGustTime'], axis=1, inplace=True)
df.drop(['PrecpHour','PrecpMax10','PrecpMax10Time','PrecpMax60','PrecpMax60Time'], axis=1, inplace=True)
df.drop(['SunShine','SunShineRate','GloblRad','VisbMean'], axis=1, inplace=True)
df.drop(['EvapA','UVI Max','UVI Max Time','Cloud Amount'], axis=1, inplace=True) 
df

# Then here we make the loss data into the value we can distinguish. 
df = df.replace('...','-999')
df = df.replace('/','-999')


for i in range(854):
    for j in range(0,13):
        if df.iloc[i,j] == '-999':
            df.iloc[i,j] = 0.0

df=pd.DataFrame(df,dtype=np.float)

def countAverage(df, row, column):
    count = 0
    jump = 1
    total = 0
    ans = 0

    for i in range(1, column):
        if (df.iloc[row,i] == 0):
            jump += 1
        else:
            temp = float(df.iloc[row,i])
            count += 1
            total += temp
    
    ans = total / count
    print(ans)
    print(jump)

    return


def countAverage(df,row,column):
    count = 0
    jump = 1
    total = 0
    ans = 0

    for k in range(0, row):
        if (df.iloc[k, column] == 0.0):
           jump += 1
        else:
           temp = float(df.iloc[k, column])
           count += 1
           total += temp
    ans = total / count
    print(ans)
    print(count)
    return
    
countAverage(df,853,0)

df['StnPres'].value_counts()
df["StnPres"].median()

countAverage(df, 853, 2)