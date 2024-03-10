import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
pd.set_option('display.max_columns', 500)

df = pd.read_csv("C:/Users/88695/Desktop/ALEX/撈資料/定賢/test_KML/養老院資料統整.csv", encoding='big5')
address = df['地址']
name = df['名稱']
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--headless")
final = pd.DataFrame()
final2 = pd.DataFrame()
for i in range(0, len(address)):
    print("No.", (i + 2), "  ,Address = ", address[i], "  ,Name = ", name[i])
    chrome = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe', chrome_options=chrome_options)
    chrome.get("https://www.google.com.tw/maps/@23.546162,120.6402133,8z?hl=zh-TW")
    test = chrome.find_element('xpath', '//*[@id="searchboxinput"]')
    search = chrome.find_element('xpath', '//*[@id="searchbox-searchbutton"]')
    time.sleep(3)
    test.send_keys(address[i])
    search.click()
    time.sleep(3)
    str1 = chrome.current_url
    try:
        str2 = str1.split('!3d')[1]
        str3 = str2.split('!4d')
        str4 = str3[1].split('!')
        tmp = pd.DataFrame({"Address": address[i],
                            "Name": name[i],
                            "Lat": str3[0],
                            "Lon": str4[0]}, index=[0])
        final = pd.concat([final, tmp], axis=0)
    except IndexError:
        print("地址錯誤")
        print(str1)
        try:
            chrome.close()
            time.sleep(2)
            chrome = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe', chrome_options=chrome_options)
            chrome.get("https://www.google.com.tw/maps/@23.546162,120.6402133,8z?hl=zh-TW")
            test = chrome.find_element('xpath', '//*[@id="searchboxinput"]')
            search = chrome.find_element('xpath', '//*[@id="searchbox-searchbutton"]')
            time.sleep(3)
            test.send_keys(name[i])
            search.click()
            time.sleep(3)
            str1 = chrome.current_url
            str2 = str1.split('!3d')[1]
            str3 = str2.split('!4d')
            str4 = str3[1].split('!')
            tmp = pd.DataFrame({"Address": address[i],
                                "Name": name[i],
                                "Lat": str3[0],
                                "Lon": str4[0]}, index=[0])
            final = pd.concat([final, tmp], axis=0)
        except IndexError:
            print("名稱錯誤")
            print(str1)
            tmp = pd.DataFrame({"Address": address[i],
                                "Name": name[i]}, index=[0])
            final2 = pd.concat([final2, tmp], axis=0)
    chrome.close()
    time.sleep(2)
final.to_csv("nursehome_lat_lon.csv", index=False)
final2.to_csv("nursehome_error.csv", index=False)
