# Midterm Exam

## 109-2
b. Which layer of the TCP/IP model is equivalent to the session layer and the presentation layer of the OSI model?\
Note:
- OSI model: 7層
- TCP/IP model: 5層
- OSI model 的 application layer, presentation layer 與 session layer 一起合併到 application layer

## 109-3
- a. DDos attack: Distributed Denial of Service attack
  - 透過大量的分散的合法請求佔用資源，使目標電腦或伺服器無法正常運作
- b. IP spoofing: IP偽造
  - 帶有假的IP來源位址，讓攻擊者可以冒充身份
- c. packet sniffer: 封包偵測器
  - 擷取封包，以取得、分析資料
  - 是一種網絡流量數據分析的手段，

## 109-4
Briefly explain the encapsulation/decapsulation procedure on the switch and the router.\
switch:
- physical layer 解封裝到 link layer
- 查看 header 的 MAC address
router:
- link layer 解封裝到 network layer
- 查看 header 的 IP address

## 109-6
iterated query:
- 被聯絡的 DNS server 負責回答你可以去聯絡哪個 server


recursive query:
- 被聯絡的 DNS server 負責幫你去聯絡，並回答你 IP address
pros and cons:

iterated query: 可以避免 DNS server 負擔過重，但是需要多次的 query

recursive query: 只需要一次 query，但是高層級的 DNS server 負擔過重

## 109-13
- Mbits = 10^6 bits, Gbits = 10^9 bits

## 110-4
Which system call attaches a local address to a socket?
- bind()

## 110-5
Which system call is to specify queue size for a server socket?
- listen()

## 110-7
DNS resource record format is (name, value, type, ttl). A diferent type has the corresponding name and value which has the different meaning. What are the meanings of name and value when the types is "A" (5 marks) and "NS" (5 marks) respectively?\
舉例：\
動作1：local DNS 去問 TLD server：「www.google.com 的 IP address 是？」， 所以 TLD server 查詢自己的資料庫，看到了這行
- `name: .google.com, type: NS, value: ns1.google.com`


於是回答 local DNS，你可以去問 ns1.google.com ( Google 的 authoritative DNS server 的 hostname )

動作2：local DNS 去問 Google 的 authoritative DNS server： 「www.google.com 的 IP address 是？」， 所以 ns1.google.com 查詢自己的資料庫，看到了這行
- `name: www.google.com, type: A, value:111.222.333.444`


於是回答 local DNS，www.google.com 的 IP address 是 111.222.333.444

## 110-7,10
What is the mail server address for jojo@cs.ncu.edu.tw?\
Note:
CNAME: Canonical Name, 意思是「真實名稱」
- 例如：`name: www.google.com, type: CNAME, value: www.l.google.com`
- 這表示 www.l.google.com 是 www.google.com 的真實名稱, 而 www.google.com 是 www.l.google.com 的別名



## 110-12
Is it possible for an application to enjoy reliable data transfer
even when the application runs over UDP? If so, how?
- Yes, the application can implement the reliable data transfer by itself.

