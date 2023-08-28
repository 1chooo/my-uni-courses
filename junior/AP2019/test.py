import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pd.set_option('display.max_columns', 500)

df = pd.read_csv("./data/A17000000J-020028-cAw.csv", encoding='utf-8')
address = df['地址']
name = df['醫院名稱']
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--headless")
chrome = webdriver.Chrome('./chromedriver_mac64/chromedriver', options=chrome_options)
wait = WebDriverWait(chrome, 10)
final = pd.DataFrame()
final2 = pd.DataFrame()

def get_lat_lon(address, name):
    chrome.get("https://www.google.com.tw/maps")
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchboxinput"]')))
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchbox-searchbutton"]')))
    search_box.clear()
    search_box.send_keys(address)
    search_button.click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".widget-pane-link")))

    current_url = chrome.current_url
    try:
        lat = current_url.split('!3d')[1].split('!4d')[0]
        lon = current_url.split('!4d')[1].split('!')[0]
        return lat, lon
    except IndexError:
        print("地址錯誤")
        print(current_url)
        chrome.get("https://www.google.com.tw/maps")
        search_box.clear()
        search_box.send_keys(name)
        search_button.click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".widget-pane-link")))

        current_url = chrome.current_url
        try:
            lat = current_url.split('!3d')[1].split('!4d')[0]
            lon = current_url.split('!4d')[1].split('!')[0]
            return lat, lon
        except IndexError:
            print("名稱錯誤")
            print(current_url)
            return None, None

for i in range(len(address)):
    print("No.", (i + 2), ", Address =", address[i], ", Name =", name[i])
    lat, lon = get_lat_lon(address[i], name[i])

    if lat is not None and lon is not None:
        tmp = pd.DataFrame({"Address": address[i], "Name": name[i], "Lat": lat, "Lon": lon}, index=[0])
        final = pd.concat([final, tmp], axis=0)
    else:
        tmp = pd.DataFrame({"Address": address[i], "Name": name[i]}, index=[0])
        final2 = pd.concat([final2, tmp], axis=0)

final.to_csv("./data/nursehome_lat_lon.csv", index=False)
final2.to_csv("./data/nursehome_error.csv", index=False)

chrome.quit()
