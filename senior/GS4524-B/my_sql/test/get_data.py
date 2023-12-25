# -*- coding: UTF-8 -*-

"""
Reference: 
https://medium.com/web-design-zone/mysql%E8%B3%87%E6%96%99%E5%BA%AB%E7%9A%84%E5%AE%89%E8%A3%9D%E8%88%87%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C-f36a079afd85
https://medium.com/web-design-zone/sql-table%E8%B3%87%E6%96%99%E8%A1%A8%E7%9A%84%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C-b7c0f830c60f
"""

import mysql.connector
from mysql.connector import Error

config = {
    'host': 'localhost',
    'database': 'database_name',
    'user': 'root',
    'password': 'pwd',
}

# 建立資料庫連線
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# 執行 SELECT 指令選取表格的 data 欄位資料
query = ("SELECT data from garmin_push_log;")

# 執行 SELECT 指令
cursor.execute(query)

# 將資料匯出成 txt 檔案
with open('./data/output.txt', 'w') as f:
    for (data,) in cursor:
        f.write(data + '\n')

# 關閉資料庫連線
cursor.close()
cnx.close()