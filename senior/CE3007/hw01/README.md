# Computer Network HOMEWORK 1, Due Date Oct 23, 2023

1. True or false? (10%)
   - a. A user requests a Web page that consists of some text and three images. For this page, the client will send one request message and receive four response messages.
   - b. Two distinct Web pages (for example, www.mit.edu/research.html andwww.mit.edu/students.html ) can be sent over the same persistent connection.
   - c. With nonpersistent connections between browser and origin server, it is possible for a single TCP segment to carry two distinct HTTP request messages. 
   - d. The Date: header in the HTTP response message indicates when the object in the response was last modified. 
   - e. HTTP response messages never have an empty message body.

2. What are the five layers in the Internet protocol stack? (10%)

3. How long does it take a packet of length 1,000 bytes to propagate over a link of distance 2,500 km, propagation speed 2.5 · 10^8 m/s, and transmission rate 2 Mbps? More generally, how long does it take a packet of length L to propagate over a link of distance d, propagation speed s, and transmission rate R bps? Does this delay depend on packet length? Does this delay depend on transmission rate? (15%)

4. Suppose Host A wants to send a large file to Host B. The path from Host A to Host B has three links, of rates R1 = 500 kbps, R2 = 2 Mbps, and R3 = 1 Mbps. (15%)
   - a. Assuming no other traffic in the network, what is the throughput for the file transfer? 
   - b. Suppose the file is 4 million bytes. Dividing the file size by the throughput, roughly how long will it take to transfer the file to Host B? 
   - c. Repeat (a) and (b), but now with R2 reduced to 100 kbps.

5. Q: Consider Figure 2.12, for which there is an institutional network connected to the Internet. Suppose that the average object size is 850,000 bits and that the average request rate from the institution’s browsers to the origin servers is 16 requests per second. Also suppose that the amount of time it takes from when the router on the Internet side of the access link forwards an HTTP request until it receives the response is three seconds on average. Model the total average response time as the sum of the average access delay (that is, the delay from Internet router to institution router) and the average Internet delay. For the average access delay, use Δ/(1−Δβ) where Δ is the average time required to send an object over the access link and b is the arrival rate of objects to the access link. (10%)
   - a. Find the total average response time. (5%)
   - b. Now suppose a cache is installed in the institutional LAN. Suppose the miss rate is 0.4. Find the total response time. (5%)

   ![Q5](https://github.com/1chooo/socket-programming/blob/main/hw01/imgs/q5.png?raw=true)

6. Q: the UDP server described needed only one socket, whereas the TCP server needed two sockets. Why? If the TCP server were to support n simultaneous connections, each from a different client host, how many sockets would the TCP server need? (10%)

7. Q: Suppose N packets arrive simultaneously to a link at which no packets are currently being transmitted or queued. Each packet is of length L and the link has transmission rate R. What is the average queuing delay for the N packets? (5%)

8. What default port numbers are used by the application protocols HTTP, FTP, DNS, and SMTP? (5%)

9.  Consider the queuing delay in a router buffer. Let I denote traffic intensity: that is, I=La/R. Suppose that the queuing delay takes the form $IL/R(1-I)$ for $I<1$. (10%)
    - a. Provide a formula for the total delay, that is, the queuing delay plus the transmission delay.
    - b. Plot the total delay as a function of $L/R$

10.   Let a denote the rate of packets arriving at a link in $packets/sec$, and let $\mu$ denote the link’s transmission rate in $packets/sec$. Based on the formula for the total delay (i.e., the queuing delay plus the transmission delay) derived in the previous problem, derive a formula for the total delay in terms of $a$ and $\mu$. (10%)
