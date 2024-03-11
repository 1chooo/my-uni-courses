import json

with open("data/test.txt", "r") as file:
    content = file.read().splitlines()

result = []

for i in range(0,len(content)):
    try:
        data = json.loads(content[i])
        avg_heart_rate = data.get("dailies")[0].get("averageHeartRateInBeatsPerMinute")
        result.append(avg_heart_rate)
    except:
        continue

print(result)