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
28 // private int[][] characterDataBase = new int[characterNumber][characterDataBaseElement]; 
29 //characterDataBaseElement：speed，生命初始值，攻擊使別人失血量。
30 // 0 1 2 
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
44 //npc：x，y，eaten，index(clientNo = nowCharacterNum+1)。 
45 // 0 1 2 3 
46 int[] npc = { 
47 3, 6, 0, 0}; 
48 int npcElement = npc.length; 
49  
50 boolean eaten = false; 
51 static final int characterNumber = 6; //clientNo不用0，從1開始。
52 int nowCharacterNum = 0; 
53 static final int characterElement = 7; 
54 //characterElement：動物種類，dir，speed，x，y，生命值，(是1)(否0)發動攻擊。
55 // 0 1 2 3 4 5 6 
56 static public int[][] character = new int[characterNumber][characterElement]; 
57 static final int MAX_map = 30; 
58 static public int[][] map = new int[MAX_map][MAX_map]; 
59 Vector info = new Vector(); 
60 private int itemNumber = 1; //info vector 第0個為itemNumber，目前沒有用到。
61 static public Npc n1; 
62 static position p1; 
63 // DiedJudge d1; 
64  
65 public Cdc() { 
66 n1 = new Npc(this); 
67 p1 = new position(this); 
68 // d1 = new DiedJudge(this); 
69 // d1.start(); 
70 p1.start(); 
71 // n1.start(); 
72 
73 map[0][13] = map[0][14] = map[0][15] = map[0][16] = -1; 
74 map[1][13] = map[1][14] = map[1][15] = map[1][16] = -1; 
75 map[2][13] = map[2][14] = map[2][15] = map[2][16] = -1; 
76 map[10][8] = map[10][9] = map[10][10] = map[10][11] = -1; 
77 map[10][12] = map[10][17] = map[10][18] = map[10][19] = -1; 
78 map[10][20] = map[10][21] = -1; 
79 map[11][8] = map[11][9] = map[11][10] = map[11][11] = -1; 
80 map[11][12] = map[11][17] = map[11][18] = map[11][19] = -1; 
81 map[11][20] = map[11][21] = -1; 
82 map[12][8] = map[12][9] = map[12][10] = map[12][11] = -1; 
83 map[12][12] = map[12][17] = map[12][18] = map[12][19] = -1; 
84 map[12][20] = map[12][21] = -1; 
85 map[17][8] = map[17][9] = map[17][10] = map[17][11] = -1; 
86 map[17][12] = map[17][17] = map[17][18] = map[17][19] = -1; 
87 map[17][20] = map[17][21] = -1; 
88 map[18][8] = map[18][9] = map[18][10] = map[18][11] = -1; 
89 map[18][12] = map[18][17] = map[18][18] = map[18][19] = -1; 
90 map[18][20] = map[18][21] = -1; 
91 map[19][8] = map[19][9] = map[19][10] = map[19][11] = -1; 
92 map[19][12] = map[19][17] = map[19][18] = map[19][19] = -1; 
93 map[19][20] = map[19][21] = -1; 
94 map[13][0] = map[13][1] = map[13][2] = map[13][27] = -1; 
95 map[13][28] = map[13][29] = -1; 
96 map[14][0] = map[14][1] = map[14][2] = map[14][27] = -1; 
97 map[14][28] = map[14][29] = -1; 
98 map[15][0] = map[15][1] = map[15][2] = map[15][27] = -1; 
99 map[15][28] = map[15][29] = -1; 
100 map[16][0] = map[16][1] = map[16][2] = map[16][27] = -1; 
101 map[16][28] = map[16][29] = -1; 
102 map[27][13] = map[27][14] = map[27][15] = map[27][16] = -1; 
103 map[28][13] = map[28][14] = map[28][15] = map[28][16] = -1; 
104 map[29][13] = map[29][14] = map[29][15] = map[29][16] = -1; 
105 init(); 
106 } 
107  
108 public void init() { 
109 for (int i = 0; i < characterNumber; i++) 
110 for (int j = 0; j < characterElement; j++) 
111 character[i][j] = -99; 
112  
113 } 
114  
115 public void addVirtualCharacter(int clientNo, int x, int y, int animalKind) { 
116 nowCharacterNum++; 
117 character[clientNo][0] = animalKind; 
118 character[clientNo][1] = 0; 
119 character[clientNo][2] = characterDataBase[animalKind][0]; 
120 character[clientNo][3] = x; 
121 character[clientNo][4] = y; 
122 character[clientNo][5] = characterDataBase[animalKind][1]; 
123 character[clientNo][6] = 0; 
124  
125 /* for(int i=y-1; i<= y+1; i++){ 
126 for(int j=x-1; j<=x+1; j++) 
127 map[i][j] = clientNo; 
128 }*/ 
129  
130 // System.out.println("get addVirtualCharacter"); 
131 } 
132  
133  
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
149 // int itemNumber = 0; //info vector 第0個為itemNumber，目前沒有用到。
150 info.add(Integer.toString(itemNumber)); 
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
180 // System.out.println("in getUpdateInfo. npcElement is " + npcElement ); 
181 infoString = "I"; 
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
200 return info; 
201 } 
202  
203 public boolean isalive(int clientno) { 
204 if (character[clientno][5] <= 0) { 
205 // cleanDied(clientno); 
206 return false; 
207 } 
208 else 
209 return true; 
210 } 
211  
212 /** public static void startgame() { //lucianna:？這裡有用嗎？ 
213 //call UDP 
214 // System.out.println("position"); 
215 u1.startUDPBroadCast(); 
216  
217 }*/ 
218 
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
277 x2 = tempx - 10 +1; //用此角落的值,去做碰撞的判斷 
278 x3 = tempx + 10 -1; // 加或減一,是以防碰到邊界,避免map判斷出錯
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
298 case 2: //往2方向的碰撞判定 
299 mapx = x4 / 20; 
300 if (map[y1/20][mapx] == -1 || map[y2 / 20][mapx] == -1 || 
301 map[y3 / 20][mapx] == -1 || map[y4 / 20][mapx] == -1) { 
302 // System.out.println("because of map"); 
303 return false; 
304 } 
305 break; 
306 case 3: //往3方向的碰撞判定 
307 mapy = y4 / 20; 
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
337 
```
