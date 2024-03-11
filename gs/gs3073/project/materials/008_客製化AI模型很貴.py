# %% [markdown]
# 東勝神州，石頭立於山尖，受日蒸月晾，雨蝕風刻，苦不堪言，只見形體一傾，繃出隻石猴心猿
# 
# 猿心造次，只好西行一遭，道是修心，不使心搖意動。
# 
# 每每讀至此，便傷感難耐，人間之味出於情，若不動情則無味。
# 
# 就來做個有情機器人吧，但願這個機器人有了情之後，開始老去。
# 
# 在老去的過程中，體驗清歡滋味。

# %%
!which python
!python --version

# %%
'''
安裝套件
'''
!pip install line-bot-sdk flask flask-ngrok boto3

# %%
'''
引用機器人套件
'''

# 引用Web Server套件
from flask import Flask, request, abort, jsonify

# 載入json處理套件
import json

# 外部連結自動生成套件
from flask_ngrok import run_with_ngrok

# 從linebot 套件包裡引用 LineBotApi 與 WebhookHandler 類別
from linebot import (
    LineBotApi, WebhookHandler
)

# 引用無效簽章錯誤
from linebot.exceptions import (
    InvalidSignatureError
)


# %%
'''

建置主程序

建置handler與 line_bot_api

'''

import config

# 生成實體物件
line_bot_api = LineBotApi(config.line_bot_api)
handler = WebhookHandler(config.handler)

# AWS要知道大家是誰，需要類似身份帳號密碼的亂數
client_aws_access_key_id = config.client_aws_access_key_id
client_aws_secret_access_key = config.client_aws_secret_access_key
client_aws_session_token = config.client_aws_session_token

# 模型在AWS的位置
model_arn = config.model_arn

# 存放消費者上傳照片的桶子名
client_bucket_name = config.client_bucket_name
client_region_name = config.client_region_name

# 載入劇本Excel
import pandas as pd
plot_content = pd.read_excel("bearbear.xlsx")

# %%
# 引用會用到的套件
from linebot.models import (
    ImagemapSendMessage,TextSendMessage,ImageSendMessage,LocationSendMessage,FlexSendMessage,VideoSendMessage,StickerSendMessage,AudioSendMessage
)

from linebot.models.template import (
    ButtonsTemplate,CarouselTemplate,ConfirmTemplate,ImageCarouselTemplate
    
)

from linebot.models.template import *

import json

def detect_json_array_to_new_message_array(jsonObjectArray):
    

    # jsonObject = json.loads(jsonObjectString)
    
    # 解析json
    returnArray = []


    # 讀取其用來判斷的元件
    for jsonObject in jsonObjectArray:
      message_type = jsonObject.get('type')
          
      # 轉換
      if message_type == 'text':
          returnArray.append(TextSendMessage.new_from_json_dict(jsonObject))
      elif message_type == 'imagemap':
          returnArray.append(ImagemapSendMessage.new_from_json_dict(jsonObject))
      elif message_type == 'template':
          returnArray.append(TemplateSendMessage.new_from_json_dict(jsonObject))
      elif message_type == 'image':
          returnArray.append(ImageSendMessage.new_from_json_dict(jsonObject))
      elif message_type == 'sticker':
          returnArray.append(StickerSendMessage.new_from_json_dict(jsonObject))  
      elif message_type == 'audio':
          returnArray.append(AudioSendMessage.new_from_json_dict(jsonObject))  
      elif message_type == 'location':
          returnArray.append(LocationSendMessage.new_from_json_dict(jsonObject))
      elif message_type == 'flex':
          returnArray.append(FlexSendMessage.new_from_json_dict(jsonObject))  
      elif message_type == 'video':
          returnArray.append(VideoSendMessage.new_from_json_dict(jsonObject))    

    # 回傳
    return returnArray

# %%
'''
從劇本excel找回覆，並轉成消息
'''
from numpy import NaN
import math
import json

def drama_execl_to_json(user_input_keyword):
  result = plot_content[plot_content['keyword']==user_input_keyword]
  result_dict=result.to_dict()
  for field in result_dict.keys():
    for key in result_dict[field].keys():
      result_dict[field]= result_dict[field][key]
  
  reply_json_array=[]
  combin_json_array=['reply_message1','reply_message2','reply_message3','reply_message4','reply_message5']

  for ele in combin_json_array:
    if pd.isna(result_dict[ele]) is False:
      print(result_dict[ele])
      reply_json_array.append(json.loads(result_dict[ele]))
      print(reply_json_array)

  if pd.isna(result_dict['choice_button']) is False:
    reply_json_array[len(reply_json_array)-1].update(json.loads(result_dict['choice_button']))

  reply_message_array = detect_json_array_to_new_message_array(reply_json_array)
  return reply_message_array

# %%
'''
確認桶子是否存在，若不存在，則新建
'''
import boto3
import json

s3_client = boto3.client(
        's3',
        aws_access_key_id = client_aws_access_key_id,
        aws_secret_access_key = client_aws_secret_access_key,
        aws_session_token=client_aws_session_token,
        region_name=client_region_name
)

response = s3_client.list_buckets()
bucket_name_list=[]
for bucket in response['Buckets']:
  bucket_name_list.append(bucket['Name'])
print(bucket_name_list)

if client_bucket_name not in bucket_name_list:
  
  s3_client.create_bucket(Bucket=client_bucket_name)

  # Create a bucket policy
  bucket_policy = {
      'Version': '2012-10-17',
      'Statement': [{
          'Sid': 'AddPerm',
          'Effect': 'Allow',
          'Principal': '*',
          'Action': ['s3:GetObject'],
          'Resource': f'arn:aws:s3:::{client_bucket_name}/*'
      }]
  }
  # Convert the policy from JSON dict to string
  bucket_policy = json.dumps(bucket_policy)
  s3_client.put_bucket_policy(Bucket=client_bucket_name, Policy=bucket_policy)
else:
  print("桶子已建立")

# %% [markdown]
# 先到AWS學生帳號環境內，把Model打開來，之後不用記得要關掉，不然會一直收費喔！！！！
# 

# %%
import boto3

def show_custom_labels(model,photo, min_confidence):
    client=boto3.client(
        'rekognition',
        aws_access_key_id = client_aws_access_key_id,
        aws_secret_access_key = client_aws_secret_access_key,
        aws_session_token=client_aws_session_token,
        region_name=client_region_name
        )

    #Call DetectCustomLabels
    with open(photo, 'rb') as image:
      response = client.detect_custom_labels(Image={'Bytes': image.read()},
        MinConfidence=min_confidence,
        ProjectVersionArn=model
      )

    result = ' '
    if len(response['CustomLabels'])==0:
      result="這個AI模型無法辨認你想知道的事情"
    else:
      result = response['CustomLabels'][0]
      # for custom_label in response['CustomLabels']:
      #   result = result + ' ' + custom_label['Name'] 
      # for custom_label in response['CustomLabels']:
      #   result = result + ' ' + custom_label['Name'] 

    print(result)
    return result


# %%
# 設定Server啟用細節
app = Flask(__name__)
run_with_ngrok(app)

# %%
'''
建置主程序的API入口
  接受Line傳過來的消息
  並取出消息內容
  將消息內容存在google drive的檔案內
  並請handler 進行消息驗證與轉發
'''

# 啟動server對外接口，使Line能丟消息進來
@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print(body)
    
    with open('ai-event.log', 'a') as f:
      f.write(body)
      f.write('\n')


    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# %%
'''
用戶關注
'''
from linebot.models import(
    FollowEvent,ImageMessage, TextSendMessage
)
# 圖片下載與上傳專用
import urllib.request

@handler.add(FollowEvent)
def handle_follow_event(event):

  user=line_bot_api.get_profile(event.source.user_id)
  file_name = event.source.user_id + '.jpg'
  urllib.request.urlretrieve(user.picture_url, file_name)

  s3_client.upload_file(file_name, client_bucket_name, f"{event.source.user_id}/user_info.jpg")



# %%
'''

若收到圖片消息時，

先將收到的照片降維，降維之後才能比較


'''

from linebot.models import(
    MessageEvent,ImageMessage, TextSendMessage
)

@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):

    # 抓取用戶照片
    user_upload_image_file_name=event.message.id+'.jpg'
    message_content = line_bot_api.get_message_content(event.message.id)
    with open(user_upload_image_file_name, 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)

    s3_client.upload_file(user_upload_image_file_name, client_bucket_name, f"{event.source.user_id}/images/{event.message.id}.jpg")
    reply_text = show_custom_labels(model_arn,user_upload_image_file_name,90)
    
    
    if reply_text != '':
      if len(drama_execl_to_json(reply_text['Name']))!= 0 :
        line_bot_api.reply_message(
          event.reply_token,
          drama_execl_to_json(reply_text['Name'])
        )
      else:
        line_bot_api.reply_message(
          event.reply_token,
          TextSendMessage('此物件沒有劇情設計')
        )


    # if reply_text != ' ':
    #   line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(reply_text)
    #     )
    


# %%
'''
用戶收到文字消息

'''


from linebot.models import(
    MessageEvent,ImageMessage, TextSendMessage,TextMessage
)

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):

    if len(drama_execl_to_json(event.message.text)) != 0 :
      line_bot_api.reply_message(
        event.reply_token,
        drama_execl_to_json(event.message.text)
      )
    else:
      line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage('此物件沒有劇情設計')
      )

  

# %%
# 主程序運行
app.run()

# %%



