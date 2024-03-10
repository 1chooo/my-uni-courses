""" The goal of this analysis is to predict the trend of pibal. """


""" Import the package we need. """

import csv
import math
import matplotlib.pyplot as plt


""" Initialize the variable we need. """
time, wd, elevation = 0, 0, 0
list_time, list_wd, list_elevation = [], [], []


""" Get the data what We want. """

inputFile = open("pibal_data.csv", 'r')
dataReader = csv.reader(inputFile)

for line in dataReader:

    time = line[0]
    wd = line[1]
    elevation = line[2]

    list_time.append(time)
    list_wd.append(wd)
    list_elevation.append(elevation)

inputFile.close()

del list_time[0]
del list_wd[0]
del list_elevation[0]

list_time_float, list_wd_float, list_elevation_float = [], [], []

for i in range(len(list_time)):
    time = float(list_time[i])
    list_time_float.append(time)

    wd = float(list_wd[i])
    list_wd_float.append(wd)

    elevation = float(list_elevation[i])
    list_elevation_float.append(elevation)


""" Find the counting circumstances. """

list_height = []
initial = 6.26
vector = 150.0 / 60.0

for i in list_time_float:
    height = i * vector
    height = initial + height
    list_height.append(height)

print("Height:", list_height, "\n")

list_ele_rad = []
for i in range(len(list_elevation_float)):
    angle = math.radians(list_elevation_float[i])
    angle = round(angle, 3)
    list_ele_rad.append(angle)

print("elevation in rad:", list_ele_rad, "\n")

list_wd_rad = []
angle = 0
for i in range(len(list_wd_float)):
    angle = math.radians(list_wd_float[i])
    angle = round(angle, 3)
    list_wd_rad.append(angle)

print("wind direction in rad:", list_wd_rad, "\n")

list_distance = []
d = 0
for i in range(0, 78):
    d = list_height[i] / math.tan(list_ele_rad[i])
    d = round(d, 3)
    list_distance.append(d)

print("Horizontal distance:", list_distance, "\n")


"""
Import the formula and start to analyze 
the wind direction and wind speed in high sky.
"""

list_E1E2 = []
e1e2 = 0
for i in range(1, len(list_height)):
    e1e2 = (list_distance[i] * math.sin(list_wd_rad[i])) - \
           (list_distance[i-1] * math.sin(list_wd_rad[i-1]))
    e1e2 = round(e1e2, 3)
    list_E1E2.append(e1e2)

print("E1E2:", list_E1E2, "\n")

list_N1N2 = []
n1n2 = 0
for i in range(1, len(list_height)):
    n1n2 = (list_distance[i] * math.cos(list_wd_rad[i])) - \
           (list_distance[i-1] * math.cos(list_wd_rad[i-1]))
    n1n2 = round(n1n2, 3)
    list_N1N2.append(n1n2)

print("N1N2:", list_N1N2, "\n")

alpha = 0
list_alpha = []
for i in range(len(list_E1E2)):
    alpha = math.atan(list_E1E2[i] / list_N1N2[i])
    alpha = round(alpha, 3)
    list_alpha.append(alpha)

print("alpha:", list_alpha, "\n")


""" alpha turn into degree"""

wd_list = []
for i in range(len(list_alpha)):
    a = math.degrees(list_alpha[i])
    a = a % 360
    wd_list.append(round(a, 2))

print("Wind Direction:", wd_list, "\n")


""" alpha turn into x-y axis"""

pP_qP = 0
ws_list = []
list_pP_qP = []

for i in range(len(list_E1E2)):
    pP_qP = list_E1E2[i] / math.sin(math.radians(wd_list[i]))
    list_pP_qP.append(pP_qP)
    ws = pP_qP / 30.0
    ws = abs(round(ws, 2))
    ws_list.append(ws)

print("Wind Speed:", ws_list)


""" 
After solving the data and getting the results what we want 
then we plot the data in the figure to let the results visualize.
"""

plt.figure("Pibal's Height to Horizontal Distance")
plt.plot(list_distance, list_height)
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Height (m)")
plt.legend(["Height"])
plt.title("Pibal's Height to Distance", fontweight = "bold")
plt.grid()
plt.savefig('./image/Height_to_Distance.png', dpi = 300)

# Because the interval is the total minus one.
new_height = list_height        
del new_height[77]              

plt.figure("Pibal's Height to WindDirection")
plt.plot(new_height, wd_list)
plt.ylabel("Wind Direction (degree)")
plt.xlabel("Height (m)")
plt.legend(["wd"])
plt.title("Pibal's Height to WindDirection", fontweight = "bold")
plt.grid()
plt.savefig('./image/Pibal_Height_to_WindDirection.png', dpi = 300)

plt.figure("Pibal's Height to WindSpeed")
plt.plot(ws_list, new_height)
plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Height (m)")
plt.legend(["ws"])
plt.title("Pibal's Height to WindSpeed", fontweight = "bold")
plt.grid()
plt.savefig('./image/Pibal_Height_to_WindSpeed.png', dpi = 300)
plt.show()
