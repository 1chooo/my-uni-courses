# Material 06 Lab - Source Code Quality <!-- omit in toc -->

**Table of Contents**
- [Course](#course)
  - [Lab 01](#lab-01)
  - [Lab 03](#lab-03)
  - [Lab 05](#lab-05)
  - [Lab 06](#lab-06)
  - [Lab 07](#lab-07)
  - [Lab 08](#lab-08)
- [Code](#code)
  - [CODE-LAB CDC-DJ line 1-48](#code-lab-cdc-dj-line-1-48)
  - [CODE-LAB CDC-DJ line 49-63](#code-lab-cdc-dj-line-49-63)
  - [CODE-LAB CDC-DJ line 65-107](#code-lab-cdc-dj-line-65-107)
  - [CODE-LAB CDC-DJ line 134-199](#code-lab-cdc-dj-line-134-199)
  - [CODE-LAB CDC-DJ line 219-336](#code-lab-cdc-dj-line-219-336)
  - [針對 copy-paste programming 應該怎麼改（10倍分數）](#針對-copy-paste-programming-應該怎麼改10倍分數)
  - [CODE-LAB CDC-GK line 32-136](#code-lab-cdc-gk-line-32-136)
  - [CODE-LAB CDC-GK line 204-440](#code-lab-cdc-gk-line-204-440)
- [Take Home](#take-home)
  - [Homework - 針對 copy-paste programming 應該怎麼改（補交題，5倍分數）](#homework---針對-copy-paste-programming-應該怎麼改補交題5倍分數)

## Course 

### Lab 01

我的學生畢業之後出去工作，他們曾遇到 `main()` 的程式行數高達多少行 ?

> **My Answer:**
>
> 500 多行

### Lab 03

請用幾行文字解釋何謂的 coupling ?

> **My Answer:**
>
> 就是當今天產品變得非常大的時候，很多功能都會互相影響，當今天可能做了一個改動，很多的部分都要去修改，然而可能各個部分都是上萬行的規模。

### Lab 05

大部分的軟體工程與物件導向等技術都是在解決 _______________的問題  
OOAD 其實是一種 __________________的方法。

> **My Answer:**
>
> 1. Coupling （維護擴充）
> 2. Decoupling （去耦合）

### Lab 06

好的設計，或者是乾淨的介面在其他的工程領域（例如機械）通常很容易認知。但是在軟體卻非常難。原因是？

> **My Answer:**
>
> 因為軟體是一堆的文字，他沒有辦法像機械設計一樣，可以有設計圖紙，同樣地很多人沒有寫好品質程式碼的 Common Sense。再者，每個人設計軟體的規範都不相同，造就了現在所遇到的困難。

工程跟幾何無關

### Lab 07

你如果給我 3000 行的程式碼要我來判斷你的程式碼品質，理論上你的程式碼可能可讀性還不錯，但是你的程式碼好壞還要根據一個重要的依據，我才能判定好壞。這個重要的依據是？

> **My Answer:**
>
> 未來需要如何維護，以及未來所需要新增設的功能。

### Lab 08

Spaghetti Code – 是形容爛程式碼  
為何喜歡用 Spaghetti 來形容

> **My Answer:**
>
> 因為他會全部攪在一起，很難去看清楚什麼是什麼，也很難去定義裡面的內容物。

## Code

### CODE-LAB CDC-DJ line 1-48

```java
1 package Cdc; 
2  
3  
4 import java.io.*; 
5 import javax.swing.*; 
6 import java.awt.*; 
7 import java.util.*; //for Vecter 
8 import java.lang.*; 
9 import java.lang.*; 
10 import java.awt.event.*; 
11 import udpbc.*; 
12  
13  
14  
15 /** 
16 * <p>Title: </p> 
17 * <p>Description: </p> 
18 * <p>Copyright: Copyright (c) 2005</p> 
19 * <p>Company: </p> 
20 * @author not attributable 
21 * @version 1.0 
22 */ 
23  
24  
25  
26 public class Cdc { 
27 static UDPclient u1; 
28 // private int[][] characterDataBase = new  
int[characterNumber][characterDataBaseElement]; 
29 //characterDataBaseElement：speed，生命初始值，攻擊使別人失血量。30 // 0 1 2 
31 public int clientEatNpc = 0; 
32 public int[][] characterDataBase = { 
33 { 
34 0, 250, 20} 
35 , { 
36 0, 200, 30} 
37 , { 
38 0, 220, 25} 
39 , { 
40 0, 200, 25} 
41 }; 
42 int updatearray[]; 
43  
44 //npc：x，y，eaten，index(clientNo = nowCharacterNum+1)。 45 // 0 1 2 3 
46 int[] npc = { 
47 3, 6, 0, 0}; 
48 int npcElement = npc.length; 
```

> **My Answer:**
>
> 1. 使用大量的 static 變數，很多無關的變數都在這裡寫上。當看到有這麼多 static 變數的時候，代表寫的人當成當 Global 在用
> 31, 33 行宣告很多 class 的變數為 public
> 34, 36, 37 有大量 { 0, 250, 20} , { 0, 200, 30} , { 0, 220, 25} , { 0, 200, 25} };  這是 magic number，不知道這些數字是什麼意思。

### CODE-LAB CDC-DJ line 49-63

```java
49  
50 boolean eaten = false; 
51 static final int characterNumber = 6; //clientNo不用0，從1開始。52 int nowCharacterNum = 0; 
53 static final int characterElement = 7; 
54 //characterElement：動物種類，dir，speed，x，y，生命值，(是1)(否0)發動攻擊。55 // 0 1 2 3 4 5 6 
56 static public int[][] character = new int[characterNumber][characterElement]; 57 static final int MAX_map = 30; 
58 static public int[][] map = new int[MAX_map][MAX_map]; 
59 Vector info = new Vector(); 
60 private int itemNumber = 1; //info vector 第0個為itemNumber，目前沒有用到。61 static public Npc n1; 
62 static position p1; 
63 // DiedJudge d1; 
```

> **My Answer:**
> 
> 51, 53 是 magic Number

### CODE-LAB CDC-DJ line 65-107

```java
65 public Cdc() { 
66 n1 = new Npc(this); 
67 p1 = new position(this); 
68 // d1 = new DiedJudge(this); 
69 // d1.start(); 
70 p1.start(); 
71 // n1.start(); 
72 
73 map[0][13] = map[0][14] = map[0][15] = map[0][16] = -1; 74 map[1][13] = map[1][14] = map[1][15] = map[1][16] = -1; 75 map[2][13] = map[2][14] = map[2][15] = map[2][16] = -1; 76 map[10][8] = map[10][9] = map[10][10] = map[10][11] = -1; 
77 map[10][12] = map[10][17] = map[10][18] = map[10][19] = -1; 78 map[10][20] = map[10][21] = -1; 
79 map[11][8] = map[11][9] = map[11][10] = map[11][11] = -1; 80 map[11][12] = map[11][17] = map[11][18] = map[11][19] = -1; 81 map[11][20] = map[11][21] = -1; 
82 map[12][8] = map[12][9] = map[12][10] = map[12][11] = -1; 83 map[12][12] = map[12][17] = map[12][18] = map[12][19] = -1; 84 map[12][20] = map[12][21] = -1; 
85 map[17][8] = map[17][9] = map[17][10] = map[17][11] = -1; 86 map[17][12] = map[17][17] = map[17][18] = map[17][19] = -1; 87 map[17][20] = map[17][21] = -1; 
88 map[18][8] = map[18][9] = map[18][10] = map[18][11] = -1; 89 map[18][12] = map[18][17] = map[18][18] = map[18][19] = -1; 90 map[18][20] = map[18][21] = -1; 
91 map[19][8] = map[19][9] = map[19][10] = map[19][11] = -1; 92 map[19][12] = map[19][17] = map[19][18] = map[19][19] = -1; 93 map[19][20] = map[19][21] = -1; 
94 map[13][0] = map[13][1] = map[13][2] = map[13][27] = -1; 95 map[13][28] = map[13][29] = -1; 
96 map[14][0] = map[14][1] = map[14][2] = map[14][27] = -1; 97 map[14][28] = map[14][29] = -1; 
98 map[15][0] = map[15][1] = map[15][2] = map[15][27] = -1; 99 map[15][28] = map[15][29] = -1; 
100 map[16][0] = map[16][1] = map[16][2] = map[16][27] = -1; 101 map[16][28] = map[16][29] = -1; 
102 map[27][13] = map[27][14] = map[27][15] = map[27][16] = -1; 103 map[28][13] = map[28][14] = map[28][15] = map[28][16] = -1; 104 map[29][13] = map[29][14] = map[29][15] = map[29][16] = -1; 105 init(); 
106 } 
107  
```

> **My Answer:**
>
> 1. 73 - 102 有大量的不知所以陣列。
> 2. 66, 67 new 了不知道要幹嘛的元素，如果有關聯可以直接繼承過來。

Cdc 是個 Constructor 但還在裡面 new 了很多的物件，應該只專心的初始化自己的記憶體。

把變動的部分寫死在程式碼。 `map` 理論上是要由檔案讀進來。

總結，他把資料內嵌在程式碼裡面，愚蠢的做法。

### CODE-LAB CDC-DJ line 134-199

```java
134 public Vector getAddInfo() { 
135 String infoString = "C"; 
136 info.add(Integer.toString(itemNumber)); //SET itemNumber; 
137 for (int i = 1; i <= nowCharacterNum; i++) { 
138 infoString = infoString + Integer.toString(i) + 
139 Integer.toString(character[i][0]); 
140 info.add(infoString); 
141 infoString = "C"; 
142 } 
143 infoString = "I0"; 
144 info.add(infoString); 
145 return info;
146 } 
147  
148 synchronized public Vector getUpdateInfo() { 
149 // int itemNumber = 0; //info vector 第0個為itemNumber，目前沒有用到。150 info.add(Integer.toString(itemNumber)); 
151 String infoString = "C"; 
152 String tempString = ""; 
153 for (int i = 1; i <= nowCharacterNum; i++) { 
154 infoString = infoString + Integer.toString(i); //clientNo 
155 for (int j = 1; j < characterElement; j++) { 
156 // System.out.print(character[i][j]); 
157 tempString = Integer.toString(character[i][j]); 
158  
159 if (j == 2 ) { //2位數。 
160 if (tempString.length() == 1) //不足2位數補0。 
161 tempString = "0" + tempString; 
162 } 
163 else if (j == 3 || j == 4 || j == 5) { //3位數。 
164 if (tempString.length() != 3) { 
165 if (tempString.length() == 1) 
166 tempString = "00" + tempString; 
167 else 
168 tempString = "0" + tempString; 
169 } 
170 } 
171 infoString = infoString + tempString; 
172 // System.out.println(infoString); 
173 } 
174 // System.out.println(""); 
175 // System.out.println(infoString); 
176 info.add(infoString); 
177 infoString = "C"; 
178 } 
179  
180 // System.out.println("in getUpdateInfo. npcElement is " + npcElement ); 181 infoString = "I"; 
182 for(int j=0; j<itemNumber; j++){ //把item的東西加到vector裡面。
183 for (int i = 0; i < npcElement-1; i++) { 
184 tempString = Integer.toString(npc[i]); 
185 if (i == 0 || i == 1) { 
186 if (tempString.length() != 3) { 
187 if (tempString.length() == 1) 
188 tempString = "00" + tempString; 
189 else 
190 tempString = "0" + tempString; 
191 } 
192 } 
193 infoString = infoString + tempString; 
194 } 
195 infoString = infoString + Integer.toString(0); 
196 info.add(infoString); 
197 infoString = "I"; 
198 } 
199  
```

> **My Answer:**
>
> 138 行做了很多的型別轉換，應該直接另外設計一個功能來達成，否則未來很難做變動。這段做了很多 String 的運算，但是看不出來為什麼要加上這些數字，又或是這些數字是什麼意思。

159-163 Hardwire 用 if then else 邏輯寫死在程式裡面，而不是用其他的資料結構

這個人其實不會抽象畫，有兩個迴圈，裡面又有邏輯判斷，通常會包裝成 function code，通常兩層以上的迴圈會變得非常難理解。


### CODE-LAB CDC-DJ line 219-336

```java
219 public void UpdateDirection(int clientno, int Movecode) { 
220 int tempx; 
221 int tempy; 
222 tempx = character[clientno][3]; 
223 tempy = character[clientno][4]; 
224 switch (Movecode) { 
225 case 0: 
226 character[clientno][2] = 0; 
227 break; 
228 case 1: 
229 if (cango(tempx, tempy - 10, 1, clientno)) { 
230 character[clientno][1] = 1; 
231 character[clientno][2] = 1; 
232  
233 // drawmap(tempx,tempy,clientno,1); 
234 // System.out.println("UpdateDir " + character[clientno][3] + " " + 
235 // character[clientno][4]); 
236 } 
237 break; 
238 case 3: 
239 if (cango(tempx, tempy + 10, 3, clientno)) { 
240 // drawmap(tempx,tempy,clientno,2); 
241 character[clientno][1] = 3; 
242 character[clientno][2] = 1; 
243  
244 // System.out.println(character[clientno][3] + " " + 
245 // character[clientno][4]); 
246 } 
247 break; 
248 case 4: 
249 if (cango(tempx - 10, tempy, 4, clientno)) { 
250 // drawmap(tempx,tempy,clientno,3); 
251 character[clientno][1] = 4; 
252 character[clientno][2] = 1; 
253 //System.out.println("west dir " +character[clientno][2]); 
254 // System.out.println(character[clientno][3] + " " + 
255 // character[clientno][4]); 
256 } 
257 break; 
258 case 2: 
259 if (cango(tempx + 10, tempy, 2, clientno)) { 
260 // drawmap(tempx,tempy,clientno,4); 
261 character[clientno][1] = 2; 
262 character[clientno][2] = 1; 
263 // System.out.println(character[clientno][3] + " " + 
264 // character[clientno][4]); 
265 } 
266 break; 
267 } 
268 } 
269  
270  
271 //判斷是否下一個想要走的位置可以走,可以的話回傳true,否則回傳false 
272 boolean cango(int tempx, int tempy, int move, int no) { 
273 int x1, x2, x3, x4, xx; 
274 int y1, y2, y3, y4, yy; 
275 int mapx, mapy; 
276 x1 = tempx - 30 +1; //先取出各角落的pixel值 
277 x2 = tempx - 10 +1; //用此角落的值,去做碰撞的判斷 278 x3 = tempx + 10 -1; // 加或減一,是以防碰到邊界,避免map判斷出錯
279 x4 = tempx + 30 -1; 
280 y1 = tempy - 30 +1; 
281 y2 = tempy - 10 +1; 
282 y3 = tempy + 10 -1; 
283 y4 = tempy + 30 -1; 
284 if (x1 < 0 || x4 > 600 || y1 < 0 || y4 > 600) { //邊界判定 
285 // System.out.println("because of bound"); 
286 return false; 
287 } 
288 //map 
289 switch (move) { //根據要移動的方向,去看map是否有障礙 
290 case 1: 
291 mapy = y1 / 20; //map的障礙物,用array儲存,所以用/20來取map位置
292 if (map[mapy][x1 / 20] == -1 || map[mapy][x2 / 20] == -1 || 
293 map[mapy][x3 / 20] == -1 || map[mapy][x4 / 20] == -1) { 
294 // System.out.println("because of map"); 
295 return false; 
296 } 
297 break; 
298 case 2: //往2方向的碰撞判定 299 mapx = x4 / 20; 
300 if (map[y1/20][mapx] == -1 || map[y2 / 20][mapx] == -1 || 
301 map[y3 / 20][mapx] == -1 || map[y4 / 20][mapx] == -1) { 
302 // System.out.println("because of map"); 
303 return false; 
304 } 
305 break; 
306 case 3: //往3方向的碰撞判定 307 mapy = y4 / 20; 
308 if (map[mapy][x1 / 20] == -1 || map[mapy][x2 / 20] == -1 || 
309 map[mapy][x3 / 20] == -1 || map[mapy][x4 / 20] == -1) { 
310 // System.out.println("because of map"); 
311 return false; 
312 } 
313 break; 
314 case 4: //往4方向的碰撞判定 
315 mapx = x1 / 20; 
316 if (map[y1 / 20][mapx] == -1 || map[y2 / 20][mapx] == -1 || 
317 map[y3 / 20][mapx] == -1 || map[y4 / 20][mapx] == -1) { 
318 // System.out.println("because of map"); 
319 return false; 
320 } 
321 break; 
322 } 
323 for (int z = 1; z <= 4; z++) { //去看其他腳色是否有碰撞的情況
324 yy = character[z][4]; 
325 xx = character[z][3]; 
326 if (z != no) { 
327 if ( (xx - tempx < 60 && xx - tempx > -60) && 
328 (yy - tempy < 60 && yy - tempy > -60)) { 
329 // System.out.println("because of client" + z); 
330 return false; 
331 } 
332 } 
333 } 
334 return true; 
335 } 
336 } 
```


> **My Answer:**
>
> 220, 221 不知道存在變數的意義是為何？
> 
> 都已經寫成 case 了，裡面還要繼續的做 if then else 判斷。
> 
> 273 - 283 很明顯會是個可以獨立出來的 function code。不用直接寫在 class 裡面。

1. 程式碼的後半部，開始有 copy-paste 的 pattern 出現，他做出了 copy-paste programming，239 到 246 行，249 到 256 行，259 到 266 行，這些都是重複的程式碼，應該要抽象化出來。
2. 耦合度過高（修改的漣漪），當我們今天要修改一個地方，很多地方都要去修改，

### 針對 copy-paste programming 應該怎麼改（10倍分數）

> 首先 219 - 263，因為 case 裡面還有 if 判斷，首先我會先把這些 if 判斷給獨立出來。另外要賦予的值，我也會寫成獨立的去有代表的意義。
> 
> 再來後面的部分，我也會把每個 move 這個獨立的 action 給另外去寫，同樣也會把角落的值給用其他變數去賦予意義，也就是我會做出一個 interface 去讓他存取。

> [!TIP]
> 可以變成查表法去撰寫。

### CODE-LAB CDC-GK line 32-136

```java
32 public CDC() 
33 { 
34 s = "8";//判斷字元 
35 i1 = i2 = i3 = i4 = i5 = i6 = i7 = i8 = 0; 
36 players = 0;//玩家人數 
37 for (int j = 0; j < 20; j++)//initialize 所有物品 38 { 
39 for (int k = 0; k < 20; k++) 
40 { 
41 check[j][k] = true;//預設true可挖false已挖 42 int rand; 
43 rand = (int) (Math.random() * 8) + 1; //rand = 1~8共八項物品44 if ( rand == 1 && i1 > 171 )//限制金礦個數 ＝ 171 45 { 
46 k--; 
47 continue; 
48 } 
49 else if ( rand == 1 && i1 <= 171 ) 
50 i1++; 
51 if ( rand == 2 && i2 > 200 )//限制銀礦個數 ＝ 200 52 { 
53 k--; 
54 continue; 
55 } 
56 else if ( rand == 2 && i2 <= 200 ) 
57 i2++; 
58 if ( rand == 3 && i3 > 5 )//限制+2金個數 ＝ 5 59 { 
60 k--; 
61 continue; 
62 } 
63 else if ( rand == 3 && i3 <= 5 ) 
64 i3++; 
65 if ( rand == 4 && i4 > 4 )//限制瞬間移動個數 ＝ 4 66 { 
67 k--; 
68 continue; 
69 } 
70 else if ( rand == 4 && i4 <= 4 ) 
71 i4++; 
72 if ( rand == 5 && i5 > 5 )//限制-2金個數 ＝ 4 73 {
74 k--; 
75 continue; 
76 } 
77 else if ( rand == 5 && i5 <= 5 ) 
78 i5++; 
79 if ( rand == 6 && i6 > 8 )//限制捶子個數 ＝ 8 80 { 
81 k--; 
82 continue; 
83 } 
84 else if ( rand == 6 && i6 <= 8 ) 
85 i6++; 
86 if ( rand == 7 && i7 > 8 )//限制金礦個數 ＝ 171 87 { 
88 k--; 
89 continue; 
90 } 
91 else if ( rand == 7 && i7 <= 8 ) 
92 i7++; 
93 if ( rand == 8 && i3 > 5 )//限制均富個數 ＝ 8 94 { 
95 k--; 
96 continue; 
97 } 
98 else if ( rand == 8 && i8 <= 5 ) 
99 i8++; 
100 map[j][k] = rand; 
101 } 
102 } 
103 check[0][0] = false; 
104 check[0][1] = false; 
105 check[1][0] = false; 
106 check[19][0] = false; 
107 check[19][1] = false; 
108 check[18][0] = false; 
109 check[0][19] = false; 
110 check[1][19] = false; 
111 check[0][18] = false; 
112 check[19][19] = false; 
113 check[18][19] = false; 
114 check[19][18] = false; 
115 check[9][9] = false; 
116 check[9][10] = false; 
117 check[10][9] = false; 
118 check[10][10] = false; 
119 map[0][0] = 0; 
120 map[0][1] = 0; 
121 map[1][0] = 0; 
122 map[19][0] = 0; 
123 map[19][1] = 0; 
124 map[18][0] = 0; 
125 map[0][19] = 0; 
126 map[1][19] = 0; 
127 map[0][18] = 0; 
128 map[19][19] = 0; 
129 map[18][19] = 0; 
130 map[19][18] = 0; 
131 map[9][9] = 0; 
132 map[9][10] = 0; 
133 map[10][9] = 0; 
134 map[10][10] = 0; 
135 } 
136  
```

34, 35 開始用奇怪的變數，


### CODE-LAB CDC-GK line 204-440

```java
204 public synchronized void addVirtualCharacter(int clientno, int pic)
205 { 
206 players++; 
207 Characters[clientno - 1] = new VirtualCharacter(); 
208 Characters[clientno - 1].clientno = clientno; 
209 Characters[clientno - 1].pic = pic; 
210 Characters[clientno - 1].money = 0; 
211 Characters[clientno - 1].gold = 0; 
212 Characters[clientno - 1].siliver = 0; 
213 Characters[clientno - 1].pick = 1; 
214 Characters[clientno - 1].mode = 0; 
215 switch (clientno) 
216 { 
217 case 1: 
218 Characters[clientno - 1].dir = 0; 
219 Characters[clientno - 1].x = 0;
220 Characters[clientno - 1].y = 0; 
221 s = s.valueOf("C1" + Characters[clientno - 1].pic); 
222 break; 
223 case 2: 
224 Characters[clientno - 1].dir = 0; 
225 Characters[clientno - 1].x = 19; 
226 Characters[clientno - 1].y = 0; 
227 s = s.valueOf("C2" + Characters[clientno - 1].pic); 
228 break; 
229 case 3: 
230 Characters[clientno - 1].dir = 0; 
231 Characters[clientno - 1].x = 0; 
232 Characters[clientno - 1].y = 19; 
233 s = s.valueOf("C3" + Characters[clientno - 1].pic); 
234 break; 
235 case 4: 
236 Characters[clientno - 1].dir = 0; 
237 Characters[clientno - 1].x = 19; 
238 Characters[clientno - 1].y = 19; 
239 s = s.valueOf("C4" + Characters[clientno - 1].pic); 
240 break; 
241 } 
242 } 
243 public synchronized void updateDirection(int clientno, int MoveCode) 244 { 
245 if (MoveCode == 1 && Characters[clientno - 1].y - 1 >= 0) 
246 { //up and walk 
247 Characters[clientno - 1].y = Characters[clientno - 1].y - 1; 248 System.out.println("第"+clientno+"位玩家方向向上走"); 
249 System.out.println("第"+clientno+"位玩家的x座標為"+Characters[clientno - 1].x); 250 System.out.println("第"+clientno+"位玩家的y座標為"+Characters[clientno - 1].y); 251 Characters[clientno - 1].dir = 1; 
252 } 
253 else if (MoveCode == 0 && Characters[clientno - 1].y + 1 <= 19) 254 { //down and walk 
255 Characters[clientno - 1].y = Characters[clientno - 1].y + 1; 256 System.out.println("第"+clientno+"位玩家方向向下走"); 
257 System.out.println("第"+clientno+"位玩家的x座標為"+Characters[clientno - 1].x); 258 System.out.println("第"+clientno+"位玩家的y座標為"+Characters[clientno - 1].y); 259 Characters[clientno - 1].dir = 0; 
260 } 
261 else if (MoveCode == 2 && Characters[clientno - 1].x - 1 >= 0) 262 { //left and walk 
263 Characters[clientno - 1].x = Characters[clientno - 1].x - 1; 264 System.out.println("第"+clientno+"位玩家方向向左走"); 
265 System.out.println("第"+clientno+"位玩家的x座標為"+Characters[clientno - 1].x); 266 System.out.println("第"+clientno+"位玩家的y座標為"+Characters[clientno - 1].y); 267 Characters[clientno - 1].dir = 2; 
268 } 
269 else if (MoveCode == 3 && Characters[clientno - 1].x + 1 <=19) 270 { //right and walk 
271 Characters[clientno - 1].x = Characters[clientno - 1].x + 1; 272 System.out.println("第"+clientno+"位玩家方向向右走"); 
273 System.out.println("第"+clientno+"位玩家的x座標為"+Characters[clientno - 1].x); 274 System.out.println("第"+clientno+"位玩家的y座標為"+Characters[clientno - 1].y); 275 Characters[clientno - 1].dir = 3; 
276 } 
277 else if (MoveCode == 6 )//up and turn 
278 { 
279 if ( Characters[clientno - 1].y != 0 ) 
280  
System.out.println("第"+clientno+"位玩家的上方物品屬性"+check[Characters[clien tno - 1].x][Characters[clientno - 1].y -1]); 
281 Characters[clientno - 1].dir = 1; 
282 System.out.println("第"+clientno+"位玩家方向轉向上"); 
283 System.out.println("第"+clientno+"位玩家的x座標為"+Characters[clientno - 1].x); 284 System.out.println("第"+clientno+"位玩家的y座標為"+Characters[clientno - 1].y); 285 } 
286 else if (MoveCode == 7 )//down and turn 
287 { 
288 if ( Characters[clientno - 1].y != 19 ) 
289  
System.out.println("第"+clientno+"位玩家的下方物品屬性"+check[Characters[clien
tno - 1].x][Characters[clientno - 1].y + 1]); 
290 Characters[clientno - 1].dir = 0; 
291 System.out.println("第"+clientno+"位玩家方向轉向下"); 
292 System.out.println("第"+clientno+"位玩家的x座標為"+Characters[clientno - 1].x); 293 System.out.println("第"+clientno+"位玩家的y座標為"+Characters[clientno - 1].y); 294 } 
295 else if (MoveCode == 8 )//left 
296 { 
297 if (Characters[clientno - 1].x != 0 ) 
298  
System.out.println("第"+clientno+"位玩家的左方物品屬性"+check[Characters[clien tno - 1].x-1][Characters[clientno - 1].y ]); 
299 Characters[clientno - 1].dir = 2; 
300 System.out.println("第"+clientno+"位玩家方向轉向左"); 
301 System.out.println("第"+clientno+"位玩家的x座標為"+Characters[clientno - 1].x); 302 System.out.println("第"+clientno+"位玩家的y座標為"+Characters[clientno - 1].y); 303 } 
304 else if (MoveCode == 9 )//right 
305 { 
306 if (Characters[clientno - 1].x != 19) 
307  
System.out.println("第"+clientno+"位玩家的右方物品屬性"+check[Characters[clien tno - 1].x+1][Characters[clientno - 1].y ]); 
308 Characters[clientno - 1].dir = 3; 
309 System.out.println("第"+clientno+"位玩家方向轉向右"); 
310 System.out.println("第"+clientno+"位玩家的x座標為"+Characters[clientno - 1].x); 311 System.out.println("第"+clientno+"位玩家的y座標為"+Characters[clientno - 1].y); 312 } 
313 } 
314 public synchronized int getItem(int clientno) 
315 { 
316 int tmpx,tmpy; 
317 int index = 0; 
318 int ix = 0; 
319 int iy = 0; 
320 System.out.println("第"+clientno+"位玩家在挖石頭"); 
321 System.out.println("第"+clientno+"位玩家的方向為"+Characters[clientno-1].dir); 322 System.out.println("第"+clientno+"位玩家的x座標為"+Characters[clientno - 1].x); 323 System.out.println("第"+clientno+"位玩家的y座標為"+Characters[clientno - 1].y); 324 if (Characters[clientno - 1].dir == 2 && Characters[clientno - 1].x - 1 >= 0) //left 
325 { 
326 ix = Characters[clientno - 1].x - 1; 
327 iy = Characters[clientno - 1].y; 
328 } 
329 else if (Characters[clientno - 1].dir == 0 && Characters[clientno - 1].y + 1 <= 19) //down 
330 { 
331 ix = Characters[clientno - 1].x; 
332 iy = Characters[clientno - 1].y + 1; 
333 } 
334 else if (Characters[clientno - 1].dir == 3 && Characters[clientno - 1].x + 1 <= 19) //right 
335 { 
336 ix = Characters[clientno - 1].x + 1; 
337 iy = Characters[clientno - 1].y; 
338 } 
339 else if ( Characters[clientno - 1].dir == 1 && Characters[clientno - 1].y - 1 >= 0)//up 
340 { 
341 ix = Characters[clientno - 1].x; 
342 iy = Characters[clientno - 1].y - 1; 
343 } 
344 System.out.println("第"+clientno+"位玩家挖的x座標為"+ix); 
345 System.out.println("第"+clientno+"位玩家挖的y座標為"+iy); 
346 System.out.println("第"+clientno+"位玩家挖的地點為"+check[ix][iy]); 
347 System.out.println("第"+clientno+"位玩家挖的東西為"+map[ix][iy]); 
348 check[ix][iy] = false; 
349 item = item.valueOf( item + "x"+ix + "x"+iy ); 
350 if (map[ix][iy] == 1) 
351 { //1 金礦 
352 index = map[ix][iy]; 
353 System.out.println("第"+clientno+"位玩家挖到金礦");
354 Characters[clientno - 1].money += 50 + Characters[clientno - 1 ].pick*(int) (Math.random() * 50); 
355 Characters[clientno - 1].gold += Characters[clientno - 1].gold; 
356 map[ix][iy] = 0; 
357 } 
358 else if (map[ix][iy] == 2) 
359 { //2 銀礦 
360 index = map[ix][iy]; 
361 System.out.println("第"+clientno+"位玩家挖到銀礦"); 
362 Characters[clientno - 1].money +=Characters[clientno - 1 ].pick*(int) (Math.random() * 50); 
363 Characters[clientno - 1].siliver += Characters[clientno - 1].siliver; 
364 map[ix][iy] = 0; 
365 } 
366 else if (map[ix][iy] == 3) 
367 { //3 金錢兩倍 
368 index = map[ix][iy]; 
369 System.out.println("第"+clientno+"位玩家挖到+2金"); 
370 Characters[clientno - 1].money *= 2; 
371 map[ix][iy] = 0; 
372 } 
373 else if (map[ix][iy] == 4)//4 隨機傳送至一空格處 
374 { 
375 index = map[ix][iy]; 
376 System.out.println("第"+clientno+"位玩家挖到move"); 
377 map[ix][iy] = 0; 
378 do 
379 { 
380 tmpx = (int) (Math.random()*16)+2; 
381 tmpy = (int) (Math.random()*16)+2; 
382 } 
383 while(check[tmpx][tmpy]); 
384 Characters[clientno -1].x = tmpx; 
385 Characters[clientno -1].y = tmpy; 
386 System.out.println("第"+clientno+"位玩家傳到"+tmpx+" "+tmpy); 
387 } 
388 else if (map[ix][iy] == 5) //5 金錢減半 
389 { 
390 index = map[ix][iy]; 
391 Characters[clientno - 1].money /= 2; 
392 System.out.println("第"+clientno+"位玩家挖到-2金"); 
393 map[ix][iy] = 0; 
394 } 
395 else if (map[ix][iy] == 6) //6 鎚子升級 396 { 
397 index = map[ix][iy]; 
398 System.out.println("第"+clientno+"位玩家挖到pick"); 
399 Characters[clientno -1].pick++; 
400 map[ix][iy] = 0; 
401 } 
402 else if (map[ix][iy] == 7) 
403 { //7 控制顛倒 
404 index = map[ix][iy]; 
405 System.out.println("第"+clientno+"位玩家挖到島"); 
406 if(Characters[clientno -1].mode == 1) 
407 { 
408 Characters[clientno - 1].mode--; 
409 map[ix][iy] = 0; 
410 } 
411 else 
412 { 
413 Characters[clientno - 1].mode++; 
414 map[ix][iy] = 0; 
415 } 
416 } 
417 else if (map[ix][iy] == 8)//8 均富 418 { 
419 index = map[ix][iy]; 
420 System.out.println("第"+clientno+"位玩家挖到="); 
421 map[ix][iy] = 0; 
422 int tmp = 0; 
423 for(int j=0;j<4;j++) 
424 {
425 tmp += Characters[j].money; 
426 } 
427 tmp /= 4; 
428 for(int j=0;j<4;j++) 
429 { 
430 Characters[j].money = tmp; 
431 } 
432 } 
433 System.out.println("第1位玩家錢數"+Characters[0].money); 
434 System.out.println("第2位玩家錢數"+Characters[1].money); 
435 System.out.println("第3位玩家錢數"+Characters[2].money); 
436 System.out.println("第4位玩家錢數"+Characters[3].money); 
437  
438 return index; 
439 } 
440 }
```

> **My Answer:**
> 1. 在最後 433 - 436 如果是要 print 的話，可以 wrap 成其他的 function 去呼叫。就不用寫四次
> 2. 另外還是一樣，有大量的 copy paste code 
> 3. 這中間有大量地耦合，當今天要改一個 switch 所有地方都要一起改。

可以運用多型去避免使用過多的 switch case，這樣就可以避免很多的問題。


## Take Home

### Homework - 針對 copy-paste programming 應該怎麼改（補交題，5倍分數）

```java
219 public void UpdateDirection(int clientno, int Movecode) { 
220 int tempx; 
221 int tempy; 
222 tempx = character[clientno][3]; 
223 tempy = character[clientno][4]; 
224 switch (Movecode) { 
225 case 0: 
226 character[clientno][2] = 0; 
227 break; 
228 case 1: 
229 if (cango(tempx, tempy - 10, 1, clientno)) { 
230 character[clientno][1] = 1; 
231 character[clientno][2] = 1; 
232  
233 // drawmap(tempx,tempy,clientno,1); 
234 // System.out.println("UpdateDir " + character[clientno][3] + " " + 
235 // character[clientno][4]); 
236 } 
237 break; 
238 case 3: 
239 if (cango(tempx, tempy + 10, 3, clientno)) { 
240 // drawmap(tempx,tempy,clientno,2); 
241 character[clientno][1] = 3; 
242 character[clientno][2] = 1; 
243  
244 // System.out.println(character[clientno][3] + " " + 
245 // character[clientno][4]); 
246 } 
247 break; 
248 case 4: 
249 if (cango(tempx - 10, tempy, 4, clientno)) { 
250 // drawmap(tempx,tempy,clientno,3); 
251 character[clientno][1] = 4; 
252 character[clientno][2] = 1; 
253 //System.out.println("west dir " +character[clientno][2]); 
254 // System.out.println(character[clientno][3] + " " + 
255 // character[clientno][4]); 
256 } 
257 break; 
258 case 2: 
259 if (cango(tempx + 10, tempy, 2, clientno)) { 
260 // drawmap(tempx,tempy,clientno,4); 
261 character[clientno][1] = 2; 
262 character[clientno][2] = 1; 
263 // System.out.println(character[clientno][3] + " " + 
264 // character[clientno][4]); 
265 } 
266 break; 
267 } 
268 } 
269  
270  
271 //判斷是否下一個想要走的位置可以走,可以的話回傳true,否則回傳false 
272 boolean cango(int tempx, int tempy, int move, int no) { 
273 int x1, x2, x3, x4, xx; 
274 int y1, y2, y3, y4, yy; 
275 int mapx, mapy; 
276 x1 = tempx - 30 +1; //先取出各角落的pixel值 
277 x2 = tempx - 10 +1; //用此角落的值,去做碰撞的判斷 278 x3 = tempx + 10 -1; // 加或減一,是以防碰到邊界,避免map判斷出錯
279 x4 = tempx + 30 -1; 
280 y1 = tempy - 30 +1; 
281 y2 = tempy - 10 +1; 
282 y3 = tempy + 10 -1; 
283 y4 = tempy + 30 -1; 
284 if (x1 < 0 || x4 > 600 || y1 < 0 || y4 > 600) { //邊界判定 
285 // System.out.println("because of bound"); 
286 return false; 
287 } 
288 //map 
289 switch (move) { //根據要移動的方向,去看map是否有障礙 
290 case 1: 
291 mapy = y1 / 20; //map的障礙物,用array儲存,所以用/20來取map位置
292 if (map[mapy][x1 / 20] == -1 || map[mapy][x2 / 20] == -1 || 
293 map[mapy][x3 / 20] == -1 || map[mapy][x4 / 20] == -1) { 
294 // System.out.println("because of map"); 
295 return false; 
296 } 
297 break; 
298 case 2: //往2方向的碰撞判定 299 mapx = x4 / 20; 
300 if (map[y1/20][mapx] == -1 || map[y2 / 20][mapx] == -1 || 
301 map[y3 / 20][mapx] == -1 || map[y4 / 20][mapx] == -1) { 
302 // System.out.println("because of map"); 
303 return false; 
304 } 
305 break; 
306 case 3: //往3方向的碰撞判定 307 mapy = y4 / 20; 
308 if (map[mapy][x1 / 20] == -1 || map[mapy][x2 / 20] == -1 || 
309 map[mapy][x3 / 20] == -1 || map[mapy][x4 / 20] == -1) { 
310 // System.out.println("because of map"); 
311 return false; 
312 } 
313 break; 
314 case 4: //往4方向的碰撞判定 
315 mapx = x1 / 20; 
316 if (map[y1 / 20][mapx] == -1 || map[y2 / 20][mapx] == -1 || 
317 map[y3 / 20][mapx] == -1 || map[y4 / 20][mapx] == -1) { 
318 // System.out.println("because of map"); 
319 return false; 
320 } 
321 break; 
322 } 
323 for (int z = 1; z <= 4; z++) { //去看其他腳色是否有碰撞的情況
324 yy = character[z][4]; 
325 xx = character[z][3]; 
326 if (z != no) { 
327 if ( (xx - tempx < 60 && xx - tempx > -60) && 
328 (yy - tempy < 60 && yy - tempy > -60)) { 
329 // System.out.println("because of client" + z); 
330 return false; 
331 } 
332 } 
333 } 
334 return true; 
335 } 
336 } 
```

**Refactor:**

```java
public void UpdateDirection(int clientno, int Movecode) {
    int tempx;
    int tempy;
    tempx = character[clientno][3];
    tempy = character[clientno][4];
    switch (Movecode) {
        case 0:
            character[clientno][2] = 0;
            break;
        case 1:
            if (cango(tempx, tempy - 10, 1, clientno)) {
                character[clientno][1] = 1;
                character[clientno][2] = 1;

                // drawmap(tempx,tempy,clientno,1);
                // System.out.println("UpdateDir " + character[clientno][3] + " " +
                // character[clientno][4]);
            }
            break;
        case 3:
            if (cango(tempx, tempy + 10, 3, clientno)) {
                // drawmap(tempx,tempy,clientno,2);
                character[clientno][1] = 3;
                character[clientno][2] = 1;

                // System.out.println(character[clientno][3] + " " +
                // character[clientno][4]);
            }
            break;
        case 4:
            if (cango(tempx - 10, tempy, 4, clientno)) {
                // drawmap(tempx,tempy,clientno,3);
                character[clientno][1] = 4;
                character[clientno][2] = 1;
                // System.out.println("west dir " +character[clientno][2]);
                // System.out.println(character[clientno][3] + " " +
                // character[clientno][4]);
            }
            break;
        case 2:
            if (cango(tempx + 10, tempy, 2, clientno)) {
                // drawmap(tempx,tempy,clientno,4);
                character[clientno][1] = 2;
                character[clientno][2] = 1;
                // System.out.println(character[clientno][3] + " " +
                // character[clientno][4]);
            }
            break;
    }
}

// 判斷是否下一個想要走的位置可以走,可以的話回傳true,否則回傳false
boolean cango(int tempx, int tempy, int move, int no) {
    int x1, x2, x3, x4, xx;
    int y1, y2, y3, y4, yy;
    int mapx, mapy;
    x1 = tempx - 30 + 1; // 先取出各角落的pixel值
    x2 = tempx - 10 + 1; // 用此角落的值,去做碰撞的判斷
    x3 = tempx + 10 - 1; // 加或減一,是以防碰到邊界,避免map判斷出錯
    x4 = tempx + 30 - 1;
    y1 = tempy - 30 + 1;
    y2 = tempy - 10 + 1;
    y3 = tempy + 10 - 1;
    y4 = tempy + 30 - 1;
    if (x1 < 0 || x4 > 600 || y1 < 0 || y4 > 600) { // 邊界判定
        // System.out.println("because of bound");
        return false;
    }
    // map
    switch (move) { // 根據要移動的方向,去看map是否有障礙
        case 1:
            mapy = y1 / 20; // map的障礙物,用array儲存,所以用/20來取map位置
            if (map[mapy][x1 / 20] == -1 || map[mapy][x2 / 20] == -1 ||
                    map[mapy][x3 / 20] == -1 || map[mapy][x4 / 20] == -1) {
                // System.out.println("because of map");
                return false;
            }
            break;
        case 2: // 往2方向的碰撞判定
            mapx = x4 / 20;
            if (map[y1 / 20][mapx] == -1 || map[y2 / 20][mapx] == -1 ||
                    map[y3 / 20][mapx] == -1 || map[y4 / 20][mapx] == -1) {
                // System.out.println("because of map");
                return false;
            }
            break;
        case 3: // 往3方向的碰撞判定
            mapy = y4 / 20;
            if (map[mapy][x1 / 20] == -1 || map[mapy][x2 / 20] == -1 ||
                    map[mapy][x3 / 20] == -1 || map[mapy][x4 / 20] == -1) {
                // System.out.println("because of map");
                return false;
            }
            break;
        case 4: // 往4方向的碰撞判定
            mapx = x1 / 20;
            if (map[y1 / 20][mapx] == -1 || map[y2 / 20][mapx] == -1 ||
                    map[y3 / 20][mapx] == -1 || map[y4 / 20][mapx] == -1) {
                // System.out.println("because of map");
                return false;
            }
            break;
    }
    for (int z = 1; z <= 4; z++) { // 去看其他腳色是否有碰撞的情況
        yy = character[z][4];
        xx = character[z][3];
        if (z != no) {
            if ((xx - tempx < 60 && xx - tempx > -60) &&
                    (yy - tempy < 60 && yy - tempy > -60)) {
                // System.out.println("because of client" + z);
                return false;
            }
        }
    }
    return true;
}
```

> [!TIP]
> 不要動用到物件導向，用查表法去改寫。


**After:**

```java
public void UpdateDirection(int clientno, int Movecode) {
    int[][] directions = {
        {0, 0},  // No movement
        {1, 1},  // Up
        {2, 1},  // Right
        {3, 1},  // Down
        {4, 1}   // Left
    };

    int tempx = character[clientno][3];
    int tempy = character[clientno][4];

    switch (Movecode) {
        case 0:
            character[clientno][2] = 0;
            break;
        default:
            int direction = directions[Movecode][0];
            int moveValue = directions[Movecode][1];
            if (cango(tempx + (direction == 2 ? moveValue : 0) - (direction == 4 ? moveValue : 0), 
                      tempy + (direction == 3 ? moveValue : 0) - (direction == 1 ? moveValue : 0), 
                      Movecode, 
                      clientno)) {
                character[clientno][1] = Movecode;
                character[clientno][2] = 1;
            }
            break;
    }
}

boolean cango(int tempx, int tempy, int move, int no) {
    int[][][] movements = {
        {{-30, -10, 10, 30}, {-30, -30, -30, -30}},  // No movement
        {{-30, -10, 10, 30}, {-30, -10, -10, -30}},  // Up
        {{-30, -10, 10, 30}, {10, 10, 10, 10}},      // Right
        {{-30, -10, 10, 30}, {10, 30, 30, 10}},     // Down
        {{-30, -10, 10, 30}, {-30, -30, -30, -30}}   // Left
    };

    int[] movementX = movements[move][0];
    int[] movementY = movements[move][1];

    for (int i = 0; i < 4; i++) {
        int x = tempx + movementX[i];
        int y = tempy + movementY[i];
        if (x < 0 || x > 600 || y < 0 || y > 600) {
            return false;
        }
    }

    for (int z = 1; z <= 4; z++) {
        if (z != no) {
            int xx = character[z][3];
            int yy = character[z][4];
            if (Math.abs(xx - tempx) < 60 && Math.abs(yy - tempy) < 60) {
                return false;
            }
        }
    }

    return true;
}
```


