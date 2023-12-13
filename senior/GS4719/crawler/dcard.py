import requests as rq

url='https://www.dcard.tw/service/api/v2/forums/stock/posts?limit=30&before=999999999'
posts = rq.get(url)

# 列出收到的 Response 文字內容
print(posts.text)

# 為了避免被DCard視為爬蟲，加上瀏覽器的header
url='https://www.dcard.tw/service/api/v2/forums/stock/posts?limit=30&before=999999999'
posts = rq.get(
    url, headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
    }
)

# 將文字內容轉成JSON物件
jsonobj = posts.json()
print(type(jsonobj))

# 列出所有文章標題
for post in jsonobj:
    print(post.get('title'))

# 列出所有文章編號
for post in jsonobj:
    print(post.get('id'))

# 列出最後一篇文章的編號
print(jsonobj[-1].get('id'))
