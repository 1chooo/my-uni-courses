# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/12
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

import json
import config
from flask import Flask
from flask import request
from flask import abort
from flask import jsonify
from linebot.models.events import MessageEvent
from linebot.models.events import FollowEvent
from flask_ngrok import run_with_ngrok
from linebot import WebhookHandler
from linebot import LineBotApi
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextSendMessage
from linebot.models import ImageMessage
from linebot.models import VideoMessage
from linebot.models import AudioMessage
from linebot.models import AudioSendMessage

# Initialize LineBotApi and WebhookHandler instances
line_bot_api = LineBotApi(config.line_bot_api)
handler = WebhookHandler(config.handler)

# Create Flask app and enable ngrok
app = Flask(__name__)
run_with_ngrok(app)

# Handle Line webhook callback
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    print(body)

    # Log user activity
    with open("./ai-event.log", "a") as f:
        f.write(body + '\n')

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# Handle user follow event
@handler.add(FollowEvent)
def handle_follow(event):
    user_profile = line_bot_api.get_profile(event.source.user_id)

    with open("./users.txt", "a") as myfile:
        myfile.write(json.dumps(vars(user_profile), sort_keys=True) + '\n')

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage('Hello, your information has been recorded.')
    )

# Handle image, audio, and video messages

@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):

    message_type = "Image"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            f'{message_type} has been uploaded. ID: {event.message.id}')
        )
    
    message_content = line_bot_api.get_message_content(event.message.id)
    with open(f'./{event.message.id}.{message_type.lower()}', 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)

@handler.add(MessageEvent, message=VideoMessage)
def handle_video_message(event):

    message_type = "Video"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            f'{message_type} has been uploaded. ID: {event.message.id}')
        )
    
    message_content = line_bot_api.get_message_content(event.message.id)
    with open(f'./{event.message.id}.{message_type.lower()}', 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)

@handler.add(MessageEvent, message=AudioMessage)
def handle_audio_message(event):

    message_type = "Audio"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            f'{message_type} has been uploaded. ID: {event.message.id}')
        )
    
    message_content = line_bot_api.get_message_content(event.message.id)
    with open(f'./{event.message.id}.{message_type.lower()}', 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)

# Run the Flask app
if __name__ == "__main__":
    app.run()
