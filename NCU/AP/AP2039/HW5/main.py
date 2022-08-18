"""
This code is to analysis the atmospheric data from tower.
"""


""" Import the package. """

import csv
import math


""" Initialize and announce the variable. """

list_ws, list_ws_perTenMin, list_ws24 = [], [], []
list_wd, list_wd_perTenMin = [], []
gust_ws, gust_ws_p10 = [], []


""" Data pre-processing. """

def getMode (arr):

    mode = []
    arr_appear = dict((a, arr.count(a)) for a in arr)  # count the times of every item
    if max(arr_appear.values()) == 1:  # show one time
        return  # none
    else:
        for k, v in arr_appear.items():  # get the most showing times and the biggest
            if v == max(arr_appear.values()):
                mode.append(k)
    return mode



""" Turn the wind direction into 16 bearings. """

def diverseWindDirection (x):

    direction = []

    if x == 0:
        direction.append("Calm")
        return direction[0]
    # elif 348.749 < x < 359.999 or 0.001 < x < 11.241:
    #     direction.append("N")
    #     return direction[0]
    elif 11.249 < x < 33.741:
        direction.append(77.5)
        return direction[0]
    elif 33.749 < x < 56.241:
        direction.append(45)
        return direction[0]
    elif 56.249 < x < 78.741:
        direction.append(22.5)
        return direction[0]
    elif 78.749 < x < 101.241:
        direction.append(0)
        return direction[0]
    elif 101.249 < x < 123.741:
        direction.append(337.5)
        return direction[0]
    elif 123.749 < x < 146.241:
        direction.append(315)
        return direction[0]
    elif 146.249 < x < 168.741:
        direction.append(292.5)
        return direction[0]
    elif 168.749 < x < 191.241:
        direction.append(270)
        return direction[0]
    elif 191.249 < x < 213.741:
        direction.append(247.5)
        return direction[0]
    elif 213.749 < x < 236.241:
        direction.append(225)
        return direction[0]
    elif 236.249 < x < 258.741:
        direction.append(202.5)
        return direction[0]
    elif 258.749 < x < 281.241:
        direction.append(180)
        return direction[0]
    elif 281.249 < x < 303.741:
        direction.append(157.5)
        return direction[0]
    elif 303.749 < x < 326.241:
        direction.append(135)
        return direction[0]
    elif 326.249 < x < 348.741:
        direction.append(112.5)
        return direction[0]
    else:
        direction.append(90)
        return direction[0]


""" Rate the wind speed in Atmospheric specific level. """

def diverseBeaufortScale (x):

    beaufortScale = []

    if 0 < x < 0.2001:
        beaufortScale.append('0')
        return beaufortScale[0]
    elif 0.2999 < x < 1.5001:
        beaufortScale.append('1')
        return beaufortScale[0]
    elif 1.5999 < x < 3.3001:
        beaufortScale.append('2')
        return beaufortScale[0]
    elif 3.3339 < x < 5.4001:
        beaufortScale.append('3')
        return beaufortScale[0]
    elif 5.4999 < x < 7.9001:
        beaufortScale.append('4')
        return beaufortScale[0]
    elif 7.9999 < x < 10.7001:
        beaufortScale.append('5')
        return beaufortScale[0]
    elif 10.7999 < x < 13.8001:
        beaufortScale.append('6')
        return beaufortScale[0]
    elif 13.7999 < x < 17.1001:
        beaufortScale.append('7')
        return beaufortScale[0]
    elif 17.2001 < x < 20.7001:
        beaufortScale.append('8')
        return beaufortScale[0]
    elif 20.7999 < x < 24.4001:
        beaufortScale.append('9')
        return beaufortScale[0]
    elif 24.4999 < x < 28.4001:
        beaufortScale.append('10')
        return beaufortScale[0]
    elif 28.4999 < x < 32.6001:
        beaufortScale.append('11')
        return beaufortScale[0]
    elif 32.6999 < x < 36.9001:
        beaufortScale.append('12')
        return beaufortScale[0]
    elif 36.999 < x < 41.1001:
        beaufortScale.append('13')
        return beaufortScale[0]
    elif 41.4999 < x < 46.1001:
        beaufortScale.append('14')
        return beaufortScale[0]
    elif 46.1999 < x < 50.9001:
        beaufortScale.append('15')
        return beaufortScale[0]
    elif 50.9999 < x < 56.0001:
        beaufortScale.append('16')
        return beaufortScale[0]
    elif 56.0999 < x < 61.2001:
        beaufortScale.append('17')
        return beaufortScale[0]


""" Read the file and get the data we want to analyze. """

inputFile1 = open("10M_tower_data1.csv", 'r')
dataReader1 = csv.reader(inputFile1)

for line1 in dataReader1:

    if line1[1] == '9' and line1[2] == '8':
        # line1[4] = int(line1[4])
        list_ws24.append(float(line1[7]))

        if int(line1[4]) >= 50:
            list_ws.append(float(line1[7]))
            list_wd.append(float(line1[8]))


inputFile1.close()


""" 
Find ten minutes before every hours 
and diverse to sixteen bearings.
To get average wind direction.   
"""


num, situate = 0, 0
list_wd_avg, mode, list_mode, list_count, list_new = [], [], [], [], []


""" Show wind direction average. """

for i in range(0, len(list_wd), 10):
    list_wd16 = []
    list_wd_perTenMin = list_wd[i: (i + 10)]
    list_ws_perTenMin = list_ws[i: (i + 10)]
    num += 1
    # print(num)
    # print(list_wd_perTenMin)
    # print(list_ws_perTenMin)

    for j in list_wd_perTenMin:
        list_wd16.append(diverseWindDirection(j))

    for k in range(0, len(list_wd16), 10):
        list_wd16 = list_wd16[k: (k + 10)]
        # print(list_wd16)        # 16 bearings
        mode = getMode(list_wd16)
        if len(mode) == 1:
            list_mode.append(mode[0])
        else:
            list_count = []
            for l in range(0, len(mode)):
                for m in range(10):
                    if list_wd16[m] == mode[l]:
                        list_count.append(m)

            # print(list_count)

            for n in list_count:
                list_new.append(list_ws_perTenMin[n])

            situate = list_count[list_new.index(max(list_new))]
            list_mode.append(list_wd16[situate])
            list_new = []

        list_count = []

hour = 0

for i in range(len(list_mode)):
    hour += 1

    print("Hour:", hour, "\tWind Direction average:", list_mode[i])

print("")


""" Find average wind speed. """

hour = 0
list_ws_avg = []


for i in range(0, len(list_ws), 10):
    list_ws_perTenMin = list_ws[i: (i+10)]
    # print(list_ws_perTenMin)
    ws = 0

    for j in range(len(list_ws_perTenMin)):
        ws += list_ws_perTenMin[j]

    ws_avg = round((ws/10), 1)
    list_ws_avg.append(ws_avg)
    hour += 1
    print("Hour:", hour, "\tWind Speed Average:", ws_avg)

print("")


""" Diverse to beaufort scale """


hour = 0
for i in list_ws_avg:
    hour += 1
    print("Hour:", hour, "\tBeaufort Scale:", diverseBeaufortScale(i))

print("")


""" Find u and v wind. """


angle = []
u, v, hour = 0, 0, 0

for i in range(0, 24):
    angle = math.radians(list_mode[i])
    u = (abs(round(list_ws_avg[i] * math.cos(angle), 1)))
    v = (abs(round(list_ws_avg[i] * math.sin(angle), 1)))
    hour += 1

    print( "hour:", hour, "\tu_wind:",  u, "\t,", "v_wind:", v)

print("")


""" Find the gust. """


time = 0

for i in range(0, len(list_ws24), 10):
    list_ws24_p10 = list_ws24[i: (i+10)]
    # print(list_ws24_p10)
    ws_p10_max = max(list_ws24_p10)
    gap = 0
    ws_p10 = 0

    for j in range(0, len(list_ws24_p10)):
        ws_p10 += list_ws24_p10[j]

    ws_p10_avg = ws_p10/10
    gap = ws_p10_max - ws_p10_avg
    time += 1
    if gap > 5:
        gust_ws.append(ws_p10_max)
    else:
        gust_ws.append("NaN")

hour = 0

for i in range(0, len(gust_ws), 6):
    gust_ws_p10 = gust_ws[i: (i+6)]
    count = 0
    hour += 1
    for j in range(len(gust_ws_p10)):
        if gust_ws_p10[j] == "NaN":
            count += 1
            if count == 6:
                print("Hour:", hour, "\tgust_ws:", "NaN")
        else:
            print("Hour:", hour, "gust_ws:", gust_ws_p10[j])
