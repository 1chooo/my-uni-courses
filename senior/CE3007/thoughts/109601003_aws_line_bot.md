# AWS x LINE Bot 雲端探險計畫 

> Name: 林群賀  
> Dept.: 大氣四  
> ID: 109601003

在 2023/12/15 我參加了 AWS Educate 舉辦的工作坊，名稱為「AWS x LINE Bot 雲端探險計畫」，這是一個 3 小時的工作坊，主要是帶領我們使用 AWS 服務來建立一個 LINE Bot，並且過程中含有發想、設計、開發等等的流程，以設計出商業名片為主題，讓我們可以體驗到如何使用 AWS 服務來開發一個 LINE Bot。

- GitHub Repo: https://github.com/1chooo/aws-line-business-card-workshop

## 1. 介紹雲端

- 雲端服務的優點
  - 降低成本
  - 提升效率
  - 提升安全性
  - 提升可靠性
  - 提升彈性
  - 提升創新

我們聽到了一些使用雲端的優點以及雲端服務的種類，並且我們了解到為什麼要使用雲端以及量化經濟的概念，我們也使用了本次工作坊示範的 LINE BOT 名片，內容主要是介紹 AWS 的服務以及 AWS Educate Program 內容，並且目的是以推廣的方式讓我們了解到雲端服務的優點，讓我們了解到了等等需要完成的 LINE BOT。

## 2. 介紹 LINE BOT

- LINE BOT 的特色
  - 自動回覆
  - 訊息推播
  - 資料收集
  - 資料分析
  - 資料儲存
  - 資料處理
  - 資料視覺化
  - 資料呈現

我們聽到了一些使用 LINE BOT 的優點以及 LINE BOT 的特色，並且我們了解到為什麼要使用 LINE BOT 以及 LINE BOT 的使用情境，接下來我們要介紹 AWS 服務。

## 3. 介紹 AWS 服務

我們這次主要以 AWS 服務來開發 LINE BOT，並且我們使用了以下的服務：

- Amazon API Gateway
- AWS Lambda
- AWS s3

## 4. 工作坊實作

在工作坊中我們時做了一個 LINE BOT 名片，這個名片是一個可以讓使用者了解到我們公司的內容，因此一開始我們先找尋我們想要推廣的公司，緊接著依據以下內容設計出我們的 LINE BOT 名片：

- 設定加入好友訊息
- 公司創辦的故事
- 公司提供業務
- 公司的技術背景
- 公司的宗旨
- 公司的未來展望
- 製作 LINE BOT 的開發團隊

### 4.1. 建立 LINE BOT

首先我們要建立一個 LINE BOT，這個 LINE BOT 會是我們的名片，我們可以在這個 LINE BOT 中建立 Webhook URL、Channel Secret、Channel Access Token 等等。

### 4.2. 建立 AWS Lambda

我們以講著提供的 AWS Lambda function 為基礎，並且在這個 function 中加入我們的程式碼，這個程式碼會是我們的 LINE BOT 名片的內容，我們可以在這個 function 中建立 Webhook URL、Channel Secret、Channel Access Token 等等。  

### 4.3. 建立 Amazon API Gateway

我們要建立一個 Amazon API Gateway，這個 Amazon API Gateway 會是我們的 LINE BOT 與 AWS Lambda 的連結，我們可以在這個 Amazon API Gateway 中建立 Webhook URL。

### 4.4. 建立 AWS s3

因為有些企業的內容未必公開，因此我們需要一個儲存庫來儲存企業的內容，我們可以在這個 AWS s3 中建立 Bucket。在這個工作坊中我們用來當作抓取圖片的儲存庫。

## 5. 心得

