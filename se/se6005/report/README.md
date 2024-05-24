# Dcard - 軟體排程

## 講義中可以討論的內容

1. To show how graphical schedule representations are used by project management.
2. To discuss the notion of risks and the risk management process.
- Organize tasks concurrently to make optimal use of resources
- Minimize task dependencies to avoid delays caused by one task waiting for another to complete
- Dependent on project managers intuition and experience

## 我找到的資料


### Dcard 工程師認為不錯的 4 個 coding 習慣！ [^1]

除了排版跟風格之外，另一點我們會注意的是 coding 的架構設計。接到需求時，首先夥伴們會思考如何把需求拆小、可以做哪些功能，並跟其他成員一起討論。

這裡推薦測試驅動開發 (TDD) 方法。

TDD 本身其實是很簡單的觀念，重點在於一步步提出假設 (the test)，然後以程式碼驗證假設 (pass the test)，最後再透過重構 (refactoring the code) 的手段，讓程式碼更強固、精煉。但是要針對 domain knowledge 提出正確且可驗證的假設，卻是極不容易的。尤其是對不了解的 domain 更是如此，會需要不斷地練習，積累豐富的經驗後才能駕輕就熟。

所以雖然 Dcard 工程師們並不會要求能在工作上運用 TDD 方法，但建議可以在空閒時，刻意練習 TDD 及 refactoring 小步前進的觀念及做法。另外，在練習的時候，也不妨試著刻意用不同的策略方式來寫相同的功能，比較一下不同寫法的優缺點。

如果要練習 TDD，那就可以嘗試用自己慣用的測試框架，架構一套寫測試用的流程，縮短每一步測試的時間。

### Dcard 怎麼 WFH？很少人知道的 Backend Team 日常
OKR Release / Review
我們如何知道每次開發的專案目標？

公司從每年的戰略，切分成每一季的子目標去實現，而 Dcard 在這個基礎上將傳統的一季三個月縮短為一季兩個月，以便在快速發展的同時，更快速的做出應對，此外，公司各部門的發展目標，成效等也公開透明，在每季開始前向所有同仁簡介，每季結束後也會分享其成果，不只是加深了對其他部門的了解，更能強化了各部門合作。

在 Dcard 不只能學到所屬團隊領域的知識，透過各種會議、合作方式，不論隸屬於哪個 Team ，都會知道在各團隊內部的專案進度或技術等。

## 我的分析
- Dcard 因為是個社群為導向，因此任何一刻都不能造成服務中斷
- 拆分專案成小的 Tasks 並且要預估時長跟資源

另外，感覺團隊是以敏捷的概念作為開發，因為從 Dcard Lab 可以看出每天都有 Daily Meeting 並且將產品開發作為一季兩個月去實現子目標，如此希望可以更快速地去應對，同時也會有安排做 Review, Sharing 的時間

![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*C2Z4_ymBc3U-DrUkNhtGqA.png)

## 架構層面
以前端的架構設計為例，在開始 coding 前可以根據規格，依照 model / view / controller 的劃分，依序構想程式架構。這樣我們就能避免寫出來的架構不好、需要東加一個西加一個的的 code。


[^1] [Dcard 工程師認為不錯的 4 個 coding 習慣！](https://medium.com/dcardlab/dcard-%E5%B7%A5%E7%A8%8B%E5%B8%AB%E8%AA%8D%E7%82%BA%E4%B8%8D%E9%8C%AF%E7%9A%84-4-%E5%80%8B-coding-%E7%BF%92%E6%85%A3-ba1ddc7cf427)
[^2] [Dcard 怎麼 WFH？很少人知道的 Backend Team 日常](https://medium.com/dcardlab/dcard-%E6%80%8E%E9%BA%BC-wfh-%E5%BE%88%E5%B0%91%E4%BA%BA%E7%9F%A5%E9%81%93%E7%9A%84-backend-team-%E6%97%A5%E5%B8%B8-53770dcdbe42)

# Risk

因為 Dcard 開發週期為兩個月一個季，並且將任務分配給縮小，因此產品風險是可以預防下降的

Dcard 強調大量的員工訓練

3. 自主學習
團隊內部而言，Dcard 非常重視「自主學習」，並提供了許多相關資源在幫助員工成長。除了辦公室裡放有各領域書籍的書櫃、鼓勵員工組成讀書會以外，更開設社團讓大家可以申請想看的書/想參加的活動。

讀書會

企業與人才應該建立「聯盟關係」。

https://www.cw.com.tw/article/5126756

https://medium.com/ellia-%E6%98%AF%E5%80%8B%E5%A4%A7%E5%AD%B8%E7%94%9F/dcard%E4%BC%81%E6%A5%AD%E5%8F%83%E8%A8%AA-%E9%AB%98%E6%89%8B%E9%9B%B2%E9%9B%86%E7%9A%84%E5%B7%A5%E4%BD%9C%E7%92%B0%E5%A2%83-%E5%90%83%E4%B8%8D%E5%AE%8C%E7%9A%84%E9%A3%B2%E6%96%99%E9%BB%9E%E5%BF%83-254fd114e115


- Project
- Product
- Business