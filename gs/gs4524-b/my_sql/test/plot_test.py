# -*- coding: UTF-8 -*-

import json
import matplotlib.pyplot as plt

# read the data we export to the output.txt
data_path = './data/output.txt'
with open(data_path, "r") as input_file:
    content = input_file.read().splitlines()

# capture the data concerining sleep.
result = []

for i in range(0, len(content)):

    try:
        data = json.loads(content[i])
        sleep_map = data.get('sleeps')[0].get('sleepLevelsMap')
        result.append(sleep_map)
    except:
        continue

# print(result)
print("Total map we have gotten:", str(len(result)))

"""
"""

# first, we test the specific index 
# we want to visualize.
number = 0
# print(result[number])

"""_comment_
@1chooo
I would recommend reworking the following 
code as it contains three nested for-loops 
that could potentially impact its efficiency. 
Additionally, it appears that we have only 
printed the first data figure obtained.
"""

# find the minimum of the TimeInSeconds
min_time = float('inf')
for phase in result[number].values():
    for period in phase:
        for key, value in period.items():
            if key.endswith('TimeInSeconds'):
                min_time = min(min_time, value)

# find the maximum of the TimeInSeconds
max_time = float('-inf')
for phase in result[number].values():
    for period in phase:
        for key, value in period.items():
            if key.endswith('TimeInSeconds'):
                max_time = max(max_time, value)

""" Show the result of sleep time. """
sleep_runtime = max_time - min_time
sleep_runtime_in_hr = sleep_runtime / 3_600

print("The minimum of the time:", str(min_time))
print("The minimum of the time:", str(max_time))
print("The runtime of the sleep time:", sleep_runtime, "(s) =", sleep_runtime_in_hr, "(hr)")


# let every TimeInSeconds - min_time
# to get the time era.
for phase in result[number].values():
    for period in phase:
        for key, value in period.items():
            if key.endswith('TimeInSeconds'):
                period[key] = value - min_time

# print(result[number])

#--------------------------------------------------------#

# get the interval of the time.
times = []

for phase in result[number].values():
    for period in phase:
        times.append(period['startTimeInSeconds'])
        times.append(period['endTimeInSeconds'])
times.sort()

start_time = times[0]
end_time = times[-1]


"""_comment_
@1chooo
there is no present of the REM.
"""
# plot the figure.
fig, ax = plt.subplots()
phases = ['Deep', 'Light', 'Awake', 'REM']

for i, phase in enumerate(phases):

    y = i + 1

    for period in result[number].get(phase.lower(), []):
        start = period['startTimeInSeconds']
        end = period['endTimeInSeconds']
        duration = end - start
        ax.barh(y, duration, left=start, height=0.5, align='center', alpha=0.7, label=phase)

ax.set_yticks([1, 2, 3, 4])
ax.set_yticklabels(phases)
ax.set_xlabel('Time (s)')
ax.set_xlim(0, end_time - start_time)
ax.legend(loc='lower center', ncol=4, bbox_to_anchor=(0.5, -0.2))
plt.legend().set_visible(False)
plt.title('The cycle in one sleep.')

plt.show()