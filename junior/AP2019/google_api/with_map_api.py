import pandas as pd
import time
import requests

pd.set_option('display.max_columns', 500)

df = pd.read_csv("./data/A17000000J-020028-cAw.csv", encoding='utf-8')
address = df['地址']
name = df['醫院名稱']
final = pd.DataFrame()
final2 = pd.DataFrame()

def get_lat_lon(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": "YOUR_GOOGLE_MAPS_API_KEY"
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data["status"] == "OK":
        location = data["results"][0]["geometry"]["location"]
        return location["lat"], location["lng"]
    else:
        return None, None

for i in range(len(address)):
    print("No.", (i + 2), ", Address =", address[i], ", Name =", name[i])
    lat, lon = get_lat_lon(address[i])

    if lat is not None and lon is not None:
        tmp = pd.DataFrame({"Address": address[i], "Name": name[i], "Lat": lat, "Lon": lon}, index=[0])
        final = pd.concat([final, tmp], axis=0)
    else:
        print("地址錯誤")
        tmp = pd.DataFrame({"Address": address[i], "Name": name[i]}, index=[0])
        final2 = pd.concat([final2, tmp], axis=0)

    time.sleep(1)

final.to_csv("./data/nursehome_lat_lon.csv", index=False)
final2.to_csv("./data/nursehome_error.csv", index=False)
