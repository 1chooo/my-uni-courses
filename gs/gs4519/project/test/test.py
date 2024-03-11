# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/24
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

import os
import pandas as pd
from glob import glob


root = "../data"
files = glob('../data/*.csv')
print(files)


# print(data)
df_1 = pd.concat((pd.read_csv(f) for f in files))

print(df_1)
df_1.to_csv('./test.csv',encoding="utf_8_sig", index=0)

print("** Merging multiple csv files into a single pandas dataframe **")
# Merge files by joining all files
dataframe = pd.concat(map(pd.read_csv, files), ignore_index=True)
print(dataframe)

dataframe.to_csv('./test.csv',encoding="utf_8_sig", index=0)

content = open('./test.csv', 'r', encoding='UTF-8')
df = content.readlines()
content.close()

for i in range(0, len(df)):

    print((df[i]).split())
