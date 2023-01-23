import csv
import requests
import pandas as pd

CSV_URL = 'https://agr.cwb.gov.tw/NAGR/history/station_day/create_report?station=K2E360&start_time=2017-01-01&end_time=2021-12-31&items=TxMaxAbs&report_type=csv&level=新農業站'

with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8', "ignore")

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)

    i = 1
    year = 2017
    df = []
    print("K2E360 2017-01-01 to 2021-12-31 TxMaxAbs\n")
    for row in my_list:
        jump = [1, 2, 36, 37, 38, 72, 73, 74, 108, 109, 110, 144, 145, 146, 180]
        
        if i not in jump :
            df.append(row)
            # print(row)
            # df.append(row)
        if (i % 36 == 2) :
            row.clear()
            row.append(str(year))
            df.append(row)
            # print(row)
            year += 1
        i += 1
    
    for i in df :
        print(i)