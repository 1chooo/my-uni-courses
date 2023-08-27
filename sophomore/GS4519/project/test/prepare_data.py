# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/24
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.2
'''

import os
import pandas as pd
from glob import glob

csv_files = glob('../data/*.csv')
csv_files.sort()  # 对文件名列表进行排序

merged_df = pd.DataFrame()  # 初始化一个空的DataFrame

for file in csv_files:
    file_name = os.path.basename(file)
    year = int(file_name.split('-')[1])  # 获取文件名中的年份信息

    if year >= 2016:  # 使用'\t'分隔的文件
        df = pd.read_csv(file, delimiter='\t')
    else:  # 使用','分隔的文件
        df = pd.read_csv(file, delimiter=',')

    merged_df = merged_df.append(df, ignore_index=True)  # 将当前数据合并到总的DataFrame中

# 将合并后的DataFrame保存为CSV文件
merged_df.to_csv('./20_years_data.csv', sep=',', index=False, encoding='utf-8-sig')

print("Merging and transforming multiple CSV files completed.")
