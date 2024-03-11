'''

'''

import zipfile
import config

def unzip_file(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print("Unzip Successfully!!!")

# 範例使用：
zip_path = config.dataset_path
extract_path = config.extract_path

unzip_file(zip_path, extract_path)
