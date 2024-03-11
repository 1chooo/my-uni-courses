import json
import matplotlib.pyplot as plt
import mysql.connector
from mysql.connector import Error
import app_config as ac

def get_data_from_sql(garmin_data, config,) -> None:
    
    cnx = mysql.connector.connect(**config)     # connect to the mySQL
    cursor = cnx.cursor()

    query = ("SELECT data from garmin_push_log;")
    cursor.execute(query)
    
    garmin_data = [data for data, in cursor]

    cursor.close()
    cnx.close()

    return garmin_data

def get_data_without_try(sleep_levels, garmin_data) -> list:

    sleep_levels = []

    for line in garmin_data:
        data = json.loads(line)
        if (data.get('sleeps')[0].get('sleepLevelsMap')) != None:
            sleep_levels.append(data.get('sleeps')[0].get('sleepLevelsMap'))
    
    return sleep_levels

def get_data_with_try(sleep_levels, garmin_data) -> list:

    sleep_levels = []

    for line in garmin_data:
        data = json.loads(line)
        """ 
            The original format.
            try:
                data = json.loads(line)
                sleep_levels.append(data['sleeps'][0]['sleepLevelsMap'])
            How to rewrote without try, except?
            if (sleep_level != None):
                sleep_levels.append(sleep_level)
        """
        try:
            sleep_level = data['sleeps'][0]['sleepLevelsMap']
            sleep_levels.append(sleep_level)
        except:
            pass
    
    return sleep_levels

def show_sleep_level_maps(sleep_levels) -> None:

    print(f"Total sleep level maps we can use: {len(sleep_levels)}")

def get_sleep_map(num) -> list:

    sleep_map = sleep_levels[num]

    return sleep_map

def get_sleep_range(sleep_map) -> float:

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
    
    return start_time, end_time

def show_sleep_runtime(start_time, end_time, sleep_runtime,) -> None:

    sleep_runtime_in_hr = sleep_runtime / 3600
    print(f"Sleep time range: {start_time} - {end_time}")
    print(f"Sleep runtime: {sleep_runtime} s ({sleep_runtime_in_hr} hr)")


def main(num,):
    try:
        # select the first sleep level map

        sleep_map = get_sleep_map(num)
        start_time, end_time = get_sleep_range(sleep_map)
        sleep_runtime = end_time - start_time
        show_sleep_runtime(start_time, end_time, sleep_runtime,)

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
        plt.title(f'The cycle in one sleep.({num})')
        file_name = './img/' + str(num) + '.png'
        # file_name = './test_img/' + str(num) + '.png'
        plt.savefig(file_name)
        plt.show()
    except:
        pass


sleep_levels = []
garmin_data = []
garmin_data = get_data_from_sql(garmin_data, ac.config)
sleep_levels = get_data_with_try(sleep_levels, garmin_data)
print(len(sleep_levels))
show_sleep_level_maps(sleep_levels)

for i in range(len(sleep_levels)):
    main(i)