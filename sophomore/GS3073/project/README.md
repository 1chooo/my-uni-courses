# BearBear You

[![project badge](https://img.shields.io/badge/1chooo-bear__bear-informational)](https://github.com/1chooo/bear-bear)
[![Made with Python](https://img.shields.io/badge/Python=3.10-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")
[![License](https://img.shields.io/badge/License-MIT-blue)](./LICENSE "Go to license section")

A brief summary of the project
---
Develop a Line BOT utilizing S3 and Amazon Recognition services to enhance familiarity with NCU Campus.

| [BearBear You](https://lin.ee/Ju3NM0m) |LINE QRCODE |
|:-:|:-:|
| <img src="images/profile.png" width="300">| <img src="images/L_gainfriends_2dbarcodes_BW.png" width="300"> |

Enviroment: 
---

### With pip vertial environment
- python request: `3.10`
- Required package: `numpy flask line-bot-sdk face_recognition pandas boto3`
#### For **Linux/MacOS**
```shell
$ pip3 install virtualenv
$ virtualenv venv --python=python3.10
$ source venv/bin/activate
$ pip install -r requirements.txt
$ deactivate
$ rm -rf venv     # remove the venv
```

#### For **Windows**
```shell
$ pip install virtualenv
$ virtualenv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ deactivate
$ rmdir /s venv     # remove the venv
```

### Add LINE BOT Developer Config

You should duplicate the file `config_example.py` and rename into `config.py`

```py
# line bot info
line_bot_api = 'your_line_bot_api'
handler = 'your_handler'

# AWS info
client_aws_access_key_id = "your_client_aws_access_key_id"
client_aws_secret_access_key = "your_client_aws_secret_access_key"
client_aws_session_token="your_client_aws_session_token"

# Model in AWS
model_arn="your_model_arn"

# AWS bucket info
client_bucket_name="your_client_bucket_name"
client_region_name="your_client_region_name"
```


### With ngrok free server
```SHELL
$ brew install ngrok --cask
$ ngrok config add-authtoken YOUR_TOKEN
$ python run.py
$ ngrok http 5002
```

### Start multiple tunnel

```shell
$ ngrok config check
Valid configuration file at YOUR_PATH/ngrok/ngrok.yml
```

Add the below code in `YOUR_PATH/ngrok/ngrok.yml`

```yml
version: "2"
authtoken: "YOUR_TOKEN"
# Please avoid making any changes to the content provided below
tunnels:
  first:
    addr: 5002
    proto: http    
  second:
    addr: 5012
    proto: http
```

type `ngrok start --all` in terminal to start `ngrok`

```shell
$ mkdocs build
$ mkdocs serve
```
Workflow permissions
- [x] Read and Write Permissions

Project Structure
---
```
PROJECT_ROOT
├── test/
│   ├── test_main.py/
│   ├──   :
│   └──   :
├── Bear/
│   ├── Drama.py
│   ├── Utils.py
│   └──   :
├── log/
│   ├── date/
│   └──   :
├── app.py
├── config.py
├── LICENSE
└── README.md
```

License
---
Released under [MIT](./LICENSE) by [@1chooo](https://github.com/1chooo)

This software can be modified and reused without restriction.
The original license must be included with any copies of this software.
If a significant portion of the source code is used, please provide a link back to this repository.