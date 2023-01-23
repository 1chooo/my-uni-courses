TITLE MASM Final Project
; ASCII Table
; http://www.theasciicode.com.ar/extended-ascii-code/block-graphic-character-ascii-code-219.html

INCLUDE Irvine32.inc

; 新定義的座標Structure
COORDINATE STRUCT
	X BYTE ?
	Y BYTE ?
COORDINATE ENDS

.DATA
; Constant 用數字來代替
	UP = 1
	DOWN = 2
	LEFT = 3
	RIGHT = 4
	
	ROW =  24
	COLUMN = 80

;Variables 變數們	
	snake BYTE 254				;蛇的點點 ASCII
	appleChar BYTE 162			;Apple ASCII
	speed DWORD 100				;毫秒

	currentDirection BYTE RIGHT
	currentX BYTE ?
	currentY BYTE ?

	snakeMax = 1276					;22*78 = 1716 蛇不能太長
	snakeLength WORD 10				;蛇的初始長度
	snakeBody COORDINATE SnakeMax DUP(<0,0>)	; 蛇身的陣列座標
	snakeHead COORDINATE <>						; 蛇頭座標
	snakeTail COORDINATE <>						; 蛇尾座標
	apple COORDINATE <>							; 蘋果座標
	tempX BYTE ?
	tempY BYTE ?
	hit	BYTE 0h 								; 是否碰撞 Boolean 

	score WORD 0h 								; 存放分數
	scoreString BYTE "Score:",0
	speedString BYTE "Speed:",0
	speed_1 BYTE "Slow",0
	speed_2 BYTE "Oops!",0
	speed_3 BYTE "Fast",0
	speed_4 BYTE "Faster",0
	speed_5 BYTE "Crazy",0
	speed_meh BYTE "Medium",0


.CODE
main PROC

Initialization:	
	call splashScreen ; 初始畫面(按Enter)
	mov eax,0h						
	mov edx,0h
	mov ecx,0h

	call initializeSnake ; 蛇初始化
	call drawWalls ; 牆 畫一次就好
	call appleManager ; 蘋果初始化

	; 移動游標到中間
	mov dh, (ROW-2)/2
	mov dl, (COLUMN-2)/2
	call gotoXY	

; 遊戲迴圈 無限循環
gameLoop:
	mov ecx,999
	call drawScoreAndSpeed 	; 畫當前分數跟跟速度
	call changeSpeed		; 根據分數改變速度
	call handleDirection	; 改變蛇頭的方向
	call moveSnake			; 移動蛇
	call drawSnake			; 畫蛇
	call drawApple			; 畫蘋果
	call eatApple			; 如果吃到蘋果增長
	call checkCollision		; 檢查是否撞到牆或自己 回傳hit值
	.IF hit==1
		mov eax, 550
		call delay
		jmp finishGame
	.ENDIF
	
	; delay 可以暫停程式的執行狀態
	mov eax, speed
	call delay	
loop gameLoop

finishGame:
	call gameOverScreen

exit
main ENDP

;;; 下面一堆 PROC

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
; 蛇蛇初始化
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
initializeSnake PROC
	mov currentX, (ROW-2)/2
	mov currentY, (COLUMN-2)/2

	mov cx, snakeLength
	mov edi, 0
snakeIni:
	mov al, currentX
	mov (COORDINATE PTR snakeBody[edi]).X, al
	mov al, currentY
	mov (COORDINATE PTR snakeBody[edi]).Y, al
	
	.IF cx==1
		mov al, currentX
		mov snakeTail.X, al
		mov al, currentY
		mov snakeTail.Y, al
	.ENDIF
	.IF cx==snakeLength
		mov al, currentX
		mov snakeHead.X, al
		mov al, currentY
		mov snakeHead.Y, al
	.ENDIF
	add edi, TYPE COORDINATE
	dec currentY
loop snakeIni

ret
initializeSnake ENDP

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
; 控制蛇面對的方向 : readKey 無緩衝輸入
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

handleDirection PROC uses eax
	call readKey
	.IF ah==72 && currentDirection!=DOWN
	mov currentDirection, UP
	jmp exitFunction
		.ELSEIF ah==77 && currentDirection!=LEFT
		mov currentDirection, RIGHT
		jmp exitFunction
			.ELSEIF ah==80 && currentDirection!=UP
			mov currentDirection, DOWN
			jmp exitFunction
				.ELSEIF ah==75 && currentDirection!=RIGHT
				mov currentDirection, LEFT
exitFunction:
	.ENDIF
ret
handleDirection ENDP

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
; 畫牆 只畫一次
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
drawWalls PROC uses edx
	mov eax, 0h
	call gotoXY
	mov ecx, COLUMN
drawTop:
	mov al,203		;ASCII
	call writeChar
loop drawTop

	mov dh, ROW
	mov dl, 0
	call gotoXY
	mov ecx, COLUMN
drawBottom:
	mov al,202		;ASCII
	call writeChar
loop drawBottom

	mov edx,0h
	call gotoXY
	mov ecx,ROW
drawLeft:
	mov al,204
	call writeChar
	call crlf	
loop drawLeft

	mov dh, 0h
	mov dl, COLUMN-1
	call gotoXY
	mov ecx,ROW
drawRight:
	mov al,185
	call writeChar
	inc dh
	call gotoXY
loop drawRight	

ret
drawWalls ENDP


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
; 蛇會自動移動一格
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
moveSnake PROC uses eax ecx edi
;暫存蛇尾座標
	mov al, snakeTail.X
	mov tempX, al
	mov al, snakeTail.Y
	mov tempY, al

;從蛇長算 存蛇身座標
	mov cx, snakeLength
	sub cx, 1

	;(SnakeLength-2)*2
	mov ax, snakeLength
	sub ax, 2			;-1 to correct for zero correction, another -1 to get the second last element
	shl ax, 1			; 乘2 ; 因為 TYPE COORD = 2

	mov di, ax
pushCoord:
	mov ax, snakeBody[di]
	mov snakeBody[di+2], ax

	sub di, 2
loop pushCoord

.IF currentDirection == RIGHT
	mov al, snakeHead.X
	mov (snakeBody[0]).X, al
	mov snakeHead.X, al

	mov al, snakeHead.Y
	inc al
	mov (snakeBody[0]).Y, al
	mov snakeHead.Y, al
.ENDIF

.IF currentDirection == LEFT
	mov al, snakeHead.X
	mov (snakeBody[0]).X, al
	mov snakeHead.X, al

	mov al, snakeHead.Y
	dec al
	mov (snakeBody[0]).Y, al
	mov snakeHead.Y, al
.ENDIF

.IF currentDirection == UP
	mov al, snakeHead.X
	dec al
	mov (snakeBody[0]).X, al
	mov snakeHead.X, al

	mov al, snakeHead.Y
	mov (snakeBody[0]).Y, al
	mov snakeHead.Y, al
.ENDIF

.IF currentDirection == DOWN
	mov al, snakeHead.X
	inc al
	mov (snakeBody[0]).X, al
	mov snakeHead.X, al

	mov al, snakeHead.Y
	mov (snakeBody[0]).Y, al
	mov snakeHead.Y, al
.ENDIF

;把舊的蛇尾換成空白
	mov dh, tempX
	mov dl, tempY
	call gotoXY
	mov al, ' '
	call writeChar

;重設新尾巴
	; (snakeLength-1)*2
	mov di, snakeLength
	sub di, 1
	shl di, 1

	mov bl, snakeBody[di].X
	mov bh, snakeBody[di].Y

	mov snakeTail.X, bl
	mov snakeTail.Y, bh

ret
moveSnake ENDP

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
; 把蛇畫出來
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
drawSnake PROC uses ecx eax
	mov cx, snakeLength
	mov edi, 0
	mov edx, 0
drawingLoop:
	mov al, snakeBody[edi].X
	mov tempX, al

	mov al, snakeBody[edi].Y
	mov tempY, al

	.IF tempX!=0 && tempY!=0		
		mov dh, tempX
		mov dl, tempY
		call gotoXY

		mov al, snake
		call writeChar
	.ENDIF
	add edi, TYPE COORDINATE
loop drawingLoop

ret
drawSnake ENDP

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
; 控制&畫 Apple 
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
appleManager PROC
	mov eax, ROW-1
	call randomRange	; 0 ~ (ROW-1)-1
	inc eax				; 1 ~ (ROW-1) : 蘋果不能在牆上
	mov apple.X, al

	mov eax, COLUMN-1
	call randomRange
	inc eax
	mov apple.Y, al

ret
appleManager ENDP


drawApple PROC uses edx eax
	mov dh, apple.X
	mov dl, apple.Y
	call gotoXY

	mov eax, lightRed+(black*16)
	call setTextColor

	mov al, appleChar
	call writeChar

; 畫完蘋果後 要把顏色還原成白字
	mov eax, white+(black*16)
	call setTextColor
ret
drawApple ENDP

eatApple PROC
	mov dh, snakeHead.X
	mov dl, snakeHead.Y
COMMENT $
	.IF dh==apple.X && dl==apple.Y
		add score,8
		call appleManager
		inc snakeLength
	.ENDIF
$

	cmp dh, apple.X
	jne safeExit
	cmp dl, apple.Y
	jne safeExit
		add score,8
		call appleManager
		inc snakeLength
safeExit:
ret 
eatApple ENDP

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
; 碰撞偵測
; Store decision in bl which can be used to end the game
; hit : 0 = OK, 1 = Hit
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
checkCollision PROC
	mov dh, snakeHead.X
	mov dl, snakeHead.Y
COMMENT $
	.IF dl==0 || dh==0 || dh==ROW || dl==COLUMN-1
		mov bl,1
		mov hit,bl
	.ENDIF
$

	or dl,dl
	je doThis
	or dh,dh
	je doThis
	cmp dh, ROW
	je doThis
	cmp dl, COLUMN-1h
	jne didntMakeIt

doThis:
	mov bl,1
	mov hit,bl

didntMakeIt:	

;檢查是否撞到自己
	mov edi,2
	mov cx, snakeLength
	dec cx
hitItself:
COMMENT $
	.IF dh==snakeBody[edi].X && dl==snakeBody[edi].Y
		mov bl,1
		mov hit,bl
	.ENDIF
$

	cmp dh, snakeBody[edi].X
	jne nextStep
	cmp dl, snakeBody[edi].Y
	jne nextStep
		mov bl,1
		mov hit, bl
	
nextStep:
	add edi, TYPE COORDINATE
loop hitItself

safe:	
ret
checkCollision ENDP

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
; 根據分數改變速度
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
changeSpeed PROC uses eax
	.IF score==48
		mov eax, 90
		mov speed, eax
	.ELSEIF score==80
		mov eax, 80
		mov speed, eax
	.ELSEIF score==128
		mov eax, 70
		mov speed, eax
	.ELSEIF score==160
		mov eax, 50
		mov speed, eax
	.ELSEIF score==200
		mov eax, 40
		mov speed, eax
	.ENDIF

ret
changeSpeed ENDP

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
; Draw Score And Speed
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
drawScoreAndSpeed PROC

; 分數
	mov dh, 1
	mov dl, 70
	call gotoXY
	mov edx, OFFSET scoreString
	call writeString

	mov dh, 1
	mov dl, 76
	call gotoXY
	mov ax, score
	call writeDec

; 速度
	mov dh, 1
	mov dl, 1
	call gotoXY
	mov edx, OFFSET speedString
	call writeString

	mov dh, 1
	mov dl, 7
	call gotoXY
	
	.IF score<48
		mov edx, OFFSET speed_1
		call writeString
	.ELSEIF score>=48 && score<80
		mov edx, OFFSET speed_meh
		call writeString
	.ELSEIF score>=80 && score<128
		mov edx, OFFSET speed_2
		call writeString
	.ELSEIF score>=128 && score<160
		mov edx, OFFSET speed_3
		call writeString
	.ELSEIF score>=160 && score<200
		mov edx, OFFSET speed_4
		call writeString
	.ELSEIF score>200
		mov edx, OFFSET speed_5
		call writeString
	.ENDIF

ret
drawScoreAndSpeed ENDP

.data

splash BYTE "Snake!",0
ourNames BYTE "MASM Final Project",0
start BYTE "Start Game", 0


.code
splashScreen PROC
	call clrscr

	mov eax, yellow+(black*16)
	call setTextColor

	mov dh, 10
	mov dl, 24
	call gotoXY
	mov edx, OFFSET splash
	call writeString

	mov dh, 12
	mov dl, 24
	call gotoXY
	mov edx, OFFSET ourNames
	call writeString

	mov dh, 17
	mov dl, 32
	call gotoXY
	mov eax, white+(red*16)
	call setTextColor
	mov edx, OFFSET start
	call writeString

	mov eax, white+(black*16)
	call setTextColor
	
	mov dh, 17
	mov dl, 30
	call gotoXY
	mov al, 175 ; ">>"
	call writeChar
again:
	call readChar	
	cmp al, 0Dh
	jne again

	call clrscr
	
ret
splashScreen ENDP


.data
gameOverSplash BYTE "Game Over",0
yourScore BYTE "Your score is: ",0
restartButton BYTE "Restart",0
exitButton BYTE "Exit",0
choice BYTE 0
                                                 

.code
gameOverScreen PROC
	call clrscr

	mov eax, yellow+(black*16)
	call setTextColor

	mov dh, 10
	mov dl, 24
	call gotoXY
	mov edx, OFFSET gameOverSplash
	call writeString

	mov dh, 12
	mov dl, 24
	call gotoXY
	mov edx, OFFSET yourScore
	call writeString

	mov dh, 13
	mov dl, 39
	call gotoXY
	mov ax, score
	call writeDec
	call crlf

	; 按鈕顏色: 紅底白字
	mov eax, white+(red*16)
	call setTextColor

	mov dh, 17
	mov dl, 32
	call gotoXY
	mov edx, OFFSET restartButton
	call writeString

	mov dh, 18
	mov dl, 32
	call gotoXY
	mov edx, OFFSET exitButton
	call writeString

	; 顏色改回來預設
	mov eax, white+(black*16)
	call setTextColor
	endChoice:
		call moveCursor
		call readChar
		call cleanMenu
		cmp al, 0Dh
		jne nopeNope
			.IF choice==0h
			call again
			.ELSEIF choice==1h
			call crlf
			exit
			.ENDIF
		nopeNope:

		.IF ah == 72
			mov choice,0h
		.ELSEIF ah == 80
			mov choice,1h
		.ENDIF
		
						
	jmp endChoice	
ret
gameOverScreen ENDP


; Helper Functions

; 移動游標到 >
moveCursor PROC uses eax edx
	.IF choice==0
			mov dh, 17
			mov dl, 30
			call gotoXY
			mov al, 175 ; ">>"
			call writeChar
			
	.ELSEIF choice==1
				mov dh, 18
				mov dl, 30
				call gotoXY
				mov al, 175 ; ">>"
				call writeChar
	.ENDIF
ret
moveCursor ENDP

; 清除螢幕Menu~
cleanMenu PROC uses eax edx				
		cmp choice, 1
		je otherOption
			mov dh, 17
			mov dl, 30
			call gotoXY
			mov al,' '
			call writeChar
			jmp goBack
		otherOption:
			mov dh, 18
			mov dl, 30
			call gotoXY
			mov al,' '
			call writeChar
goBack:
ret
cleanMenu ENDP

; 重新開始
again PROC
	mov ax, 10
	mov snakeLength, ax

	mov ecx, snakeMax
	mov edi, 0
zeroInitialize:
	mov ax, 0
	mov snakeBody[edi],ax
	add edi, TYPE COORDINATE
loop zeroInitialize
	call initializeSnake

	mov score, 0
	mov hit, 0
	mov speed,100
	mov currentDirection, RIGHT
	call main
ret
again ENDP

end main