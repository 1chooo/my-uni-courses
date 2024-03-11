import requests
import json

url_submit = "http://140.115.59.7:12004/api/submit"
url_score = "http://140.115.59.7:12004/api/score"

headers_submit = {
    "Host": "140.115.59.7:12004",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Origin": "http://140.115.59.7:12004",
    "Referer": "http://140.115.59.7:12004/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,ja;q=0.6,zh-CN;q=0.5,yo;q=0.4",
    "Cookie": "session=.eJwNwoENwCAIBMBdmADwK9ptQCFxhqa7t5d7KM-mm3Kx9ynCnWcJ70LTMkCikv-o2Fzm5sBlrTQjdDUfS8eYMHo_BF4Ulg.ZZEk1A.x2q5KgJIfuXayc_2fHhFBBTQqxY",
    "Connection": "close"
}

headers_score = {
    "Host": "140.115.59.7:12004",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Referer": "http://140.115.59.7:12004/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,ja;q=0.6,zh-CN;q=0.5,yo;q=0.4",
    "Cookie": "session=.eJwNwoENwCAIBMBdmADwK9ptQCFxhqa7t5d7KM-mm3Kx9ynCnWcJ70LTMkCikv-o2Fzm5sBlrTQjdDUfS8eYMHo_BF4Ulg.ZZEk1A.x2q5KgJIfuXayc_2fHhFBBTQqxY",
    "Connection": "close"
}

data = [ [None for i in range(10)] for _ in range(10)]

for i in range(10):
    for j in range(10):
        for ans in range(4):
            data[i][j] = ans
            requests.post(url_submit, headers=headers_submit, data=json.dumps(data))
            response = requests.get(url_score, headers=headers_score)
            if i*10 + j+1 == response.json()["data"]["score"]:
                print(f"ans: {ans}")
                break
            
print(data)
