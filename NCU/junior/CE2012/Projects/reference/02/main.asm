INCLUDE Irvine32.inc

main          EQU start@0

element STRUCT
	opHandle 	DWORD ?
	count 		DWORD ?
	position 	COORD <>
element ENDS

printScreen proto, array:PTR BYTE, screen:element
endScreen proto, array:PTR BYTE, screen:element
gameScreen proto, screen:element, screen2:element
printBox proto, screen:element
printPlayer proto, screen:element
printTime proto
printTarget proto
initial_cube_set proto
random_cube_set proto
cube_renew proto
printskull proto
computescore proto
printscore proto
scorechoose proto
cube proto
ExitProcess proto,dwExitCode:dword

.data
	;畫面邊界----------------------------------------------------------------------------
	boxTop    	BYTE 0DAh, (70 - 2) DUP(0C4h), 0BFh
	boxBody   	BYTE 0B3h
	boxBottom 	BYTE 0C0h, (70 - 2) DUP(0C4h), 0D9h

	;開始畫面----------------------------------------------------------------------------
	startArray   	BYTE "                            "
		     	BYTE "        HIT THE SKULL       "
			BYTE "                            "
	 	     	BYTE "        Start   (Space)     "
		     	BYTE "        Quit    (Esc)       "

	;結束畫面----------------------------------------------------------------------------
	endArray	BYTE "Score:                      "
			BYTE "                            "
			BYTE "                            "
			BYTE "                            "
			BYTE "                            "
			BYTE "                            "
			BYTE "                            "
			BYTE "                            "
			BYTE "                            "
			BYTE "                            "
			BYTE "                            "
			BYTE "                            "
			BYTE "                            "
			BYTE "                            "
			BYTE "                            "
			BYTE "                            "
			BYTE "                            "
			BYTE "                            "
			BYTE "                            "
			BYTE "                            "
			BYTE "                            "
			BYTE "                            "
			BYTE "                            "
			BYTE "                            "
			BYTE "                            "
	 		BYTE "Restart   (Space)           "
			BYTE "Quit      (Esc)             "
	
	;遊戲畫面----------------------------------------------------------------------------
	;	遊戲中右邊界-----------------------------------------------------------------
	right		BYTE "Restart(Space)"
			BYTE "End    (Z)  "
	boxBodyR 	COORD <69, 1>			;畫面右邊位置

	;遊戲內物件--------------------------------------------------------------------------
	screenIni 	element <0, 0, <0, 0>>		;畫面參數
	cubePosition 	BYTE 5 DUP(0)			;目標位置陣列

	skull		BYTE"                        uuuuuuuuuuuuuuuuuuuuu.                     "
			BYTE"                   .u$$$$$$$$$$$$$$$$$$$$$$$$$$W.                  "
			BYTE"                 u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Wu.             "
			BYTE"               $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i           "
			BYTE"              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$          "
        		BYTE"                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       "
			BYTE"           .i$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i       "
			BYTE"           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$W      "
			BYTE"          .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$W    "
			BYTE"         .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i  "
			BYTE"         #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$. "
			BYTE"         W$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ "
			BYTE"$u       #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$~"
			BYTE"$#      `*$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
			BYTE"$i        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
			BYTE"$$        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
			BYTE"$$         $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
			BYTE"#$.        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#"
			BYTE" $$      $iW$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$!"
			BYTE" $$i      $$$$$$$#** `***#$$$$$$$$$$$$$$$$$#******#$$$$$$$$$$$$$$$W"
			BYTE" #$$W    `$$$#*            *       !$$$$$`           `*#$$$$$$$$$$#"
			BYTE"  $$$     ``                 ! !iuW$$$$$                 #$$$$$$$# "
			BYTE"  #$$    $u                  $   $$$$$$$                  $$$$$$$~ "
			BYTE"   *#    #$$i.               #   $$$$$$$.                 `$$$$$$  "
			BYTE"          $$$$$i.                ***#$$$$i.               .$$$$#   "
			BYTE"          $$$$$$$$!         .   `    $$$$$$$$$i           $$$$$    "
			BYTE"          `$$$$$  $iWW   .uW`        #$$$$$$$$$W.       .$$$$$$#   "
			BYTE"            *#$$$$$$$$$$$$#`          $$$$$$$$$$$iWiuuuW$$$$$$$$W  "
			BYTE"               !#**    **             `$$$$$$$##$$$$$$$$$$$$$$$$   "
			BYTE"          i$$$$    .                   !$$$$$$ .$$$$$$$$$$$$$$$#   "
			BYTE"         $$$$$$$$$$`                    $$$$$$$$$Wi$$$$$$#*#$$`    "
			BYTE"         #$$$$$$$$$W.                   $$$$$$$$$$$#   ``          "
			BYTE"          `$$$$##$$$$!       i$u.  $. .i$$$$$$$$$#**               "
			BYTE"             *     `#W       $$$$$$$$$$$$$$$$$$$`      u$#         "
			BYTE"                            W$$$$$$$$$$$$$$$$$$      $$$$W         "
			BYTE"                            $$`!$$$##$$$$``$$$$      $$$$!         "
			BYTE"                           i$* $$$$  $$#*`  ***     W$$$$          "
			BYTE"                                                   W$$$$!          "
			BYTE"                      uW$$  uu  uu.  $$$  $$$Wu#   $$$$$$          "
			BYTE"                     ~$$$$iu$$iu$$$uW$$! $$$$$$i .W$$$$$$          "
			BYTE"             ..  !   *#$$$$$$$$$$##$$$$$$$$$$$$$$$$$$$$#*          "
			BYTE"             $$W  $     *#$$$$$$$iW$$$$$$$$$$$$$$$$$$$$$W          "
 			BYTE"            $#`   `       **#$$$$$$$$$$$$$$$$$$$$$$$$$$$           "
			BYTE"                              !$$$$$$$$$$$$$$$$$$$$$#`             "
			BYTE"                              $$$$$$$$$$$$$$$$$$$$$$!              "
			BYTE"                            $$$$$$$$$$$$$$$$$$$$$$$`               "
			BYTE"                             $$$$$$$$$$$$$$$$$$$$*                 "

	player		BYTE" _-_____________=_  "
			BYTE"|_______|======|' >="
			BYTE"|_______|======| |/ "
			BYTE"       \|======| |  "
			BYTE"        '------| |\ "
			BYTE"          |  | \...'" 
			BYTE"          |  / |...|"
			BYTE"          \____|...|"
			BYTE"               |...|"
			BYTE"              /....|"
			BYTE"             '-----/"

	target		BYTE" _.-======-._ "
			BYTE"|, .-.  .-. ,|"
			BYTE"|)(__/  \__)(|"
			BYTE"(_    ^^     )"
			BYTE" \_|IIIIII|_/ "
			BYTE"   \______/   "

	score0		BYTE"  ******  "
			BYTE"  *    *  "
			BYTE"  *    *  "
			BYTE"  *    *  "
			BYTE"  ******  "

	score1		BYTE"    **    "
			BYTE"   * *    "
			BYTE"     *    "
			BYTE"     *    "
			BYTE"   *****  "

	score2		BYTE"  ******  "
			BYTE"       *  "
			BYTE"  ******  "
			BYTE"  *       "
			BYTE"  ******  "

	score3		BYTE"  ******  "
			BYTE"       *  "
			BYTE"  ******  "
			BYTE"       *  "
			BYTE"  ******  "

	score4		BYTE"  *    *  "
			BYTE"  *    *  "
			BYTE"  ******  "
			BYTE"       *  "
			BYTE"       *  "

	score5		BYTE"  ******  "
			BYTE"  *       "
			BYTE"  ******  "
			BYTE"       *  "
			BYTE"  ******  "

	score6		BYTE"  ******  "
			BYTE"  *       "
			BYTE"  ******  "
			BYTE"  *    *  "
			BYTE"  ******  "

	score7		BYTE"  ******  "
			BYTE"       *  "
			BYTE"       *  "
			BYTE"       *  "
			BYTE"       *  "

	score8		BYTE"  ******  "
			BYTE"  *    *  "
			BYTE"  ******  "
			BYTE"  *    *  "
			BYTE"  ******  "

	score9		BYTE"  ******  "
			BYTE"  *    *  "
			BYTE"  ******  "
			BYTE"       *  "
			BYTE"  ******  "


	finalscore	BYTE "   "
	discribe	BYTE "[",6Ah,"]"
	playerAttributes	WORD (20) 	DUP(0Ah)	;玩家參數 0A綠 0B藍 0C紅 0D紫 0E黃 
	discribeAttributes	WORD (3) 	DUP(0Eh)	;描述參數
	targetAttributes	WORD (14) 	DUP(0Ch)	;目標參數
	skullAttributes		WORD (67) 	DUP(0Dh)	;骷髏頭參數

	targetCover 	BYTE (68) DUP(" ")		;目標覆蓋
	initialTime 	BYTE 33h, 30h, 73h		;時間
	timeCountDown 	BYTE 30				;總迴圈次數
	loopCount 	BYTE 0				;計秒迴圈，20次為一秒
	decimalCount 	BYTE 0				;更新時間用
	killnumber	BYTE 0				;急殺數
	scoreWeight	BYTE 1				;分數權重
	killcount	BYTE 33				;33換權重
	scoredivisor	BYTE 10				;分數除數
	score		WORD 0				;得分

	skullPosition	COORD <11, 1>			;骷髏頭位置
	targetPosition 	COORD <0, 23>			;目標位置
	scorePosition 	COORD <51, 12>			;分數位置
	coverPosition 	COORD <41, 1>			;目標覆蓋位置
	timer		COORD <6, 1>			;時間位置
	outputHandle	DWORD 0

	
.code
main PROC
	
	call Clrscr
	invoke printskull
	mov eax, 2000
	call Delay	

;開始畫面------------------------------------------------------------------------------------
START:	
	;印出畫面----------------------------------------------------------------------------
	invoke printScreen, ADDR startArray, screenIni
L5:
	call ReadChar
	.IF ax == 011Bh	;esc
		jmp gameEXIT				;按Esc,關閉遊戲
	.ENDIF
	.IF ax == 3920h	;z
		jmp GAME				;按Space,開始遊戲
	.ENDIF
	jmp L5

;遊戲畫面------------------------------------------------------------------------------------
GAME:
	;初始化遊戲物件----------------------------------------------------------------------
	mov timeCountDown, 30
	mov loopCount, 0
	mov initialTime[0], 33h
	mov initialTime[1], 30h
	mov targetPosition.x, 0
	mov targetPosition.y, 23
	mov score,0
	mov killnumber,0
	mov scoreWeight,1
	
	;印出畫面----------------------------------------------------------------------------
	invoke gameScreen, screenIni, screenIni
	invoke printPlayer, screenIni
	invoke initial_cube_set
	invoke printTarget
	invoke printTime

	;進入迴圈----------------------------------------------------------------------------
LookForKey:
	;判斷30秒是否結束--------------------------------------------------------------------
	.IF timeCountDown == 0
		jmp gameEND
	.ENDIF
	;判斷是否過一秒----------------------------------------------------------------------
	.IF loopCount == 20
		dec timeCountDown
		mov loopCount, 0
		.IF initialTime[1] == 30h
			mov initialTime[1], 39h
			dec initialTime[0]
		.ELSE
			dec initialTime[1]
		.ENDIF
		invoke printTime
	.ENDIF

	;判斷按鍵----------------------------------------------------------------------------
	mov eax, 50
	call Delay
	inc loopCount
	call ReadKey
	jz LookForKey					;沒抓到按鍵,進入下一迴圈
	.IF al == 20h
		jmp GAME				;按Space,開始遊戲
	.ENDIF
	.IF al == 7Ah
		jmp gameEnd				;按z,結束遊戲
	.ENDIF
	.IF (al == 6Ah) && (cubePosition[0] == 00h)	;按j且目標左,得分,更新目標位置
		inc killnumber
		invoke cube_renew
		mov targetPosition.x, 0
		mov targetPosition.y, 23
		invoke printTarget
	.ENDIF
	.IF (al == 6Bh) && (cubePosition[0] == 01h)	;按k且目標中,得分,更新目標位置
		inc killnumber
		invoke cube_renew
		mov targetPosition.x, 0
		mov targetPosition.y, 23
		invoke printTarget
	.ENDIF
	.IF (al == 6Ch) && (cubePosition[0] == 02h)	;按l且目標右,得分,更新目標位置
		inc killnumber
		invoke cube_renew
		mov targetPosition.x, 0
		mov targetPosition.y, 23
		invoke printTarget
	.ENDIF

	jmp LookForKey					;進入下一迴圈
	

;結束畫面------------------------------------------------------------------------------------
gameEND:
	
	invoke computescore
	invoke endScreen, ADDR endArray, screenIni
	invoke printscore
L4:
	call ReadChar
	.IF ax == 011Bh	;esc
		jmp gameEXIT				;按Esc,關閉遊戲
	.ENDIF
	.IF ax == 3920h	;space				;按Space,開始遊戲
		jmp GAME
	.ENDIF
	jmp L4

;關閉遊戲------------------------------------------------------------------------------------
gameEXIT:
	call Clrscr
	exit


main ENDP






;Procedure///////////////////////////////////////////////////////////////////////////////////
;--------------------------------------------------------
;printScreen 列印開始畫面
;--------------------------------------------------------
printScreen PROC USES eax ecx edi, array:PTR BYTE, screen:element
	invoke printBox, screenIni
	mov screen.opHandle, 0
	mov screen.count, 0
	mov screen.position.x, 31
	mov screen.position.y, 10	 
	invoke GetStdHandle, STD_OUTPUT_HANDLE
	mov screen.opHandle, eax
	mov ecx, 5
	mov edi, array
L1:
	push ecx
	invoke WriteConsoleOutputCharacter,
		screen.opHandle, 
		edi, 
		28, 
		screen.position, 
		ADDR screen.count
	pop ecx
	add edi, 28
	inc screen.position.y
	loop L1
	ret 
printScreen ENDP

;--------------------------------------------------------
;endScreen 列印結束畫面
;--------------------------------------------------------
endScreen PROC USES eax ecx edi, array:PTR BYTE, screen:element
	invoke printBox, screenIni
	mov screen.opHandle, 0
	mov screen.count, 0
	mov screen.position.x, 12
	mov screen.position.y, 5	 
	invoke GetStdHandle, STD_OUTPUT_HANDLE
	mov screen.opHandle, eax
	mov ecx, 27
	mov edi, array
L1:
	push ecx
	invoke WriteConsoleOutputCharacter,
		screen.opHandle, 
		edi, 
		28, 
		screen.position, 
		ADDR screen.count
	pop ecx
	add edi, 28
	inc screen.position.y
	loop L1
	ret 
endScreen ENDP

;--------------------------------------------------------
;gameScreen 列印遊戲畫面(右邊界)
;--------------------------------------------------------
gameScreen PROC USES eax ecx edi, screen1:element, screen2:element
	invoke printBox, screenIni
	mov screen2.opHandle, 0
	mov screen2.count, 0
	mov screen2.position.x, 81
	mov screen2.position.y, 1
	invoke GetStdHandle, STD_OUTPUT_HANDLE
	mov screen1.opHandle, eax
	mov screen2.opHandle, eax
	mov edi, OFFSET right
	invoke WriteConsoleOutputCharacter,
		screen2.opHandle, 
		edi, 
		14, 
		screen2.position, 
		ADDR screen2.count
	inc screen2.position.y
	add edi, 14
	invoke WriteConsoleOutputCharacter,
		screen2.opHandle, 
		edi, 
		14, 
		screen2.position, 
		ADDR screen2.count
	ret 
gameScreen ENDP


;--------------------------------------------------------
;printBox 列印遊戲邊界
;--------------------------------------------------------
printBox PROC USES eax ecx edi, screen:element
	mov screen.opHandle, 0
	mov screen.count, 0
	mov screen.position.x, 10
	mov screen.position.y, 0
	mov boxBodyR.x, 79
	mov boxBodyR.y, 1
	invoke GetStdHandle, STD_OUTPUT_HANDLE
	mov screen.opHandle, eax
	call Clrscr
	invoke WriteConsoleOutputCharacter,
		screen.opHandle, 
		ADDR boxTop, 
		70, 
		screen.position, 
		ADDR screen.count
	inc screen.position.y
	mov ecx, 48
L2:
	push ecx
	invoke WriteConsoleOutputCharacter,
		screen.opHandle, 
		ADDR boxBody, 
		1, 
		screen.position, 
		ADDR screen.count
	invoke WriteConsoleOutputCharacter,
		screen.opHandle, 
		ADDR boxBody, 
		1, 
		boxBodyR, 
		ADDR screen.count
	inc screen.position.y
	inc boxBodyR.y
	pop ecx
	loop L2
	invoke WriteConsoleOutputCharacter,
		screen.opHandle, 
		ADDR boxBottom, 
		70, 
		screen.position, 
		ADDR screen.count
	inc screen.position.y
	ret
printBox ENDP


;--------------------------------------------------------
;printPlayer 列印遊戲畫面(玩家)
;--------------------------------------------------------
printPlayer PROC USES eax ecx edi, screen:element
	mov screen.opHandle, 0
	mov screen.count, 0
	mov screen.position.x, 12
	mov screen.position.y, 39
	invoke GetStdHandle, STD_OUTPUT_HANDLE
	mov screen.opHandle, eax
	mov ecx, 10
	mov edi,OFFSET player
	;列印槍枝----------------------------------------
L1:
	push ecx
	mov ecx,3
L2:	
	push ecx
	invoke WriteConsoleOutputAttribute,
      		screen.opHandle,
      		ADDR playerAttributes,
      		20,
      		screen.position,
      		ADDR screen.count
	invoke WriteConsoleOutputCharacter,
		screen.opHandle, 
		edi, 
		20, 
		screen.position, 
		ADDR screen.count
	pop ecx
	add screen.position.x, 23
	loop L2
	pop ecx
	add edi,20
	mov screen.position.x, 12
	inc screen.position.y
	loop L1
	mov screen.position.x, 16
	mov screen.position.y, 45
	mov discribe[1],6Ah
	mov ecx,3
	;列印[j][k][l]----------------------------------
L3:
	push ecx
	invoke WriteConsoleOutputAttribute,
      		screen.opHandle,
      		ADDR discribeAttributes,
      		3,
      		screen.position,
      		ADDR screen.count
	invoke WriteConsoleOutputCharacter,
		screen.opHandle, 
		ADDR discribe, 
		3, 
		screen.position, 
		ADDR screen.count
	pop ecx
	inc discribe[1]
	add screen.position.x, 23
	loop L3


	ret
printPlayer ENDP


;--------------------------------------------------------
;printTime 列印遊戲畫面(時間)
;--------------------------------------------------------
printTime PROC USES eax ecx
	invoke GetStdHandle, STD_OUTPUT_HANDLE
	invoke WriteConsoleOutputCharacter,
		eax, 
		ADDR initialTime, 
		3, 
		timer, 
		ADDR screenIni.count
	ret
printTime ENDP



;--------------------------------------------------------
;printTime 列印遊戲畫面(所有目標)
;--------------------------------------------------------
printTarget PROC USES ecx edi
	mov ecx, 38
	mov coverPosition.x, 11
	mov coverPosition.y, 1
	;清除畫面----------------------------------------
Cover:	
	push ecx
	invoke GetStdHandle, STD_OUTPUT_HANDLE
	invoke WriteConsoleOutputCharacter,
		eax, 
		ADDR targetCover, 
		68, 
		coverPosition, 
		ADDR screenIni.count
	inc coverPosition.y
	pop ecx
	loop Cover
	;列印新目標--------------------------------------
	mov targetPosition.y, 33
	mov edi, OFFSET cubePosition
	mov ecx, 5
L:
	.IF BYTE PTR [edi] == 0
		mov targetPosition.x, 15
	.ELSEIF BYTE PTR [edi] == 1
		mov targetPosition.x, 38
	.ELSE
		mov targetPosition.x, 61
	.ENDIF
	invoke cube
	inc edi
	sub targetPosition.y, 14
	loop L
	ret
printTarget ENDP


;--------------------------------------------------------
;cube 列印遊戲畫面(單一目標)
;--------------------------------------------------------
cube PROC USES eax ecx edi
	mov ecx, 6
	mov edi,OFFSET target
L:
	push ecx
	invoke GetStdHandle, STD_OUTPUT_HANDLE
	invoke WriteConsoleOutputAttribute,
      		eax,
      		ADDR targetAttributes,
      		14,
      		targetPosition,
      		ADDR screenIni.count
	invoke GetStdHandle, STD_OUTPUT_HANDLE
	invoke WriteConsoleOutputCharacter,
		eax, 
		edi, 
		14, 
		targetPosition, 
		ADDR screenIni.count
	pop ecx
	inc targetPosition.y
	add edi,14
	loop L
	ret
cube ENDP


;--------------------------------------------------------
;random_cube_set 隨機選擇左中右
;--------------------------------------------------------
random_cube_set PROC
	mov eax,3
	call RandomRange
	mov BYTE PTR [edi],al
	ret
random_cube_set ENDP


;--------------------------------------------------------
;initial_cube_set 初始化目標位置
;--------------------------------------------------------
initial_cube_set PROC USES eax ecx edi
	mov ecx,5
	mov edi,OFFSET cubePosition
cube_set:
	invoke random_cube_set
	inc edi
	loop cube_set
	ret
initial_cube_set ENDP


;--------------------------------------------------------
;cube_renew 更新目標位置
;--------------------------------------------------------
cube_renew PROC USES eax ecx esi edi
	mov	ecx,4
	mov esi, OFFSET cubePosition
	inc esi
	mov edi, OFFSET cubePosition

	cld               ;clear direction flag
	rep movsb	     ;do the move
	invoke random_cube_set
	ret
cube_renew ENDP


;--------------------------------------------------------
;printskull 列印骷髏頭
;--------------------------------------------------------
printskull PROC USES eax ecx edi
	mov ecx, 47
	mov edi,OFFSET skull
L:
	push ecx
	invoke GetStdHandle, STD_OUTPUT_HANDLE
	invoke WriteConsoleOutputAttribute,
      		eax,
      		ADDR skullAttributes,
      		67,
      		skullPosition,
      		ADDR screenIni.count
	invoke GetStdHandle, STD_OUTPUT_HANDLE
	invoke WriteConsoleOutputCharacter,
		eax, 
		edi, 
		67, 
		skullPosition, 
		ADDR screenIni.count
	pop ecx
	inc skullPosition.y
	add edi,67
	loop L
	ret
printskull ENDP


;--------------------------------------------------------
;computescore	計算分數
;--------------------------------------------------------
computescore PROC USES eax

L:
	.IF killnumber < 33
		xor eax,eax
		mov al,scoreWeight
		mul killnumber
		add score,ax
		ret
	.ENDIF
	xor eax,eax
	mov al,scoreWeight
	mul killcount
	add score,ax
	sub killnumber,33
	inc scoreWeight
	jmp L
computescore ENDP

;--------------------------------------------------------
;printscore 列印分數
;--------------------------------------------------------
printscore PROC USES eax ebx

	mov scorePosition.x,51
	mov scorePosition.y,12
	xor eax,eax
	.IF score < 100
		jmp L
	.ENDIF
	mov ax,score
	div scoredivisor
	mov bl,ah
	invoke scorechoose
	sub scorePosition.x,15



	mov ah,0
	mov score,ax
L:
	mov ax,score
	div scoredivisor
	mov bl,ah
	invoke scorechoose
	sub scorePosition.x,15




	mov bl,al
	invoke scorechoose
	
	ret
printscore ENDP


;--------------------------------------------------------
;scorechoose 選擇分數
;--------------------------------------------------------
scorechoose PROC USES eax edi
	
	invoke GetStdHandle, STD_OUTPUT_HANDLE
	mov outputHandle,eax
	mov ecx,5
	.IF bl == 0
		mov edi,OFFSET score0
L0:
		push ecx
		invoke WriteConsoleOutputCharacter,
			outputHandle, 
			edi, 
			10, 
			scorePosition, 
			ADDR screenIni.count
		pop ecx
		inc scorePosition.y
		add edi,10
		loop L0
	.ENDIF
	.IF bl == 1
		mov edi,OFFSET score1
L1:
		push ecx
		invoke WriteConsoleOutputCharacter,
		outputHandle, 
		edi, 
		10, 
		scorePosition, 
		ADDR screenIni.count
		pop ecx
		inc scorePosition.y
		add edi,10
		loop L1
	.ENDIF
	.IF bl == 2
		mov edi,OFFSET score2
L2:
		push ecx
		invoke WriteConsoleOutputCharacter,
		outputHandle, 
		edi, 
		10, 
		scorePosition, 
		ADDR screenIni.count
		pop ecx
		inc scorePosition.y
		add edi,10
		loop L2
	.ENDIF
	.IF bl == 3
		mov edi,OFFSET score3
L3:
		push ecx
		invoke WriteConsoleOutputCharacter,
		outputHandle, 
		edi, 
		10, 
		scorePosition, 
		ADDR screenIni.count
		pop ecx
		inc scorePosition.y
		add edi,10
		loop L3
	.ENDIF
	.IF bl == 4
		mov edi,OFFSET score4
L4:
		push ecx
		invoke WriteConsoleOutputCharacter,
		outputHandle, 
		edi, 
		10, 
		scorePosition, 
		ADDR screenIni.count
		pop ecx
		inc scorePosition.y
		add edi,10
		loop L4
	.ENDIF
	.IF bl == 5
		mov edi,OFFSET score5
L5:
		push ecx
		invoke WriteConsoleOutputCharacter,
		outputHandle, 
		edi, 
		10, 
		scorePosition, 
		ADDR screenIni.count
		pop ecx
		inc scorePosition.y
		add edi,10
		loop L5
	.ENDIF
	.IF bl == 6
		mov edi,OFFSET score6
L6:
		push ecx
		invoke WriteConsoleOutputCharacter,
		outputHandle, 
		edi, 
		10, 
		scorePosition, 
		ADDR screenIni.count
		pop ecx
		inc scorePosition.y
		add edi,10
		loop L6
	.ENDIF
	.IF bl == 7
		mov edi,OFFSET score7
L7:
		push ecx
		invoke WriteConsoleOutputCharacter,
		outputHandle, 
		edi, 
		10, 
		scorePosition, 
		ADDR screenIni.count
		pop ecx
		inc scorePosition.y
		add edi,10
		loop L7
	.ENDIF
	.IF bl == 8
		mov edi,OFFSET score8
L8:
		push ecx
		invoke WriteConsoleOutputCharacter,
		outputHandle, 
		edi, 
		10, 
		scorePosition, 
		ADDR screenIni.count
		pop ecx
		inc scorePosition.y
		add edi,10
		loop L8
	.ENDIF
	.IF bl == 9
		mov edi,OFFSET score9
L9:
		push ecx
		invoke WriteConsoleOutputCharacter,
		outputHandle, 
		edi, 
		10, 
		scorePosition, 
		ADDR screenIni.count
		pop ecx
		inc scorePosition.y
		add edi,10
		loop L9
	.ENDIF
	mov scorePosition.y,12
	ret
scorechoose ENDP


END main
