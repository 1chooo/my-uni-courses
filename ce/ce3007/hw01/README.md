# Computer Network HOMEWORK 1, Due Date Oct 23, 2023

### Q1. 
True or false? (10%) [[Reference]](https://quizlet.com/173544792/cis3210-true-or-false-flash-cards/)

- a. A user requests a Web page that consists of some text and three images. For this page, the client will send one request message and receive four response messages.  
- b. Two distinct Web pages (for example, `www.mit.edu/research.html` and `www.mit.edu/students.html`) can be sent over the same persistent connection.
- c. With nonpersistent connections between browser and origin server, it is possible for a single TCP segment to carry two distinct HTTP request messages. 
- d. The Date: header in the HTTP response message indicates when the object in the response was last modified. 
- e. HTTP response messages never have an empty message body.

**Answer:**

- F 
- T 
- F 
- F 
- F

### Q2.
What are the five layers in the Internet protocol stack? (10%)

**Answer:**

```
Application Layer
-----------------
Transport Layer
-----------------
Network Layer
-----------------
Data Link Layer
-----------------
Physical Layer
```

### Q3.
- How long does it take a packet of length $1,000 bytes$ to propagate over a link of distance $2,500 km$, propagation speed $2.5 \times 10^8 m/s$, and transmission rate $2 Mbps$?
- More generally, how long does it take a packet of length L to propagate over a link of distance d, propagation speed s, and transmission rate R bps?   
- Does this delay depend on packet length?  
- Does this delay depend on transmission rate? (15%)

**Answer:**

- $d/s = \frac{(2500 \times 10^3)}{(2.5 \times 10^8)}=0.01s$   
$+$ $L/R = \frac{1000 \times 8}{2 \times 10^6} = 4 \times 10^{-3} = 0.004$  
$= 0.014s = 14ms$
- $d/s$
- No
- No


### Q4.
Suppose Host A wants to send a large file to Host B. The path from Host A to Host B has three links, of rates $R1 = 500 kbps$, $R2 = 2 Mbps$, and $R3 = 1 Mbps$. (15%)

- a. Assuming no other traffic in the network, what is the throughput for the file transfer? 
- b. Suppose the file is 4 million bytes. Dividing the file size by the throughput, roughly how long will it take to transfer the file to Host B? 
- c. Repeat (a) and (b), but now with R2 reduced to $100 kbps$.

**Answer:**

- $500 kpbs$.
- $\frac{4 \times 10^6 \times 8}{500 \times 10^3} = 64 (seconds)$ 
- 100kbps, $\frac{4 \times 10^6 \times 8}{100*10^3} = 320 (seconds)$

### Q5.
Q: Consider Figure 2.12, for which there is an institutional network connected to the Internet. Suppose that the average object size is $850,000 bits$ and that the average request rate from the institution’s browsers to the origin servers is 16 requests per second. Also suppose that the amount of time it takes from when the router on the Internet side of the access link forwards an HTTP request until it receives the response is three seconds on average. Model the total average response time as the sum of the average access delay (that is, the delay from Internet router to institution router) and the average Internet delay. For the average access delay, use $\frac{\Delta}{1 - \Delta\beta}$ where $\Delta$ is the average time required to send an object over the access link and b is the arrival rate of objects to the access link. (10%) [[reference]](https://cis.temple.edu/~tug29203/18spring-3329/reading//hw2a.pdf)

![Q5](https://github.com/1chooo/socket-programming/blob/main/hw01/imgs/q5.png?raw=true)

- a. Find the total average response time. (5%)
- b. Now suppose a cache is installed in the institutional LAN. Suppose the miss rate is 0.4. Find the total response time. (5%)

**Answer:**

### Q6.
Q: the UDP server described needed only one socket, whereas the TCP server needed two sockets. Why? If the TCP server were to support n simultaneous connections, each from a different client host, how many sockets would the TCP server need? (10%) [[reference]](https://quizlet.com/81065929/416-chapter-2-flash-cards/)

**Answer:**

- UDP send all traffic into the same socket. TCP has a welcoming socket and then creates a new socket with each connection so TCP has $n + 1$ sockets.

### Q7.
Q: Suppose N packets arrive simultaneously to a link at which no packets are currently being transmitted or queued. Each packet is of length L and the link has transmission rate R. What is the average queuing delay for the N packets? (5%)

**Answer:**

The queuing delay is O for the first transmitted packet, $L/R$ for the second transmitted packet, and generally, $(n-1)L/R$ for the $n^{th}$ transmitted packet. Thus, the average delay for the $N$ packets is: 
  	
$(L/R + 2L/R + ...... + (N-1)L/R/N$

$= L/(RN) * (1 + 2 + ... + (N-1))$

$= L/(RN) * N(N-1)/2$

$= LN(N-1)/(2RN)$

$= (N-1)L/(2R)$

Note that here we used the well-known fact:

$1+2+ ....... + N = N(N+1) / 2$

### Q8.
What default port numbers are used by the application protocols **HTTP, FTP, DNS, and SMTP**? (5%)

**Answer:**

- HTTP: 80
- FTP: 20, 21
- DNS: 53
- SMTP: 25


### Q9.
Consider the queuing delay in a router buffer. Let I denote traffic intensity: that is, I=La/R. Suppose that the queuing delay takes the form $IL/R(1-I)$ for $I<1$. (10%) [[reference]](https://www.studocu.com/tw/document/chung-yuan-christian-university/computer-networks/%E8%A8%88%E7%B6%B2ch1%E9%A1%8C%E7%9B%AE%E7%AD%94%E6%A1%88-answer/10325123)

**Answer:**

- a. Provide a formula for the total delay, that is, the queuing delay plus the transmission delay.
  - The transmission delay is $L/R$. The total delay is $\frac{IL}{R(1 - I)} + \frac{L}{R} = \frac{L / R}{1 - I}$
- b. Plot the total delay as a function of $L/R$
  - Let $x = L/R$. Total Delay = $\frac{x}{1 - ax}$ For $x = 0$, the total delay increases, approaching infinity as $x$ approaches $1/a$.


### Q10.
Let a denote the rate of packets arriving at a link in $packets/sec$, and let $\mu$ denote the link’s transmission rate in $packets/sec$. Based on the formula for the total delay (i.e., the queuing delay plus the transmission delay) derived in the previous problem, derive a formula for the total delay in terms of $a$ and $\mu$. (10%) [[reference]](https://www.studocu.com/tw/document/chung-yuan-christian-university/computer-networks/%E8%A8%88%E7%B6%B2ch1%E9%A1%8C%E7%9B%AE%E7%AD%94%E6%A1%88-answer/10325123)

**Answer:**

- $Total \ delay = \frac{\frac{L}{R}}{1 - I} = \frac{L / R}{1 - \frac{aL}{R}} = \frac{\frac{1}{\mu}}{1 - a/{\mu}} = \frac{1}{\mu - a}$

