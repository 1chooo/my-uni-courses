# %% [markdown]
# #說明
# 
# 
# 1.   quickReplyAction 必須依附在一個message底下 跟著message一起被傳送
# 2.   一個message一次最多只能有13個任何種類的quickReplyAction
# 
# #使用步驟
# 
# 
# 
# 1.   輸入message本身的訊息內容
# 2.   輸入需要的quickReplyAction數量
# 3.   依序輸入每個quickReplyAction的種類代號以及對應所需要的參數
# 
# # quickReplyAction 種類代號、所需要的參數
# 詳細規則請見：https://developers.line.biz/en/reference/messaging-api/#postback-action
# 
# ### message action
# - label
# - text
# 
# ### postback action
# - label
# - data
# - text
# 
# ### URI action
# - label
# - uri
# 
# ### Datetime picker action
# - label
# - data
# - mode: 時間格式，只能有三種值：date, time, datetime
# - initial(optional)
# - max(optional)
# - min(optional)
# 
# ### Camera action
# - label
# 
# ### Camera roll action
# - label
# 
# ### Location action
# - label
# 
# 
# 
# 

# %%
#安裝套件
!pip install line-bot-sdk 

# %%
#注入模組
import json
import sys
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
    TemplateSendMessage,
    QuickReply,
    QuickReplyButton,
    MessageAction,
    PostbackAction, ImagemapSendMessage, ImageSendMessage, StickerSendMessage, AudioSendMessage, LocationSendMessage,
    FlexSendMessage, VideoSendMessage,
)


# %%


#訊息模板們

message={
   "type":"message",
   "label":"Yes",
   "text":"Yes"
}

postback={
   "type":"postback",
   "label":"Buy",
   "data":"action=buy&itemid=111",
   "text":"Buy"
}

uri={
   "type":"uri",
   "label":"View details",
   "uri":"http://example.com/page/222",
}


datetimepicker={
   "type":"datetimepicker",
   "label":"Select date",
   "data":"storeId=12345",
   "mode":"datetime",
   "initial":"2017-12-25t00:00",
   "max":"2018-01-24t23:59",
   "min":"2017-12-25t00:00"
}

camera={
   "type":"camera",
   "label":"Camera"
}

cameraRoll={
   "type":"cameraRoll",
   "label":"Camera roll"
}

location={
   "type":"location",
   "label":"Location"
}

#dictionary
all_action_dict={
    0:message,
    1:postback,
    2:uri,
    3:datetimepicker,
    4:camera,
    5:cameraRoll,
    6:location,
} 


show_dict={
    0:'message',
    1:'postback',
    2:'uri',
    3:'datetimepicker',
    4:'camera',
    5:'cameraRoll',
    6:'location',
}




# %%
#根據datetimepicker的mode來取得對應格式的時間
def get_date_time(mode):
    if mode==0:
            #mode:date
            print(f"========請輸入日期（YYYY-MM-DD）==========")
            date=input()
            return date
    elif mode==1:
            #mode:time
            print(f"========請輸入時間（H:M）Max: 23:59 Min: 00:00 ==========")
            time=input()
            return time
    elif mode==2:
            print(f"========請輸入日期（YYYY-MM-DD）==========")
            date=input() 
            print(f"========請輸入時間（H:M）Max: 23:59 Min: 00:00==========")
            time=input()
            return date+'t'+time

# %%
reply_message={
    "quickReply": {
      "items": []
    }
}

print("================1.輸入需要的quickReplyAction數量==================")
items_count=int(input())
if items_count > 13:
    print("ERROR:一個message一次最多只能有13個任何種類的quickReplyAction")
    #!kill -9 -1


#有幾個actions就跑幾次 每次生成一個action item
for i in range(items_count):
    print(f"========請選擇第 {i+1} 個quickReply action的種類代號==========")
    print(json.dumps(show_dict, indent = 2) )
    action_number=int(input())
    action_dict=all_action_dict[action_number]

    #print(json.dumps(action_dict, indent = 2) )

    print(f"=========請依指示輸入{action_dict['type']} action 的參數==========")
       
    print(f"========輸入 {action_dict['type']} action的 label==========")
    label=input()
    action_dict['label']=label

    if(action_number==0):
        #message action
        print(f"========輸入 {action_dict['type']} action的 text==========")
        action_dict['text']=input()

    elif(action_number==1):
        #postback action
        print(f"========輸入 {action_dict['type']} action的 text==========")
        action_dict['text']=input()
        print(f"========輸入 {action_dict['type']} action的 data==========")
        action_dict['data']=input()
        
    elif(action_number==2):
        #uri action
        print(f"========輸入 {action_dict['type']} action的 uri==========")
        action_dict['uri']=input()
        
    elif(action_number==3):
        #datetimepicker action
        print(f"========輸入 {action_dict['type']} action的 data==========")
        action_dict['data']=input()

        mode_dict={
            0:"date",
            1:"time",
            2:"datetime"
        }
        print(f"========選擇 {action_dict['type']} action的 mode,共有三種選擇 請輸入數字選擇==========")
        print(json.dumps(mode_dict, indent = 2))
        mode=int(input())
        action_dict['mode']=mode_dict[mode]

        y_n_dict={
            0:'no',
            1:'yes'
        }
        
        print(f"========是否需要設定 {action_dict['type']} action的 initial ?==========")
        print(json.dumps(y_n_dict, indent = 2))
        if int(input()):
            action_dict['initial']=get_date_time(mode)
        else:
            action_dict.pop('initial')

        print(f"========是否需要設定 {action_dict['type']} action的 max ?==========")
        print(json.dumps(y_n_dict, indent = 2))
        if int(input()):
            action_dict['max']=get_date_time(mode)
        else:
            action_dict.pop('max')

       
        print(f"========是否需要設定 {action_dict['type']} action的 min ?==========")
        print(json.dumps(y_n_dict, indent = 2))
        if int(input()):
            action_dict['min']=get_date_time(mode)
        else:
            action_dict.pop('min')
 
    item={
        "type": "action",
        "action": action_dict
    }
    #把生成的action item append到reply_message
    reply_message['quickReply']['items'].append(item)

#給linebot sdk 判斷輸入的資料有沒有問題
text_send_msg = TextSendMessage.new_from_json_dict(reply_message)
print(text_send_msg)

#轉變成json string
print("===========您的message json已經生成好了，請慢用===========")
reply_message_json=json.dumps(reply_message, indent = 2) 
print(reply_message_json)


# original_string = str(quick_reply)
# new_string = original_string.replace("'","\"")
# print(new_string)


# %%



