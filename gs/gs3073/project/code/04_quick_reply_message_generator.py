# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/12
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.1
'''

import json
import sys
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    TemplateSendMessage, QuickReply, QuickReplyButton,
    MessageAction, PostbackAction, ImagemapSendMessage,
    ImageSendMessage, StickerSendMessage, AudioSendMessage,
    LocationSendMessage, FlexSendMessage, VideoSendMessage,
)

# Define message types
message_types = {
    0: 'message',
    1: 'postback',
    2: 'uri',
    3: 'datetimepicker',
    4: 'camera',
    5: 'cameraRoll',
    6: 'location',
}

# Define sample messages for each type
sample_messages = {
    'message': {
        "type": "message",
        "label": "Yes",
        "text": "Yes"
    },
    'postback': {
        "type": "postback",
        "label": "Buy",
        "data": "action=buy&itemid=111",
        "text": "Buy"
    },
    'uri': {
        "type": "uri",
        "label": "View details",
        "uri": "http://example.com/page/222",
    },
    'datetimepicker': {
        "type": "datetimepicker",
        "label": "Select date",
        "data": "storeId=12345",
        "mode": "datetime",
        "initial": "2017-12-25t00:00",
        "max": "2018-01-24t23:59",
        "min": "2017-12-25t00:00"
    },
    'camera': {
        "type": "camera",
        "label": "Camera"
    },
    'cameraRoll': {
        "type": "cameraRoll",
        "label": "Camera roll"
    },
    'location': {
        "type": "location",
        "label": "Location"
    },
}

def get_input(prompt):
    return input(prompt)

def get_date_time(mode):
    if mode == 0:
        print("========請輸入日期（YYYY-MM-DD）==========")
        date = get_input()
        return date
    elif mode == 1:
        print("========請輸入時間（H:M）Max: 23:59 Min: 00:00 ==========")
        time = get_input()
        return time
    elif mode == 2:
        print("========請輸入日期（YYYY-MM-DD）==========")
        date = get_input()
        print("========請輸入時間（H:M）Max: 23:59 Min: 00:00==========")
        time = get_input()
        return date + 't' + time

def main():
    print("================1.輸入需要的quickReplyAction數量==================")
    items_count = int(get_input())
    if items_count > 13:
        print("ERROR:一個message一次最多只能有13個任何種類的quickReplyAction")
        return
    
    reply_message = {
        "quickReply": {
            "items": []
        }
    }

    for i in range(items_count):
        print(f"========請選擇第 {i+1} 個quickReply action的種類代號==========")
        print(json.dumps(message_types, indent=2))
        action_number = int(get_input())
        action_type = message_types[action_number]

        action_dict = sample_messages[action_type]

        print(f"=========請依指示輸入{action_dict['type']} action 的參數==========")
       
        print(f"========輸入 {action_dict['type']} action的 label==========")
        action_dict['label'] = get_input()

        if action_number == 0:
            print(f"========輸入 {action_dict['type']} action的 text==========")
            action_dict['text'] = get_input()

        elif action_number == 1:
            print(f"========輸入 {action_dict['type']} action的 text==========")
            action_dict['text'] = get_input()
            print(f"========輸入 {action_dict['type']} action的 data==========")
            action_dict['data'] = get_input()
        
        # ... (similar input gathering for other action types)

        item = {
            "type": "action",
            "action": action_dict
        }
        reply_message['quickReply']['items'].append(item)

    text_send_msg = TextSendMessage.new_from_json_dict(reply_message)
    print(text_send_msg)

    reply_message_json = json.dumps(reply_message, indent=2)
    print("===========您的message json已經生成好了，請慢用===========")
    print(reply_message_json)

if __name__ == "__main__":
    main()
