# Reply

### [國產ChatGPT「TAIDE」介紹](https://github.com/NCU-GS4719-Python/Python-Community/discussions/1659)
非常感謝你分享 AI 的最新資訊，透過程式調整 AI 的參數對於開發者來說便能有更多樣性的掌握。

其他程式碼建議：可以在 \`\`\` 的右邊加上語言就會有 programming language 相對應的 syntax 

如下
\`\`\`python
paste your code here...
\`\`\`

如此，你上述的程式碼就會有以下的效果喔！
```py
#!/usr/bin/env python
import requests

# For local streaming, the websockets are hosted without ssl - http://
HOST = 'localhost:5000'
URI = f'http://{HOST}/api/v1/generate'

# For reverse-proxied streaming, the remote will likely host with ssl - https://
# URI = 'https://your-uri-here.trycloudflare.com/api/v1/generate'

class Promper:
  def __init__(self, template: str='', pattern: str=None):
    self.template = template
    self.pattern = pattern
    self.inputs = self.extract()
    self.records = []

  def extract():
    print(self.template, self.pattern)
    return None

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def run(prompt):
    request = {
        'prompt': prompt,
        'max_new_tokens': 1024,
        'auto_max_new_tokens': False,
        'max_tokens_second': 0,

        # Generation params. If 'preset' is set to different than 'None', the values
        # in presets/preset-name.yaml are used instead of the individual numbers.
        'preset': 'None',
        'do_sample': True,
        'temperature': 0.7,
        'top_p': 0.9,
        'typical_p': 1,
        'epsilon_cutoff': 0,  # In units of 1e-4
        'eta_cutoff': 0,  # In units of 1e-4
        'tfs': 1,
        'top_a': 0,
        'repetition_penalty': 1.18,
        'repetition_penalty_range': 0,
        'top_k': 40,
        'min_length': 0,
        'no_repeat_ngram_size': 0,
        'num_beams': 1,
        'penalty_alpha': 0,
        'length_penalty': 1,
        'early_stopping': False,
        'mirostat_mode': 0,
        'mirostat_tau': 5,
        'mirostat_eta': 0.1,
        'grammar_string': '',
        'guidance_scale': 1,
        'negative_prompt': '',

        'seed': -1,
        'add_bos_token': True,
        'truncation_length': 2048,
        'ban_eos_token': False,
        'custom_token_bans': '',
        'skip_special_tokens': True,
        'stopping_strings': []
    }

    response = requests.post(URI, json=request)

    if response.status_code == 200:
        result = response.json() #['results'][0]['text']
        return result
        #print(prompt + result)


if __name__ == '__main__':
    examples = [
      #"能告訴我如何申請自有雲服務嗎？",
      "請問1+1？",
      "資料結構中的Stack是什麼？",
    ]
    for exam in examples:
      prompt = f"""<bos>Human
{exam}<eos>
<bos>Assistant"""
      print(f"{bcolors.OKBLUE}Prompt:{bcolors.HEADER} {exam}{bcolors.ENDC}")
      result = run(prompt)
      response = result['results'][0]['text']
      print(f"{bcolors.OKBLUE}Result:{bcolors.HEADER} {response}{bcolors.ENDC}")
      print(f'--'*20)
```


### [剪刀 石頭 布!](https://github.com/NCU-GS4719-Python/Python-Community/discussions/1665)

看了你的文章覺得很有趣，因此想用現在正夯的 ChatGPT 快速寫一個剪刀、石頭、布程式。

#### 以下是問答過程
Q: 可以幫我用 python 寫一個剪刀石頭布的遊戲，對象是跟電腦玩，只要贏三次就宣告勝利

A: 當然可以！以下是一個簡單的Python代碼示例，實現剪刀石頭布遊戲，您對電腦進行多輪比賽，第一方贏得三輪即為勝利。遊戲過程中，您可以輸入"剪刀"、"石頭"或"布"來選擇您的動作，電腦則會隨機選擇動作。
```python
import random

def get_user_choice():
    user_choice = input("請選擇剪刀、石頭或布：")
    return user_choice

def get_computer_choice():
    choices = ["剪刀", "石頭", "布"]
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user, computer):
    if user == computer:
        return "平局"
    if (user == "剪刀" and computer == "布") or (user == "石頭" and computer == "剪刀") or (user == "布" and computer == "石頭"):
        return "玩家勝利"
    return "電腦勝利"

user_wins = 0
computer_wins = 0

while user_wins < 3 and computer_wins < 3:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"玩家選擇：{user_choice}")
    print(f"電腦選擇：{computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(f"結果：{result}\n")

    if result == "玩家勝利":
        user_wins += 1
    elif result == "電腦勝利":
        computer_wins += 1

if user_wins >= 3:
    print("玩家獲勝！")
else:
    print("電腦獲勝！")
```

這個代碼包含了用戶和電腦的選擇、贏家的確定，以及遊戲循環，直到有一方贏得三輪為止。希望這對你有所幫助！