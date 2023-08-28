import time
import requests
from selenium import webdriver

def get_coordinates(address):
    url = f'https://www.google.com/maps/search/{address}'
    
    # 使用Selenium開啟瀏覽器
    driver = webdriver.Chrome('./chromedriver_mac64/chromedriver')
    
    # 等待網頁加載完成
    time.sleep(5)
    
    # 打開指定的網址
    driver.get(url)
    
    # 等待網頁加載完成
    time.sleep(5)
    
    try:
        # 找到經緯度元素並獲取內容
        element = driver.find_element_by_css_selector('.ugiz4pqJLAG__primary-text')
        coordinates = element.text.split(',')
        
        if len(coordinates) == 2:
            latitude = coordinates[0].strip()
            longitude = coordinates[1].strip()
            return latitude, longitude
        else:
            return None
    except:
        return None
    finally:
        # 關閉瀏覽器
        driver.quit()

# 測試範例
address = '基隆市信義區信二路268號'
coordinates = get_coordinates(address)
if coordinates:
    latitude, longitude = coordinates
    print(f'經度：{longitude}, 緯度：{latitude}')
else:
    print('無法獲取該地點的經緯度資訊')
