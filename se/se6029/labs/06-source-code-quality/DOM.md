```java
1 /* 
2 * DOM.java 
3 * 
4 * Created on 2003年12月21日, 上午 12:36 
5 */ 
6  
7 package dom; 
8 import sounds.*; 
9 import tcpcm.*; 
10 import java.awt.*; 
11 /** 
12 * 
13 * @author Administrator 
14 */ 
15 public class DOM { 
16 ClientServer object; 
17 public int self_clientno=0; //連進來的順續 
18 public VirtualCharacter Characters[]=new VirtualCharacter[4]; 
19 boolean char_choosed[]; 
20 public int map[][]=new int [20][20]; 
21 /** 0表示沒磚塊 1表示有 **/ 
22 public VirtualCharacter com[]=new VirtualCharacter[3]; 
23  
24 public DOM(ClientServer ob1) 
25 { 
26 char_choosed=new boolean [9]; 
27 object = ob1; 
28 for(int j=0;j<20;j++){ 
29 for(int k=0;k<20;k++) 
30 map[j][k] = 1; 
31 } 
32 map[0][0] = 0; 
33 map[0][1] = 0; 
34 map[1][0] = 0; 
35 map[19][0] = 0; 
36 map[19][1] = 0; 
37 map[18][0] = 0; 
38 map[0][19] = 0; 
39 map[1][19] = 0; 
40 map[0][18] = 0; 
41 map[19][19] = 0; 
42 map[19][18] = 0; 
43 map[18][19] = 0; 
44 map[9][9] = 0; 
45 map[9][10] = 0; 
46 map[10][9] = 0; 
47 map[10][10] = 0; 
48 } 
49 public void choose_role(int clientno,int pic){//正如的 
50 addVirtualCharacter(clientno,pic); 
51 char_choosed[pic]=true; 
52 } 
53 public boolean[] decide_role(){//虹安的 
54 return char_choosed; 
55 } 
56 public synchronized void update_map(int x,int y) 
57 { 
58 map[x][y]=0; 
59 } 
60 public void addVirtualCharacter(int clientno,int pic){ 
61 Characters[clientno-1]=new VirtualCharacter(clientno,pic); 
62 switch(clientno){ 
63 case 1: 
64 Characters[clientno-1].x=0; 
65 Characters[clientno-1].y=0; 
66 break; 
67 case 2: 
68 Characters[clientno-1].x=19; 
69 Characters[clientno-1].y=0; 
70 break; 
71 case 3: 
72 Characters[clientno-1].x=0; 
73 Characters[clientno-1].y=19;
74 break; 
75 case 4: 
76 Characters[clientno-1].x=19; 
77 Characters[clientno-1].y=19; 
78 break; 
79 } 
80 System.out.println("client "+clientno+" get"); 
81 } 
82 public synchronized void updateVirtualCharacter(int clientno,int x,int y,int dir,int money,int pick,int mod){ 
83 Characters[clientno-1].dir=dir; 
84 Characters[clientno-1].x=x; 
85 Characters[clientno-1].y=y; 
86 Characters[clientno-1].money=money; 
87 Characters[clientno-1].pick=pick; 
88 Characters[clientno-1].mod=mod; 
89 //更新錢數同時更新status裡面的錢數 (updateMoney) 
90 } 
91 public VirtualCharacter getVirtualCharacterXY(){ 
92 return Characters[self_clientno-1]; 
93 } 
94 public void set_clientno(){ 
95 self_clientno=object.Clientnoget(); 
96 System.out.println("我的編號"+self_clientno+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~`"); 
97 } 
98 public VirtualCharacter[] getvc(){ 
99 //System.out.println("DOM role"+Characters); 
100  
101 return Characters; 
102 } 
103 public boolean[][] getMAP(){ 
104 boolean data[][] = new boolean[20][20]; 
105 for (int a = 0; a < 20; a++) { 
106 for (int b = 0; b < 20; b++) { 
107 //System.out.print(map[a][b]); 
108 if (map[a][b] == 1) 
109 data[a][b] = true; 
110 else 
111 data[a][b] = false; 
112 } 
113 //System.out.println("DOM map"+a); 
114 } 
115 return data; 
116 } 
117 public void decide(int key) 
118 { 
119 int press = key; 
120 System.out.println(key); 
121 VirtualCharacter loc=getVirtualCharacterXY(); 
122 if(loc.mod==1) //左右顛倒的道具 
123 { 
124 if(key==37) 
125 press=39; 
126 else if(key==39) 
127 press=37; 
128 else if(key==38) 
129 press=40; 
130 else if(key==40) 
131 press=38; 
132 } 
133 //1向上走0向下走2向左走3向右走 
134 //6轉向上7轉向下8轉向左9轉向右 方向性 
135 switch(press) 
136 { 
137 case 37: 
138 if(loc.x-1>=0) //左 
139 { 
140 if(map[loc.x-1][loc.y]==0) 
141 { 
142 object.inputMoves(2); 
143 System.out.println("角色" + self_clientno + "座標" +
144 Characters[self_clientno - 1].x + " " + 
145 Characters[self_clientno - 1].y + "方向" + 
146 Characters[self_clientno - 1].dir); 
147 System.out.println("角色向左走"); 
148 } 
149 else 
150 { 
151 object.inputMoves(8); 
152 System.out.println("角色" + self_clientno +"座標"+Characters[self_clientno -1].x+" "+Characters[self_clientno -1].y+"方向" + Characters[self_clientno-1].dir); 
153 System.out.println("角色向左轉"); 
154 new sounds(1); 
155 } 
156 } 
157 else 
158 { 
159 object.inputMoves(8); 
160 System.out.println("角色" + self_clientno +"座標"+Characters[self_clientno -1].x+" "+Characters[self_clientno -1].y+"方向" + Characters[self_clientno-1].dir); 
161 System.out.println("角色向左轉"); 
162 new sounds(1); 
163 } 
164 break; 
165 case 38:if(loc.y-1>=0) //上 
166 { 
167 if(map[loc.x][loc.y-1]==0) 
168 { 
169 object.inputMoves(1); 
170 System.out.println("角色" + self_clientno + "座標" + 
171 Characters[self_clientno - 1].x + " " + 
172 Characters[self_clientno - 1].y + "方向" + 
173 Characters[self_clientno - 1].dir); 
174 System.out.println("角色向上走"); 
175 } 
176 else{ 
177 object.inputMoves(6); 
178 System.out.println("角色" + self_clientno +"座標"+Characters[self_clientno -1].x+" "+Characters[self_clientno -1].y+"方向" + Characters[self_clientno-1].dir); 
179 System.out.println("角色向下上轉"); 
180 new sounds(1); 
181 } 
182 } 
183 else 
184 { 
185 object.inputMoves(6); 
186 System.out.println("角色" + self_clientno +"座標"+Characters[self_clientno -1].x+" "+Characters[self_clientno -1].y+"方向" + Characters[self_clientno-1].dir); 
187 System.out.println("角色向下上轉"); 
188 new sounds(1); 
189 } 
190 break; 
191 case 39:if(loc.x+1<=19) //右 
192 { 
193 if(map[loc.x+1][loc.y]==0) 
194 { 
195 object.inputMoves(3); 
196 System.out.println("角色" + self_clientno + "座標" + 
197 Characters[self_clientno - 1].x + " " + 
198 Characters[self_clientno - 1].y + "方向" + 
199 Characters[self_clientno - 1].dir); 
200 System.out.println("角色向右走"); 
201 } 
202 else 
203 { 
204 object.inputMoves(9); 
205 System.out.println("角色" + self_clientno + "座標" + 
206 Characters[self_clientno - 1].x + " " + 
207 Characters[self_clientno - 1].y + "方向" + 
208 Characters[self_clientno - 1].dir);
209 System.out.println("角色向右轉"); 
210 new sounds(1); 
211 } 
212 } 
213 else 
214 { 
215 object.inputMoves(9); 
216 System.out.println("角色" + self_clientno +"座標"+Characters[self_clientno -1].x+" "+Characters[self_clientno -1].y+"方向" + Characters[self_clientno-1].dir); 
217 System.out.println("角色向右轉"); 
218 new sounds(1); 
219 } 
220 break; 
221 case 40:if(loc.y+1<=19) //下 
222 { 
223 if(map[loc.x][loc.y+1]==0) 
224 { 
225 object.inputMoves(0); 
226 System.out.println("角色" + self_clientno + "座標" + 
227 Characters[self_clientno - 1].x + " " + 
228 Characters[self_clientno - 1].y + "方向" + 
229 Characters[self_clientno - 1].dir); 
230 System.out.println("角色向下走"); 
231 } 
232 else 
233 { 
234 object.inputMoves(7); 
235 System.out.println("角色" + self_clientno + "座標" + 
236 Characters[self_clientno - 1].x + " " + 
237 Characters[self_clientno - 1].y + "方向" + 
238 Characters[self_clientno - 1].dir); 
239 System.out.println("角色向下轉"); 
240 new sounds(1); 
241 } 
242 } 
243 else 
244 { 
245 object.inputMoves(7); 
246 System.out.println("角色" + self_clientno +"座標"+Characters[self_clientno -1].x+" "+Characters[self_clientno -1].y+"方向" + Characters[self_clientno-1].dir); 
247 System.out.println("角色向下轉"); 
248 new sounds(1); 
249 } 
250 break; 
251 case 8:if(loc.dir==1) // 上 
252 { 
253 if(loc.y-1>=0) 
254 { 
255 if (map[loc.x][loc.y - 1] == 1) 
256 { 
257 object.inputMoves(press-3); 
258 map[loc.x][loc.y - 1] =0; 
259 System.out.println("角色" + self_clientno +"座標"+Characters[self_clientno -1].x+"  "+Characters[self_clientno -1].y+"方向" + Characters[self_clientno-1].dir); 
260 System.out.println("角色向上挖"); 
261 new sounds(0); 
262 } 
263 } 
264 } 
265 else if(loc.dir==0) //下 
266 { 
267 if (loc.y + 1 <= 19) { 
268 if (map[loc.x][loc.y + 1] == 1) 
269 { 
270 object.inputMoves(press-3); 
271 map[loc.x][loc.y + 1] = 0; 
272 System.out.println("角色" + self_clientno +"座標"+Characters[self_clientno -1].x+"  "+Characters[self_clientno -1].y+"方向" +Characters[self_clientno-1].dir); 
273 System.out.println("角色向下挖"); 
274 new sounds(0); 
275 } 
276 } 
277 } 
278 else if(loc.dir==2) //左 
279 { 
280 if(loc.x-1>=0) 
281 { 
282 if(map[loc.x-1][loc.y]==1) 
283 { 
284 object.inputMoves(press-3); 
285 map[loc.x-1][loc.y]=0; 
286 System.out.println("角色" + self_clientno +"座標"+Characters[self_clientno -1].x+"  "+Characters[self_clientno -1].y+"方向" + Characters[self_clientno-1].dir); 
287 System.out.println("角色向左挖"); 
288 new sounds(0); 
289 } 
290 } 
291 } 
292 else if(loc.dir==3) //右 
293 { 
294 if(loc.x+1<=19) 
295 { 
296 if(map[loc.x+1][loc.y]==1) 
297 { 
298 object.inputMoves(press-3); 
299 map[loc.x+1][loc.y]=0; 
300 System.out.println("角色" + self_clientno +"座標"+Characters[self_clientno -1].x+"  "+Characters[self_clientno -1].y+"方向" + Characters[self_clientno-1].dir); 
301 System.out.println("角色向右挖"); 
302 new sounds(0); 
303 } 
304 } 
305 } 
306 } 
307 } 
308 public boolean decide_end() //傳true表示遊戲結束 
309 { 
310 for(int a=0;a<20;a++) 
311 { 
312 for(int b=0;b<20;b++) 
313 { 
314 System.out.print(map[a][b]); 
315 if(map[a][b]==1){ 
316 return false; 
317 } 
318 } 
319 } 
320 System.out.println(""); 
321 return true; 
322 } 
323 public VirtualCharacter[] returnCom() { 
324 int count=0; 
325 for (int i=0;i<4;i++) { 
326 if (i!=(self_clientno-1)) { 
327 com[count]=Characters[i]; 
328 count++; 
329 } 
330 } 
331 return com; 
332 } 
333 public int myself() { 
334 return self_clientno; 
335 } 
336 } 
337 
```
