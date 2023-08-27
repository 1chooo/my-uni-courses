# %% [markdown]
# 請先複製此檔案到自己的google drive內
# 
# 今天不是程式語言的語法教學課，重點目標在於讓大家能把程式語言這玩意當成一種普通語言來看待
# 
# 也沒什麼太高大上的

# %%
'''
寫程式其實就像是在照著語法寫文字給朋友讀，只是這個語法有一些規範。

像print()為什麼叫做print()，功效是什麼，其實就是一種規範，相當於大家在學英文時，得去翻英文字典，理解單字的意涵。

按shift+enter或旁邊三角形執行
'''
print("寫程式")

# %%
'''
我們學會中文之後，就有機會快速跟懂中文的勞動力溝通，請他們做事情

我們學會程式語言之後，就可以快速跟懂程式語言的電腦溝通，讓他們幫我們做事情

比如數學加減

'''
print(1+2)

# %%
'''

甚至可以叫他們去解聯立方程式

x+2y=1
x+y=0

'''

# 將x+2y=1，轉換成一種程式語言喜歡的表達方式
row_1=[1,2,1]
# 將x+y=0，轉換成一種程式語言喜歡的表達方式
row_2=[1,1,0]

# 把他們聯立後，印製出來
matrix_demo=[row_1,row_2]
print(matrix_demo)

# 讓row_1減掉row_2，看不懂沒關係，就是複雜，不然也不會有套件了
for i in range(0,len(row_1)):
 row_1[i]=row_1[i]-row_2[i]

# 得到[0,1,1] => 0x+1y=1 => y=1
print(row_1)

# %%
'''
人類世界為了溝通效率，會嘗試簡化言語，每個人會依照當下的地域環境，產生一種共同的溝通詞彙
比如飲料店的店員們，他們講中文，但學習了飲料店的行話，珍奶微微，溝通起來就更快速了。

電腦也得學習語法格式，這種學習叫做安裝套件

'''
# 
# 第一次使用，先安裝一個數學套件
!pip install numpy

# %%
'''
跟先前比起來，發現很多東西簡化了

'''
# 告訴電腦，我們使用的是numpy這個套件
# 就像告訴大家，我現在講的是飲料店的術語
import numpy as np

# 建置Array
row_1=np.array([1,2,1])
row_2=np.array([1,1,0])

# Array加減法
print(row_1 - row_2)

# %%
'''

商業世界就是要做商業資訊應用

做一個網路應用

'''

!pip install flask flask-ngrok

# %%
'''
人類世界，會開商店，並在店裡面制定一些規矩，
比如有人去小七時，跟店員喊個號碼，就會得到後面的香菸，這就是一種SOP

資訊世界，我們會架所謂的網站，並在裡面用程式設定一些規則
我們等等會設定幾個網址，當用戶訪問的時候，電腦就會依照我們編寫的規則，將規則下的產物傳給用戶

'''
from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/cxcxc")
def hello_123():
    return "大家好好享受青春"

if __name__ == '__main__':
    app.run()


