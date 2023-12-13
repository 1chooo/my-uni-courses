# Web Crawler

## 讀取 Dcard 股票版的前 30 篇文章

```python
import requests as rq
```

```python
url='https://www.dcard.tw/service/api/v2/forums/stock/posts?limit=30&before=999999999'
posts = rq.get(url)
```

**列出收到的 Response 文字內容**

```python
print(posts.text)
```

**為了避免被 DCard 視為爬蟲，加上瀏覽器的 header**

```python
url='https://www.dcard.tw/service/api/v2/forums/stock/posts?limit=30&before=999999999'
posts = rq.get(
    url, headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
    }
)
```

**將文字內容轉成 `JSON` 物件**

```python
jsonobj = posts.json()
print(type(jsonobj))
```

**列出所有文章標題**

```python
for post in jsonobj:
    print(post.get('title'))
```

**列出所有文章編號**

```python
for post in jsonobj:
    print(post.get('id'))
```

**列出最後一篇文章的編號**

```python
print(jsonobj[-1].get('id'))
```

## 抓取 Dcard 上面股票版的 100 篇文章

```python
import time, random
import requests as rq

i=0
total=100
id=999999999
discussion=[]

while i<total:
    post_number = total-i if (total-i)<30 else 30
    url = f'https://www.dcard.tw/service/api/v2/forums/stock/posts?limit={post_number}&before={id}'
    try:
        post_data = rq.get(
            url, 
            headers={
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
            }
        ).json()
        discussion.extend(post_data)
        id = post_data[-1].get('id')
        i+=post_number
        time.sleep(random.randint(1,3))
    except:
        print('error!', end='')
        time.sleep(random.randint(1,3))
```

## 讀取 Github 討論區的前 10 篇文章

```python
import requests

query_string = '''
{
    viewer {
        login
    }
    repository(name: "Python-Community", owner: "NCU-GS4719-Python") {
        discussions(first: 10) {
            edges {
                node {
                    id
                    title
                }
            }
        }
    }
}
'''

api_url = "https://api.github.com/graphql"
github_personal_access_token = ""
response = requests.post(
    api_url, 
    headers={
        "Authorization": f"bearer {github_personal_access_token}"
    }, 
    json={
        'query': query_string
    }
)
print(response.text)

for _ in response.json()['data']['repository']['discussions']['edges']:
    print(_['node']['title'])
```
