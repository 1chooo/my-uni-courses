import requests

url = 'http://140.115.59.7:12001/flag'

try:
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        print(html_content)  # 顯示 HTML 內容
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
except requests.RequestException as e:
    print(f"Request failed: {e}")
