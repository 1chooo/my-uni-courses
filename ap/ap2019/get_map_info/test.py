import requests
from bs4 import BeautifulSoup

def get_coordinates(address):
    # 將地址轉換為 URL 格式
    formatted_address = address.replace(' ', '+')
    url = f'https://www.google.com/maps/search/{formatted_address}'
    
    # 發送 GET 請求取得網頁內容
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    try:
        # 找到經緯度元素並獲取內容
        element = soup.select_one('.ugiz4pqJLAG__primary-text')
        coordinates = element.get_text(strip=True).split(',')
        
        if len(coordinates) == 2:
            latitude = coordinates[0].strip()
            longitude = coordinates[1].strip()
            return latitude, longitude
        else:
            return None
    except:
        return None

# 測試範例
address = '基隆市信義區信二路268號'
coordinates = get_coordinates(address)
if coordinates:
    latitude, longitude = coordinates
    print(f'經度：{longitude}, 緯度：{latitude}')
else:
    print('無法獲取該地點的經緯度資訊')
