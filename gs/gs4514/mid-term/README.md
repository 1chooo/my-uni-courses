# MID-Term Report
##### Data Visualization
##### Author: @1chooo

## Project Structure
```
PROJECT_ROOT
├── data             # data         
├── assets             
├── main.js                  
├── index.html               
├── style.css                
├── utilities.js             
├── chartData.js             
└── README.md                
```

上課時我們透過了電影資料的關係，藉以看出不同分類的電影，能帶來的收益關係以及各類電影如何以較少的成本賺到大把的收入，因此期中的報告便以此為出發點來練習如何透過網頁的方式來呈現資料視覺化的結果，於是乎我挑選了同樣具有相似特性的資料集，那就是——電玩遊戲，因為電玩遊戲具有類別，又能夠看出各類別的銷售關聯性，於是接下來的篇幅將會做更詳細的介紹。

![](./assets/pexels-jaroslav-nymburský-687811.jpg)

## 緣起

原先我在找資料集的時候，其實完全沒有想到電玩遊戲，反而是想要找「美國大學申請」相關的資料庫，畢竟現在正是我準備美國大學申請的階段，不過從中遇到了很多的狀況，我原本看重這類資料的點是：美國大學有各地情形，因此可以做出各地錄取結果的分析，不過在途中，不是只能找到單一大學的資料，就是只能找到單一年的資料，我甚至還在 Kaggle 上問資料來源的作者要如何取得，結果他回應我這是件不簡單的事，要自己去各大大學找尋並且自己統整，於是我便放棄了「美國大學申請」這份資料集，開始著手下一份資料及的找尋，後來我找尋一番看上了的資料是「奧運的選手奪牌」資料，心想奧運有各個國家、各個運動種類，資料應該很好聚合吧！不過還是遇到了麻煩，那就是國家數太多了，那時候檢查資料就有兩百多個，連五大洲的分類都沒有，而且我還發現了這個資料集的缺失，那就是奪牌人數是固定的，所以做累積的話，每年的長條圖都長一樣，也就失去了分析的意義了，於是還是決定換一個資料集，最後變選擇了「電玩遊戲」的資料集做分析，而接下來會逐一講解我做了哪些分析。

![](assets/Screen%20Shot%202023-04-17%20at%2011.21.48%20PM.png)

## 我做了哪些處理

首先就是對數據的處理以及觀察，很幸運地，我拿到的數據並沒有太多缺失值也沒有太多型別轉換的問題發生，所以目前都還滿順利的，透過課堂上的 “type()” 函式便將我的數據處理完成了，接著處理完數據後，便要著手觀察數據，於是我便自己定義了一個函式，可以用來看出該種類數據總共有幾種樣式以及各樣式分別代表的內容名稱，於是我便看出共有 13 種類別的遊戲，以及 31 種平台提供遊戲，於是透過此處理，我便確定了我的長條圖的 Y 軸可以用哪些內容呈現。

```js
export function countColumnTypes(data, columnName) {

    const types = d3.group(data, d => d[columnName]);
    console.log(`${columnName} types: ${types.size}`);
    types.forEach((value, key) => {
        console.log(`- ${key}`);
    });
}
```

<figure class="third">
<img src="assets/Screen%20Shot%202023-04-17%20at%2011.52.29%20PM.png" width="200"/><img src="assets/Screen%20Shot%202023-04-17%20at%2011.54.57%20PM.png" width="200"/>
</figure>

## 我做了哪些實驗以及觀察

我總共做了四個實驗：
1. Determine the cumulative Global Sales for each Video Game Genre to identify the highest-earning type.
2. Once all Video Game Genres have been reviewed, identify the platform with the highest earnings.
3. Since PS2 generated the most revenue, it is worth exploring whether its sales align with the industry trends of its genre.
4. Finally, analyzing user rating scores will help identify areas where PS2 can improve.

### Determine the cumulative Global Sales for each Video Game Genre to identify the highest-earning type.

首先我想看出各個類型的遊戲，哪些較符合大眾的市場，所以我就選擇了全球的銷售情形做加總，並且用來對應各種類，於是乎我得到的結果前三名分別是 “Action, Sports, Shooter”，得到這樣的結果好像沒有挺意外，畢竟現今主流遊戲確實都是這幾類，而且有趣的是這三類遊戲的銷售總額相加都快比其他還要多了！

![](assets/Screen%20Shot%202023-04-18%20at%2012.01.43%20AM.png)

### Once all Video Game Genres have been reviewed, identify the platform with the highest earnings.

看完了各類遊戲的收益後，我就想說，誒～既然平台這麼多，那就來看看誰賺最多錢吧！於是乎我就把原本的種類換成平台，同樣以全球銷售額來做依據，我只有挑選營業額有大於一百萬美元的，於是我這次得到的結果前三名分別是 “PS2, X360, PS3”，不過我看到的還不止這個，我發現 PS 家族幾乎獨霸了遊戲產業，三代的銷售額都在市場上佔有一席之地，看來遊戲機迭代的更迭，是可以影響玩家挑選平台的依據。

![](assets/Screen%20Shot%202023-04-18%20at%2012.06.37%20AM.png)

### Since PS2 generated the most revenue, it is worth exploring whether its sales align with the industry trends of its genre.

既然已經看完了賺錢的種類以及平台，那我就好奇了最賺錢的平台推出的遊戲類別會不會吻合最賺錢的那幾類，畢竟能在遊戲界賺到錢，想必從最賺得下手，肯定能拉高營業額吧！於是我就用了這個假設繼續我的實驗，我發現 PS2 賺最多的種類前三名分別是 “Sports, Action, Racing”，我發現跟主流類別是有差異的，因為 “Racing” 在主流排名中，其實大概在中間而已，而 PS2 卻可以靠他賺到錢，想必他有在這類別推出很強的大作，以吸引玩家購買。

![](assets/Screen%20Shot%202023-04-18%20at%2012.10.55%20AM.png)

### Finally, analyzing user rating scores will help identify areas where PS2 can improve.

最後我想看看使用者評分來判斷 PS2 是不是有哪些類別的遊戲是可以再改進，以獲得更多的收益，我是將所有使用者評分做平均以求得結果，不過當我畫出結果後，只能讚嘆 PS2 在各類別遊戲中都做得不錯，雖然因為類別緣故沒有太多收益（從前一個實驗結果）不過還是很認真地在做遊戲。

![](assets/Screen%20Shot%202023-04-18%20at%2012.16.30%20AM.png)

## 還有哪些可以做得更好

首先是我的程式碼，畢竟這個報告大多是用專案實作，我覺得我的 main.js 太多行了，所以我用了模組化的方式，把一些常常用到的 function 寫到其他檔案裡（詳細檔案結構可看 [GitHub Repo](https://github.com/1chooo/data-viz/tree/main/mid-term)），不過我覺得還是可以寫得更好，畢竟有很多變數是可以透過 function 傳入，我卻直接寫死在 function 裡，或許以後可以好好加強重構一下程式碼。

```html
<!-- Before -->
<script src="main.js"></script> 

<!-- After -->
<script type="module" src="main.js"></script>
```

再來是資料分析的部分，其實這個電玩遊戲數據集還有很多內容可以做分析，像是可以各大洲的遊戲情形，因為我這次主要是拿全球的銷售額做分析，不過其實還有地區的資料可以做地區性的探討，我想這也會是很可以做延伸的內容。

最後應該就是介面的優化了，畢竟我現在呈現的頁面只有單純的 html，都碰到網頁設計的語言—— JavaScripts 了，或許還可以把網頁做得更好，更多可玩性。

## 總結

這次的作業滿好玩的，看到結果確實呈現出來，也可以延續完整的故事性，雖然一開始找資料有點碰壁，但是後續實際處裡的過程我其實沒有花太多時間在 Debug，或許是寫程式的功力又提升了，也或是上課有認真聽講，不過這過程中我不只接觸了一門新的語言，也接觸了新的資料呈現方法，雖然還有很多內容可以去嘗試以及實踐，不過這次的經驗絕對是未來很重要的養分。

## Reference
* [Video Games Sales Dataset](https://www.kaggle.com/datasets/sidtwr/videogames-sales-dataset)
* [w3schools](https://www.w3schools.com/)
* [Olympics 124 years Dataset(till 2020)](https://www.kaggle.com/datasets/nitishsharma01/olympics-124-years-datasettill-2020)
* [US graduate schools's admission parameters](https://www.kaggle.com/datasets/musfiq47/us-graduate-schoolss-admission-parameters)