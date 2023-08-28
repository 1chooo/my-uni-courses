'''

'''


import requests
import config

def download_file(url, save_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)
    print("Download Successfully!!!")

url = config.dataset_url
save_path = config.save_path

download_file(url, save_path)
