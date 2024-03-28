```java
1 package cdc; 
2  
3 import java.lang.String; 
4 import java.util.*; 
5 import javax.swing.*; 
6 import java.awt.*; 
7 import java.awt.event.*; 
8  
9 public class CDC 
10 { 
11 public String s, s1; 
12 public String s2[][] = new String[20][20]; 
13 public VirtualCharacter Characters[] = new VirtualCharacter[4]; 
14 public int inputx[] = new int[2]; 
15 public int inputy[] = new int[2]; 
16 public int inputgold[] = new int[3]; 
17 public int inputsiliver[] = new int[3]; 
18 public int inputmoney[] = new int[5]; 
19 public int inputpick[] = new int[3]; 
20 public int inputmode[] = new int[1]; 
21 int players; 
22 public boolean check[][] = new boolean[20][20]; 
23 public int map[][] = new int[20][20]; 
24 public int tempx,tempy,tempgold,tempsiliver,tempmoney,temppick; 
25 public int i1,i2,i3,i4,i5,i6,i7,i8; 
26 public int judge = 0; 
27 public String temp; 
28 public String item = "x0x0"; 
29  
30 Vector v = new Vector(); 
31  
32 public CDC() 
33 { 
34 s = "8";//判斷字元 
35 i1 = i2 = i3 = i4 = i5 = i6 = i7 = i8 = 0; 
36 players = 0;//玩家人數 
37 for (int j = 0; j < 20; j++)//initialize 所有物品 
38 { 
39 for (int k = 0; k < 20; k++) 
40 { 
41 check[j][k] = true;//預設true可挖false已挖 
42 int rand; 
43 rand = (int) (Math.random() * 8) + 1; //rand = 1~8共八項物品
44 if ( rand == 1 && i1 > 171 )//限制金礦個數 ＝ 171 
45 { 
46 k--; 
47 continue; 
48 } 
49 else if ( rand == 1 && i1 <= 171 ) 
50 i1++; 
51 if ( rand == 2 && i2 > 200 )//限制銀礦個數 ＝ 200 
52 { 
53 k--; 
54 continue; 
55 } 
56 else if ( rand == 2 && i2 <= 200 ) 
57 i2++; 
58 if ( rand == 3 && i3 > 5 )//限制+2金個數 ＝ 5 
59 { 
60 k--; 
61 continue; 
62 } 
63 else if ( rand == 3 && i3 <= 5 ) 
64 i3++; 
65 if ( rand == 4 && i4 > 4 )//限制瞬間移動個數 ＝ 4 
66 { 
67 k--; 
68 continue; 
69 } 
70 else if ( rand == 4 && i4 <= 4 ) 
71 i4++; 
72 if ( rand == 5 && i5 > 5 )//限制-2金個數 ＝ 4 
73 {
74 k--; 
75 continue; 
76 } 
77 else if ( rand == 5 && i5 <= 5 ) 
78 i5++; 
79 if ( rand == 6 && i6 > 8 )//限制捶子個數 ＝ 8 
80 { 
81 k--; 
82 continue; 
83 } 
84 else if ( rand == 6 && i6 <= 8 ) 
85 i6++; 
86 if ( rand == 7 && i7 > 8 )//限制金礦個數 ＝ 171 
87 { 
88 k--; 
89 continue; 
90 } 
91 else if ( rand == 7 && i7 <= 8 ) 
92 i7++; 
93 if ( rand == 8 && i3 > 5 )//限制均富個數 ＝ 8 
94 { 
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
137 public Vector update() 
138 { 
139 s1 = "R"; 
140 temp = ""; 
141 if (judge == 0) 
142 { 
143 v.clear(); 
144 v.addElement(s); 
145 } 
146 else if (judge == 1)
147 { 
148 for (int i = 0; i < 4; i++) 
149 { 
150 tempx = Characters[i].x; 
151 tempy = Characters[i].y; 
152 tempgold = Characters[i].gold; 
153 tempsiliver = Characters[i].siliver; 
154 temppick = Characters[i].pick; 
155 tempmoney = Characters[i].money; 
156 if (Characters[i] != null) 
157 { 
158 for (int p = 1; p >= 0; p--) 
159 { 
160 inputx[p] = Characters[i].x % 10; 
161 inputy[p] = Characters[i].y % 10; 
162 Characters[i].x /= 10; 
163 Characters[i].y /= 10; 
164 } 
165 for (int q = 2; q >= 0; q--) 
166 { 
167 inputgold[q] = Characters[i].gold % 10; 
168 inputgold[q] = Characters[i].siliver % 10; 
169 inputpick[q] = Characters[i].pick % 10; 
170 Characters[i].gold /= 10; 
171 Characters[i].siliver /= 10; 
172 Characters[i].pick /= 10; 
173 } 
174 for (int t = 4; t >= 0; t--) 
175 { 
176 inputmoney[t] = Characters[i].money % 10; 
177 Characters[i].money /= 10; 
178 } 
179 inputmode[0] = Characters[i].mode; 
180 s1=s1.valueOf(s1+(i+1)+Characters[i].pic+inputx[0]+inputx[1]+ 
81 inputy[0]+inputy[1]+Characters[i].dir+inputgold[0]+ 
182 inputgold[1]+inputgold[2]+inputsiliver[0]+ 
183 inputsiliver[1]+inputsiliver[2]+inputmoney[0]+ 
184 inputmoney[1]+inputmoney[2]+inputmoney[3]+inputmoney[4]+ 
185 inputpick[0]+inputpick[1]+inputpick[2]+inputmode[0]); 
186 } 
187 Characters[i].x = tempx; 
188 Characters[i].y = tempy; 
189 Characters[i].gold = tempgold; 
190 Characters[i].siliver = tempsiliver; 
191 Characters[i].money = tempmoney; 
192 Characters[i].pick = temppick; 
193 } 
194 s1 = s1.valueOf(s1 + "M" + item); 
195 v.clear(); 
196 v.addElement(s1); 
197 } 
198 if (judge == 0 && players >= 4 ) 
199 { 
200 judge = 1; 
201 } 
202 return v; 
203 } 
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
243 public synchronized void updateDirection(int clientno, int MoveCode) 
244 { 
245 if (MoveCode == 1 && Characters[clientno - 1].y - 1 >= 0) 
246 { //up and walk 
247 Characters[clientno - 1].y = Characters[clientno - 1].y - 1; 
248 System.out.println("第"+clientno+"位玩家方向向上走"); 
249 System.out.println("第"+clientno+"位玩家的x座標為"+Characters[clientno - 1].x); 
250 System.out.println("第"+clientno+"位玩家的y座標為"+Characters[clientno - 1].y); 
251 Characters[clientno - 1].dir = 1; 
252 } 
253 else if (MoveCode == 0 && Characters[clientno - 1].y + 1 <= 19) 
254 { //down and walk 
255 Characters[clientno - 1].y = Characters[clientno - 1].y + 1; 
256 System.out.println("第"+clientno+"位玩家方向向下走"); 
257 System.out.println("第"+clientno+"位玩家的x座標為"+Characters[clientno - 1].x); 
258 System.out.println("第"+clientno+"位玩家的y座標為"+Characters[clientno - 1].y); 
259 Characters[clientno - 1].dir = 0; 
260 } 
261 else if (MoveCode == 2 && Characters[clientno - 1].x - 1 >= 0) 
262 { //left and walk 
263 Characters[clientno - 1].x = Characters[clientno - 1].x - 1; 
264 System.out.println("第"+clientno+"位玩家方向向左走"); 
265 System.out.println("第"+clientno+"位玩家的x座標為"+Characters[clientno - 1].x); 
266 System.out.println("第"+clientno+"位玩家的y座標為"+Characters[clientno - 1].y); 
267 Characters[clientno - 1].dir = 2; 
268 } 
269 else if (MoveCode == 3 && Characters[clientno - 1].x + 1 <=19) 
270 { //right and walk 
271 Characters[clientno - 1].x = Characters[clientno - 1].x + 1; 
272 System.out.println("第"+clientno+"位玩家方向向右走"); 
273 System.out.println("第"+clientno+"位玩家的x座標為"+Characters[clientno - 1].x); 
274 System.out.println("第"+clientno+"位玩家的y座標為"+Characters[clientno - 1].y); 
275 Characters[clientno - 1].dir = 3; 
276 } 
277 else if (MoveCode == 6 )//up and turn 
278 { 
279 if ( Characters[clientno - 1].y != 0 ) 
280 System.out.println("第"+clientno+"位玩家的上方物品屬性"+check[Characters[clien tno - 1].x][Characters[clientno - 1].y -1]); 
281 Characters[clientno - 1].dir = 1; 
282 System.out.println("第"+clientno+"位玩家方向轉向上"); 
283 System.out.println("第"+clientno+"位玩家的x座標為"+Characters[clientno - 1].x); 
284 System.out.println("第"+clientno+"位玩家的y座標為"+Characters[clientno - 1].y); 
285 } 
286 else if (MoveCode == 7 )//down and turn 
287 { 
288 if ( Characters[clientno - 1].y != 19 ) 
289 System.out.println("第"+clientno+"位玩家的下方物品屬性"+check[Characters[clientno - 1].x][Characters[clientno - 1].y + 1]); 
290 Characters[clientno - 1].dir = 0; 
291 System.out.println("第"+clientno+"位玩家方向轉向下"); 
292 System.out.println("第"+clientno+"位玩家的x座標為"+Characters[clientno - 1].x); 
293 System.out.println("第"+clientno+"位玩家的y座標為"+Characters[clientno - 1].y); 
294 } 
295 else if (MoveCode == 8 )//left 
296 { 
297 if (Characters[clientno - 1].x != 0 ) 
298 System.out.println("第"+clientno+"位玩家的左方物品屬性"+check[Characters[clien tno - 1].x-1][Characters[clientno - 1].y ]); 
299 Characters[clientno - 1].dir = 2; 
300 System.out.println("第"+clientno+"位玩家方向轉向左"); 
301 System.out.println("第"+clientno+"位玩家的x座標為"+Characters[clientno - 1].x); 
302 System.out.println("第"+clientno+"位玩家的y座標為"+Characters[clientno - 1].y); 
303 } 
304 else if (MoveCode == 9 )//right 
305 { 
306 if (Characters[clientno - 1].x != 19) 
307 System.out.println("第"+clientno+"位玩家的右方物品屬性"+check[Characters[clien tno - 1].x+1][Characters[clientno - 1].y ]); 
308 Characters[clientno - 1].dir = 3; 
309 System.out.println("第"+clientno+"位玩家方向轉向右"); 
310 System.out.println("第"+clientno+"位玩家的x座標為"+Characters[clientno - 1].x); 
311 System.out.println("第"+clientno+"位玩家的y座標為"+Characters[clientno - 1].y); 
312 } 
313 } 
314 public synchronized int getItem(int clientno) 
315 { 
316 int tmpx,tmpy; 
317 int index = 0; 
318 int ix = 0; 
319 int iy = 0; 
320 System.out.println("第"+clientno+"位玩家在挖石頭"); 
321 System.out.println("第"+clientno+"位玩家的方向為"+Characters[clientno-1].dir); 
322 System.out.println("第"+clientno+"位玩家的x座標為"+Characters[clientno - 1].x); 
323 System.out.println("第"+clientno+"位玩家的y座標為"+Characters[clientno - 1].y); 
324 if (Characters[clientno - 1].dir == 2 && Characters[clientno - 1].x - 1 >= 0) //left 
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
395 else if (map[ix][iy] == 6) //6 鎚子升級 
396 { 
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
417 else if (map[ix][iy] == 8)//8 均富 
418 { 
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
