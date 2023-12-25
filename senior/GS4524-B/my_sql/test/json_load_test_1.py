import json
jsonFile = open('./data/garmin_push_log.json')
a = json.load(jsonFile)
data_0 = a[2]
realdata = data_0['data']
#print(realdata[0])

for i in range(0,len(realdata)):
    del realdata[i]['userid']
    del realdata[i]['record_now']
    del realdata[i]['id']