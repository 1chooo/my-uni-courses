'''
@version: 1.0.0
@author: 1chooo
@date: 2023/05/07

`utils.py`
'''

def load_data(file_path) -> list:

    lines = []
    data = []

    with open(file_path, 'r') as f:

        lines = f.readlines()

    for i in range(0, len(lines), 2):

        line1 = lines[i].split()
        line2 = lines[i + 1].split()
        complete_data = line1 + line2
        data.append(complete_data)

    return lines, data



def check_merge_result(source_data, merged_data) -> None:

    source_data_len = len(source_data)
    merged_data_len = len(merged_data)

    if source_data_len / merged_data_len == 2:
        print('Merged Successful!')
    else:
        print('Merge Failed!')
        print('Lenght of source data:', source_data_len)
        print('Lenght of modified data:', merged_data_len)

def observe_merged_data(merged_data) -> None:

    print(merged_data[0])


def data_presolving(merged_data) -> list:

    data_len = len(merged_data)
    tmp = []
    result = []

    for i in range(data_len):
        month = str(merged_data[i][0][3:])
        year = str(merged_data[i][1][3:])
        day = str(merged_data[i][2][3:])
        time = str(merged_data[i][3][3:])
        wind_speed = str(merged_data[i][4][3:])
        wind_direction = str(merged_data[i][5][3:])
        temperature = str(merged_data[i][6][3:])
        humidity = str(merged_data[i][7][3:])
        pressure = str(merged_data[i][8][3:])
        radiation = str(merged_data[i][9][3:])
        rainfall = str(merged_data[i][10][3:])
        tmp.append(month)
        tmp.append(year)
        tmp.append(day)
        tmp.append(time)
        tmp.append(wind_speed)
        tmp.append(wind_direction)
        tmp.append(temperature)
        tmp.append(humidity)
        tmp.append(pressure)
        tmp.append(radiation)
        tmp.append(rainfall)

        result.append(tmp)
        tmp = []
    
    return result


def data_type_checking(merged_data) -> list:

    data_len = len(merged_data)
    tmp = []
    modified_datas = []

    for i in range(data_len):

        date_str = str(merged_data[1][3:-1]) + str(merged_data[2][5:-1])
        tmp.append(date_str)

        time_str = merged_data[3][3:-1]
        tmp.append(time_str)

        wind_speed = merged_data[4][3:]
        tmp.append(wind_speed)

        wind_direction = merged_data[5][3:]
        tmp.append(wind_direction)

        temperature = merged_data[6][3:]
        tmp.append(temperature)

        humidity = merged_data[7][3:]
        tmp.append(humidity)

        pressure = merged_data[8][3:]
        tmp.append(pressure)

        radiation = merged_data[9][3:]
        tmp.append(radiation)

        rainfall = merged_data[10][3:]
        tmp.append(rainfall)

        modified_datas.append(tmp)
        tmp = []

    return modified_datas


def check_modified_data(modified_datas) -> None:

    if len(modified_datas) == 1440 and len(modified_datas[0]) == 9:

        print('Successful')

    else:
        print(len(modified_datas))
        print(len(modified_datas[0]))
        print('Failed!')