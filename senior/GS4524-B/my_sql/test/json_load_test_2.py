import json

file_path = './data/garmin_push_log.txt'
input_file = open(file_path, 'r')

content = []

for line in input_file.readlines():
    content.append(line)

input_file.close()

temp = []

print(content[5])
