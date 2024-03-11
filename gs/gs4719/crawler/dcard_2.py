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
