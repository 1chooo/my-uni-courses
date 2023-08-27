# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/12
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

# Import necessary packages
import json
import math
import urllib.request
import boto3
import pandas as pd
from flask import Flask, request, abort
from flask_ngrok import run_with_ngrok
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    FollowEvent, ImageMessage, MessageEvent, TextMessage,
    TextSendMessage, ImageSendMessage, ImagemapSendMessage,
    LocationSendMessage, FlexSendMessage, VideoSendMessage,
    StickerSendMessage, AudioSendMessage, TemplateSendMessage
)
from linebot.models.template import (
    ButtonsTemplate, CarouselTemplate, ConfirmTemplate,
    ImageCarouselTemplate
)

# Load configuration settings
import config

def detect_json_array_to_new_message_array(jsonObjectString):
    jsonObject = json.loads(jsonObjectString)
    returnArray = []

    message_type = jsonObject.get('type')
    message_classes = {
        'text': TextSendMessage,
        'imagemap': ImagemapSendMessage,
        'template': TemplateSendMessage,
        'image': ImageSendMessage,
        'sticker': StickerSendMessage,
        'audio': AudioSendMessage,
        'location': LocationSendMessage,
        'flex': FlexSendMessage,
        'video': VideoSendMessage
    }

    if message_type in message_classes:
        message_class = message_classes[message_type]
        returnArray.append(message_class.new_from_json_dict(jsonObject))

    return returnArray

# Function to retrieve drama content from Excel and convert to JSON
def drama_execl_to_json(user_input_keyword):
    result = plot_content[plot_content['keyword'] == user_input_keyword]
    result_dict = result.to_dict()

    for field in result_dict.keys():
        for key in result_dict[field].keys():
            result_dict[field] = result_dict[field][key]
    
    reply_json_array = []
    combin_json_array = [
        'reply_message1', 
        'reply_message2', 
        'reply_message3', 
        'reply_message4', 
        'reply_message5'
    ]

    for ele in combin_json_array:
        if pd.notna(result_dict[ele]):
            reply_json_array.append(json.loads(result_dict[ele]))

    if pd.notna(result_dict['choice_button']):
        reply_json_array[len(reply_json_array) - 1].update(json.loads(result_dict['choice_button']))

    reply_message_array = detect_json_array_to_new_message_array(reply_json_array)
    return reply_message_array

def show_custom_labels(model,photo, min_confidence):
    client=boto3.client(
        'rekognition',
        aws_access_key_id=client_aws_access_key_id,
        aws_secret_access_key=client_aws_secret_access_key,
        aws_session_token=client_aws_session_token,
        region_name=client_region_name,
    )

    #Call DetectCustomLabels
    with open(photo, 'rb') as image:
        response = client.detect_custom_labels(
            Image={'Bytes': image.read()},
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

app = Flask(__name__)
run_with_ngrok(app)

# Set up LineBot API and handler
line_bot_api = LineBotApi(config.line_bot_api)
handler = WebhookHandler(config.handler)
client_aws_access_key_id = config.client_aws_access_key_id
client_aws_secret_access_key = config.client_aws_secret_access_key
client_aws_session_token = config.client_aws_session_token
client_bucket_name = config.client_bucket_name
client_region_name = config.client_region_name
model_arn = config.model_arn
plot_content = pd.read_excel("bearbear.xlsx")

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


@handler.add(FollowEvent)
def handle_follow_event(event):

  user=line_bot_api.get_profile(event.source.user_id)
  file_name = event.source.user_id + '.jpg'
  urllib.request.urlretrieve(user.picture_url, file_name)

  s3_client.upload_file(file_name, client_bucket_name, f"{event.source.user_id}/user_info.jpg")

@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):

    # 抓取用戶照片
    user_upload_image_file_name=event.message.id+'.jpg'
    message_content = line_bot_api.get_message_content(event.message.id)
    with open(user_upload_image_file_name, 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)

    s3_client.upload_file(
        user_upload_image_file_name, 
        client_bucket_name, 
        f"{event.source.user_id}/images/{event.message.id}.jpg"
    )
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

app.run()
