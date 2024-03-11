# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/12
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

# Import required libraries
import json
import config
import face_recognition
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
from linebot.models import ImagemapSendMessage
from linebot.models import TemplateSendMessage
from linebot.models import ImageSendMessage
from linebot.models import StickerSendMessage
from linebot.models import LocationSendMessage
from linebot.models import FlexSendMessage
from linebot.models import VideoSendMessage
from linebot.models import ImageMessage
from linebot.models import VideoMessage
from linebot.models import AudioMessage
from linebot.models import AudioSendMessage

# Initialize the Flask app
app = Flask(__name__)

# Configure Line bot API
line_bot_api = LineBotApi("CHANNEL_ACCESS_TOKEN")
handler = WebhookHandler("CHANNEL_SECRET")

# Load the memory image for comparison
memory_image_path = '006_memory.png'
picture_of_me = face_recognition.load_image_file(memory_image_path)
memory_face_encoding = face_recognition.face_encodings(picture_of_me, num_jitters=15)[0]

# Define the true answer reply message
true_answer_reply_json_string = '''
{
    "type": "template",
    "altText": "this is a confirm template",
    "template": {
        "type": "confirm",
        "actions": [
            {
                "type": "message",
                "label": "好",
                "text": "Yes"
            },
            {
                "type": "uri",
                "label": "那是啥",
                "uri": "https://www.cxcxc.io"
            }
        ],
        "text": "你總算找到這裡了，看樣子，是該讓你進來我們公司做實習生了。"
    }
}
'''

# Define the error answer reply message
error_answer_reply_json_string = '''
{
    "type": "text",
    "text": "很傷心，在你的心裡竟然不是我。"
}
'''

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

# Define the Line bot webhook endpoint
@app.route("/", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    
    return 'OK'

# Handle image messages
@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
    user_upload_image_file_name = event.message.id + '.jpg'
    message_content = line_bot_api.get_message_content(event.message.id)
    with open(user_upload_image_file_name, 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)

    unknown_picture = face_recognition.load_image_file(
        user_upload_image_file_name
    )
    unknown_face_encoding = face_recognition.face_encodings(
        unknown_picture, 
        num_jitters=30
    )[0]

    results = face_recognition.compare_faces(
        [memory_face_encoding], 
        unknown_face_encoding, 
        tolerance=0.35
    )
    
    if any(results):
        line_bot_api.reply_message(
            event.reply_token,
            json.loads(
                true_answer_reply_json_string
            )
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            json.loads(
                error_answer_reply_json_string
            )
        )

# Run the app
if __name__ == "__main__":
    app.run()
