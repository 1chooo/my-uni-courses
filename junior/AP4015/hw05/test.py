'''
@version: 1.0.0
@author: 1chooo
@date: 2023/05/07

`test.py`
'''

file_path = './ncu10m/160124.obs'


with open(file_path, "r") as f:
    lines = f.readlines()

# for i in range(2880):
#     print(lines[i])

# print(lines[0].split())
# print(lines[1].split())

# print(len(lines))
# for i in range(len(lines)):

#     print(lines[i])

datas = []

tmp = []

for i in range(2880):

    if i % 2 == 0:

        for j in range(len(lines[i])):
            tmp.append(lines[j])
        # tmp.append(lines[i].split())
    else:
        for j in range(len(lines[i])):
            tmp.append(lines[j])
        # print(tmp)

        # datas.append(tmp)
        tmp = []

for i in range(len(datas)):
    print(datas[i])

# print(datas[0][0][0])


test0 = lines[0].split()
test1 = lines[1].split()

print(test0[2][5:-1])

date_str = test0[1][3:-1] + test0[2][5:-1]
print(date_str)

time_str = test0[3][3:-1]
print(time_str)

wind_speed = test0[4][3:]
print(wind_speed)

wind_direction = test0[5][3:]
print(wind_direction)

temperature = test0[6][3:]
print(temperature)

humidity = test0[7][3:]
print(humidity)

pressure = test1[0][3:]
print(pressure)

radiation = test1[1][3:]
print(radiation)


rainfall = test1[2][3:]
print(rainfall)


# Loop through each line of the file
for i, line in enumerate(lines):
    if i % 2 == 0:  # Only read every other line
        data = line.strip().split()
        date_str = data[1] + data[2]  # Combine year and day to get date string
        time_str = data[3]
        wind_speed = float(data[4][:2])
        wind_direction = float(data[5][:2])
        temperature = float(data[6][:2])
        humidity = float(data[7][:2])
        pressure = float(data[8])
        radiation = float(data[9])
        rainfall = float(data[10])

        # Do something with the data


print(date_str)