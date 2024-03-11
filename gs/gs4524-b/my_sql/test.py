import json
import matplotlib.pyplot as plt

# read the data we export to the output.txt
data_path = './data/output.txt'
with open(data_path, "r") as input_file:
    content = input_file.read().splitlines()

# extract sleep levels data
sleep_levels = []
for line in content:
    try:
        data = json.loads(line)
        sleep_levels.append(data['sleeps'][0]['sleepLevelsMap'])
    except:
        pass

# print summary
print(f"Total sleep level maps: {len(sleep_levels)}")

def main(num,):
    try:
        # select the first sleep level map
        sleep_map = sleep_levels[num]

        # extract time range
        start_time = min(
            period['startTimeInSeconds']
            for phase in sleep_map.values()
            for period in phase
        )
        end_time = max(
            period['endTimeInSeconds']
            for phase in sleep_map.values()
            for period in phase
        )
        sleep_runtime = end_time - start_time
        sleep_runtime_in_hr = sleep_runtime / 3600
        print(f"Sleep time range: {start_time} - {end_time}")
        print(f"Sleep runtime: {sleep_runtime} s ({sleep_runtime_in_hr} hr)")

        # adjust time values relative to start_time
        for phase in sleep_map.values():
            for period in phase:
                for key, value in period.items():
                    if key.endswith('TimeInSeconds'):
                        period[key] = value - start_time

        # plot the figure
        phases = ['Deep', 'Light', 'Awake', 'REM']
        fig, ax = plt.subplots()
        for i, phase in enumerate(phases):
            y = i + 1
            for period in sleep_map.get(phase.lower(), []):
                start = period['startTimeInSeconds']
                end = period['endTimeInSeconds']
                duration = end - start
                ax.barh(
                    y, duration, left=start, height=0.5,
                    align='center', alpha=0.7, label=phase
                )

        ax.set_yticks([1, 2, 3, 4])
        ax.set_yticklabels(phases)
        ax.set_xlabel('Time (s)')
        ax.set_xlim(0, end_time - start_time)
        ax.legend(loc='lower center', ncol=4, bbox_to_anchor=(0.5, -0.2))
        plt.legend().set_visible(False)
        plt.title('The cycle in one sleep.')
        file_name = './img/' + str(num) + '.png'
        # file_name = './test_img/' + str(num) + '.png'
        plt.savefig(file_name)
        plt.show()
    except:
        pass

for i in range(len(sleep_levels)):
    main(i)