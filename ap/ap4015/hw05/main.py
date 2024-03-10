'''
@version: 1.0.0
@author: 1chooo
@date: 2023/05/01

`main.py`
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

def data_presolving(merged_data) -> list:
    result = []

    for data in merged_data:
        tmp = [
            str(data[0])[3:],  # month
            str(data[1])[3:],  # year
            str(data[2])[3:],  # day
            str(data[3])[3:],  # time
            str(data[4])[3:],  # wind_speed
            str(data[5])[3:],  # wind_direction
            str(data[6])[3:],  # temperature
            str(data[7])[3:],  # humidity
            str(data[8])[3:],  # pressure
            str(data[9])[3:],  # radiation
            str(data[10])[3:]  # rainfall
        ]

        result.append(tmp)
    
    return result


def main():

    file_paths = [
        './ncu10m/160119.obs', './ncu10m/160120.obs',
        './ncu10m/160121.obs', './ncu10m/160122.obs',
        './ncu10m/160123.obs', './ncu10m/160124.obs',
        './ncu10m/160125.obs',
    ]
    modified_data = []

    for file_path in file_paths:
        lines, data = load_data(file_path)
        modified_data.extend(data_presolving(data))

    with open('1601.obs', 'w') as file:
        for i in range(len(modified_data)):
            output_str = ' '.join(modified_data[i])

            if (i != len(modified_data) - 1):
                file.write(output_str + ' \n')
            else:
                file.write(output_str + ' ')

if __name__ == '__main__':
    main()