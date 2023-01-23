TITLE SlotMachine (SlotMachine.asm)

;INCLUDE Irvine32.inc
INCLUDE mylib.inc

MachineWidth = 61
SlotWidth = 10
betMoneyStrWidth = 6


WriteConsoleOutputCharacter PROTO,
	handleScreenBuf:DWORD,			
	pBuffer:PTR BYTE,				
	bufsize:DWORD,					
	xyPos:COORD,					
	pCount:PTR DWORD	

SetConsoleTitle PROTO, titleStr :PTR BYTE

SetConsoleScreenBufferSize PROTO,
	outHandle:DWORD,			    ; handle to screen buffer
	dwSize:COORD				    ; new screen buffer size

print_title PROTO, 
		string:ptr, position:COORD

print_rule PROTO, 
		string:ptr, position:COORD

print_lose PROTO, 
		string:ptr, position:COORD

print_slotmachine PROTO,
		string: ptr, position:COORD


main          EQU start@0

.data
drawPosition COORD <14,6>			; for drawing slotmachine
currentMoney DWORD 500
yourmoneyStr byte "Your money:"
yourMoneyStrPosition COORD <0,0>
yourbetStr byte "Your bet:"
yourbetStrPosition COORD <0,2>
cursorPosition COORD <10,2>			; for input money
seprationlinePosition COORD <0,3>
statusPosition COORD <20,2>			; for showing status message
picturePosition COORD <0,0>			; for pictures of slotmachine block

SlotBody BYTE 0, 0, 0				; for saving random number



.code
print_title PROC uses ecx, 
		string:ptr, position:COORD
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,   				
		string,   				
		77,   						
		position,   					
		ADDR count
	inc xyPosition.y
	ret
print_title ENDP

print_rule PROC uses ecx, 
		string:ptr, position:COORD
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,   				
		string,   				
		52,   						
		position,   					
		ADDR count
	inc xyPosition.y
	ret
print_rule ENDP

print_lose PROC uses ecx, 
		string:ptr, position:COORD
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,   				
		string,   				
		96,   						
		position,   					
		ADDR count
	inc xyPosition.y
	ret
print_lose ENDP

print_slotmachine PROC uses ecx,
		string: ptr, position:COORD
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,   				
		string,   				
		MachineWidth,   						
		position,   					
		ADDR count
	inc drawPosition.y
	ret
print_slotmachine ENDP

Seven PROC,
    xPos:WORD, yPos:WORD

    mov cx, xPos
    mov picturePosition.x, cx
    mov cx, yPos
    mov picturePosition.y, cx


    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR seven1,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR seven2,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR seven3,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR seven4,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR seven5,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR seven6,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR seven7,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    ret
Seven ENDP

Spade PROC,
    xPos:WORD, yPos:WORD

    mov cx, xPos
    mov picturePosition.x, cx
    mov cx, yPos
    mov picturePosition.y, cx


    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR spade1,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR spade2,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR spade3,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR spade4,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR spade5,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR spade6,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR spade7,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    ret
Spade ENDP

Heart PROC,
    xPos:WORD, yPos:WORD

    mov cx, xPos
    mov picturePosition.x, cx
    mov cx, yPos
    mov picturePosition.y, cx


    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR heart1,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR heart2,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR heart3,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR heart4,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR heart5,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR heart6,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR heart7,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    ret
Heart ENDP

Diamond PROC,
    xPos:WORD, yPos:WORD

    mov cx, xPos
    mov picturePosition.x, cx
    mov cx, yPos
    mov picturePosition.y, cx


    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR diamond1,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR diamond2,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR diamond3,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR diamond4,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR diamond5,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR diamond6,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR diamond7,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    ret
Diamond ENDP

Club PROC,
    xPos:WORD, yPos:WORD

    mov cx, xPos
    mov picturePosition.x, cx
    mov cx, yPos
    mov picturePosition.y, cx


    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR club1,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR club2,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR club3,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR club4,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR club5,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR club6,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    inc picturePosition.y                      

    INVOKE WriteConsoleOutputCharacter,
    outputHandle,                       ; console output handle
    ADDR club7,                        ; pointer to the top Slot line
    SlotWidth,                          ; size of Slot line
    picturePosition,                    ; coordinates of first char
    ADDR count                          ; output count

    ret
Club ENDP



start@0 PROC

	INVOKE GetStdHandle, STD_OUTPUT_HANDLE  
	    mov outputHandle, eax 				
	call Clrscr

	INVOKE SetConsoleTitle, ADDR titleStr	
	INVOKE SetConsoleScreenBufferSize, outputHandle, screen_size

Menu:
	INVOKE print_title, addr topic1, xyPosition
	INVOKE print_title, addr topic2, xyPosition
	INVOKE print_title, addr topic3, xyPosition
	INVOKE print_title, addr topic4, xyPosition
	INVOKE print_title, addr topic5, xyPosition
	INVOKE print_title, addr topic6, xyPosition
	INVOKE print_title, addr topic7, xyPosition
	INVOKE print_title, addr topic8, xyPosition
	INVOKE print_title, addr topic9, xyPosition
	INVOKE print_title, addr topic10, xyPosition
	INVOKE print_title, addr topic11, xyPosition
	INVOKE print_title, addr topic12, xyPosition
	INVOKE print_title, addr topic13, xyPosition
	INVOKE print_title, addr topic14, xyPosition
	INVOKE print_title, addr topic15, xyPosition


	; 改變游標位置
	push dx
	mov  dl, 33
	mov  dh, 22
	call Gotoxy
	pop  dx

	call WaitMsg


Rules:

	call Clrscr

	mov xyPosition.x, 18
	mov xyPosition.y, 5
	INVOKE print_rule, addr border, xyPosition
	INVOKE print_rule, addr rule1, xyPosition
	INVOKE print_rule, addr empty, xyPosition
	INVOKE print_rule, addr empty, xyPosition
	INVOKE print_rule, addr rule2, xyPosition
	INVOKE print_rule, addr rule3, xyPosition
	INVOKE print_rule, addr empty, xyPosition
	INVOKE print_rule, addr empty, xyPosition
	INVOKE print_rule, addr rule4, xyPosition
	INVOKE print_rule, addr empty, xyPosition
	INVOKE print_rule, addr rule5, xyPosition
	INVOKE print_rule, addr empty, xyPosition
	INVOKE print_rule, addr rule6, xyPosition
	INVOKE print_rule, addr empty, xyPosition
	INVOKE print_rule, addr rule7, xyPosition
	INVOKE print_rule, addr empty, xyPosition
	INVOKE print_rule, addr empty, xyPosition
	INVOKE print_rule, addr empty, xyPosition
	INVOKE print_rule, addr rule8, xyPosition
	INVOKE print_rule, addr empty, xyPosition
	INVOKE print_rule, addr border, xyPosition

	
	; press enter to continue
	Read:
		xor eax, eax
		call ReadChar
		.IF ax == 1C0Dh					;enter
			jmp SlotMachine
		.ELSE
			jmp Read	
		.ENDIF


SlotMachine:

	call Clrscr

	; 初始所有Position(避免從別處jump回SlotMachine時出錯)
	mov drawPosition.x, 14
	mov drawPosition.y, 6
	mov yourMoneyStrPosition.x, 0
	mov yourMoneyStrPosition.y, 0
	mov yourbetStrPosition.x, 0
	mov yourbetStrPosition.y, 2
	mov cursorPosition.x, 10
	mov cursorPosition.y, 2
	mov seprationlinePosition.x, 0
	mov seprationlinePosition.y, 3
	mov statusPosition.x, 20
	mov statusPosition.y, 2

	; 初始化moneyStr
	mov moneyStr[7], 0
	mov moneystr[6], 0
	mov moneystr[5], 0
	mov moneystr[4], 0
	mov moneystr[3], 0
	mov moneystr[2], 0
	mov moneystr[1], 0

	; 初始化betStr
	mov betMoneyStr[5], 0
	mov betMoneyStr[4], 0
	mov betMoneyStr[3], 0
	mov betMoneyStr[2], 0
	mov betMoneyStr[1], 0
	mov betMoneyStr[0], 0


	; print yourmoneyStr
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,   					
		addr yourmoneyStr,   						
		sizeof yourmoneyStr,   						
		yourMoneyStrPosition,   						
		ADDR count

	; ------------------print money------------------
	; change money to string
	mov eax, currentMoney
	mov bl, 10
	mov edi, 6
	L2:											
		div bl
		add ah, 30h
		mov moneystr[edi], ah
		dec edi
		movzx ax, al
		cmp al, 0
		ja L2
	

	mov yourMoneyStrPosition.x, 12			; 設定money數字顯示位置
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,   					; indicate money
		ADDR moneystr,   					
		sizeof moneystr,   					
		yourMoneyStrPosition,   						
		ADDR count
	; ------------------end print money------------------

	; print yourbetStr
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,   					
		addr yourbetStr,   						
		sizeof yourbetStr,   						
		yourbetStrPosition,   						
		ADDR count

	; set cursor position(cursor移至輸入賭金的位置)
	INVOKE SetConsoleCursorPosition, outputHandle, cursorPosition

	; 畫分隔線
	inc yourbetStrPosition.y
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,   					
		addr seprationline,   						
		sizeof seprationline,   						
		seprationlinePosition,   						
		ADDR count

	; Draw initial slot machine
	INVOKE print_slotmachine, addr m1_1, drawPosition
	INVOKE print_slotmachine, addr m1_2, drawPosition
	INVOKE print_slotmachine, addr m1_3, drawPosition
	INVOKE print_slotmachine, addr m1_4, drawPosition
	INVOKE print_slotmachine, addr m1_5, drawPosition
	INVOKE print_slotmachine, addr m1_6, drawPosition
	INVOKE print_slotmachine, addr m1_7, drawPosition
	INVOKE print_slotmachine, addr m1_8, drawPosition
	INVOKE print_slotmachine, addr m1_9, drawPosition
	INVOKE print_slotmachine, addr m1_10, drawPosition
	INVOKE print_slotmachine, addr m1_11, drawPosition
	INVOKE print_slotmachine, addr m1_12, drawPosition
	INVOKE print_slotmachine, addr m1_13, drawPosition
	INVOKE print_slotmachine, addr m1_14, drawPosition
	INVOKE print_slotmachine, addr m1_15, drawPosition
	INVOKE print_slotmachine, addr m1_16, drawPosition
	INVOKE print_slotmachine, addr m1_17, drawPosition
	INVOKE print_slotmachine, addr m1_18, drawPosition
	INVOKE print_slotmachine, addr m1_19, drawPosition
	INVOKE print_slotmachine, addr m1_20, drawPosition
	INVOKE print_slotmachine, addr m1_21, drawPosition
	INVOKE print_slotmachine, addr m1_22, drawPosition


	; read input money 
	call   ReadInt
	mov    betMoney, eax

	; 若賭金>本金
	.IF eax > currentMoney
		INVOKE WriteConsoleOutputCharacter,
		  outputHandle,     
		  ADDR noMoney, 
		  SIZEOF noMoney,        
		  statusPosition,      
		  ADDR cellsWritten
		
		INVOKE sleep , 800
		call Clrscr
		jmp SlotMachine
		
	; 若賭金=0
	.ELSEIF eax == 0
		INVOKE WriteConsoleOutputCharacter,
		  outputHandle,     
		  ADDR zeroMoney, 
		  SIZEOF zeroMoney,        
		  statusPosition,      
		  ADDR cellsWritten 
		
		INVOKE sleep , 800
		call Clrscr
		jmp SlotMachine
	.ENDIF

	; ------------------Draw moving slot machine handle------------------
	; Draw the slot machine runing handle2
		mov drawPosition.x, 14
		mov drawPosition.y, 6
	INVOKE print_slotmachine, addr m2_1, drawPosition
	INVOKE print_slotmachine, addr m2_2, drawPosition
	INVOKE print_slotmachine, addr m2_3, drawPosition
	INVOKE print_slotmachine, addr m2_4, drawPosition
	INVOKE print_slotmachine, addr m2_5, drawPosition
	INVOKE print_slotmachine, addr m2_6, drawPosition
	INVOKE print_slotmachine, addr m2_7, drawPosition
	INVOKE print_slotmachine, addr m2_8, drawPosition
	INVOKE print_slotmachine, addr m2_9, drawPosition
	INVOKE print_slotmachine, addr m2_10, drawPosition
	INVOKE print_slotmachine, addr m2_11, drawPosition
	INVOKE print_slotmachine, addr m2_12, drawPosition
	INVOKE print_slotmachine, addr m2_13, drawPosition
	INVOKE print_slotmachine, addr m2_14, drawPosition
	INVOKE print_slotmachine, addr m2_15, drawPosition
	INVOKE print_slotmachine, addr m2_16, drawPosition
	INVOKE print_slotmachine, addr m2_17, drawPosition
	INVOKE print_slotmachine, addr m2_18, drawPosition
	INVOKE print_slotmachine, addr m2_19, drawPosition
	INVOKE print_slotmachine, addr m2_20, drawPosition
	INVOKE print_slotmachine, addr m2_21, drawPosition
	INVOKE print_slotmachine, addr m2_22, drawPosition


	INVOKE Sleep, 200                       ; delay

	; Draw the slot machine runing handle3
	    mov drawPosition.x, 14
	    mov drawPosition.y, 6
	INVOKE print_slotmachine, addr m3_1, drawPosition
	INVOKE print_slotmachine, addr m3_2, drawPosition
	INVOKE print_slotmachine, addr m3_3, drawPosition
	INVOKE print_slotmachine, addr m3_4, drawPosition
	INVOKE print_slotmachine, addr m3_5, drawPosition
	INVOKE print_slotmachine, addr m3_6, drawPosition
	INVOKE print_slotmachine, addr m3_7, drawPosition
	INVOKE print_slotmachine, addr m3_8, drawPosition
	INVOKE print_slotmachine, addr m3_9, drawPosition
	INVOKE print_slotmachine, addr m3_10, drawPosition
	INVOKE print_slotmachine, addr m3_11, drawPosition
	INVOKE print_slotmachine, addr m3_12, drawPosition
	INVOKE print_slotmachine, addr m3_13, drawPosition
	INVOKE print_slotmachine, addr m3_14, drawPosition
	INVOKE print_slotmachine, addr m3_15, drawPosition
	INVOKE print_slotmachine, addr m3_16, drawPosition
	INVOKE print_slotmachine, addr m3_17, drawPosition
	INVOKE print_slotmachine, addr m3_18, drawPosition
	INVOKE print_slotmachine, addr m3_19, drawPosition
	INVOKE print_slotmachine, addr m3_20, drawPosition
	INVOKE print_slotmachine, addr m3_21, drawPosition
	INVOKE print_slotmachine, addr m3_22, drawPosition


	INVOKE Sleep, 200                   ; delay

	; Draw the slot machine runing handle4
	    mov drawPosition.x, 14
	    mov drawPosition.y, 6
	INVOKE print_slotmachine, addr m4_1, drawPosition
	INVOKE print_slotmachine, addr m4_2, drawPosition
	INVOKE print_slotmachine, addr m4_3, drawPosition
	INVOKE print_slotmachine, addr m4_4, drawPosition
	INVOKE print_slotmachine, addr m4_5, drawPosition
	INVOKE print_slotmachine, addr m4_6, drawPosition
	INVOKE print_slotmachine, addr m4_7, drawPosition
	INVOKE print_slotmachine, addr m4_8, drawPosition
	INVOKE print_slotmachine, addr m4_9, drawPosition
	INVOKE print_slotmachine, addr m4_10, drawPosition
	INVOKE print_slotmachine, addr m4_11, drawPosition
	INVOKE print_slotmachine, addr m4_12, drawPosition
	INVOKE print_slotmachine, addr m4_13, drawPosition
	INVOKE print_slotmachine, addr m4_14, drawPosition
	INVOKE print_slotmachine, addr m4_15, drawPosition
	INVOKE print_slotmachine, addr m4_16, drawPosition
	INVOKE print_slotmachine, addr m4_17, drawPosition
	INVOKE print_slotmachine, addr m4_18, drawPosition
	INVOKE print_slotmachine, addr m4_19, drawPosition
	INVOKE print_slotmachine, addr m4_20, drawPosition
	INVOKE print_slotmachine, addr m4_21, drawPosition
	INVOKE print_slotmachine, addr m4_22, drawPosition


	INVOKE Sleep, 200                   ; delay
	  
	; Draw the slot machine runing handle5
	    mov drawPosition.x, 14
	    mov drawPosition.y, 6
	INVOKE print_slotmachine, addr m5_1, drawPosition
	INVOKE print_slotmachine, addr m5_2, drawPosition
	INVOKE print_slotmachine, addr m5_3, drawPosition
	INVOKE print_slotmachine, addr m5_4, drawPosition
	INVOKE print_slotmachine, addr m5_5, drawPosition
	INVOKE print_slotmachine, addr m5_6, drawPosition
	INVOKE print_slotmachine, addr m5_7, drawPosition
	INVOKE print_slotmachine, addr m5_8, drawPosition
	INVOKE print_slotmachine, addr m5_9, drawPosition
	INVOKE print_slotmachine, addr m5_10, drawPosition
	INVOKE print_slotmachine, addr m5_11, drawPosition
	INVOKE print_slotmachine, addr m5_12, drawPosition
	INVOKE print_slotmachine, addr m5_13, drawPosition
	INVOKE print_slotmachine, addr m5_14, drawPosition
	INVOKE print_slotmachine, addr m5_15, drawPosition
	INVOKE print_slotmachine, addr m5_16, drawPosition
	INVOKE print_slotmachine, addr m5_17, drawPosition
	INVOKE print_slotmachine, addr m5_18, drawPosition
	INVOKE print_slotmachine, addr m5_19, drawPosition
	INVOKE print_slotmachine, addr m5_20, drawPosition
	INVOKE print_slotmachine, addr m5_21, drawPosition
	INVOKE print_slotmachine, addr m5_22, drawPosition


	INVOKE Sleep, 200                   ; delay
	  
	; Draw the slot machine runing handle6
	    mov drawPosition.x, 14
	    mov drawPosition.y, 6
	INVOKE print_slotmachine, addr m6_1, drawPosition
	INVOKE print_slotmachine, addr m6_2, drawPosition
	INVOKE print_slotmachine, addr m6_3, drawPosition
	INVOKE print_slotmachine, addr m6_4, drawPosition
	INVOKE print_slotmachine, addr m6_5, drawPosition
	INVOKE print_slotmachine, addr m6_6, drawPosition
	INVOKE print_slotmachine, addr m6_7, drawPosition
	INVOKE print_slotmachine, addr m6_8, drawPosition
	INVOKE print_slotmachine, addr m6_9, drawPosition
	INVOKE print_slotmachine, addr m6_10, drawPosition
	INVOKE print_slotmachine, addr m6_11, drawPosition
	INVOKE print_slotmachine, addr m6_12, drawPosition
	INVOKE print_slotmachine, addr m6_13, drawPosition
	INVOKE print_slotmachine, addr m6_14, drawPosition
	INVOKE print_slotmachine, addr m6_15, drawPosition
	INVOKE print_slotmachine, addr m6_16, drawPosition
	INVOKE print_slotmachine, addr m6_17, drawPosition
	INVOKE print_slotmachine, addr m6_18, drawPosition
	INVOKE print_slotmachine, addr m6_19, drawPosition
	INVOKE print_slotmachine, addr m6_20, drawPosition
	INVOKE print_slotmachine, addr m6_21, drawPosition
	INVOKE print_slotmachine, addr m6_22, drawPosition
	

	INVOKE Sleep, 200                   ; delay
	  
	; Draw the slot machine runing handle7
	    mov drawPosition.x, 14
	    mov drawPosition.y, 6
	INVOKE print_slotmachine, addr m7_1, drawPosition
	INVOKE print_slotmachine, addr m7_2, drawPosition
	INVOKE print_slotmachine, addr m7_3, drawPosition
	INVOKE print_slotmachine, addr m7_4, drawPosition
	INVOKE print_slotmachine, addr m7_5, drawPosition
	INVOKE print_slotmachine, addr m7_6, drawPosition
	INVOKE print_slotmachine, addr m7_7, drawPosition
	INVOKE print_slotmachine, addr m7_8, drawPosition
	INVOKE print_slotmachine, addr m7_9, drawPosition
	INVOKE print_slotmachine, addr m7_10, drawPosition
	INVOKE print_slotmachine, addr m7_11, drawPosition
	INVOKE print_slotmachine, addr m7_12, drawPosition
	INVOKE print_slotmachine, addr m7_13, drawPosition
	INVOKE print_slotmachine, addr m7_14, drawPosition
	INVOKE print_slotmachine, addr m7_15, drawPosition
	INVOKE print_slotmachine, addr m7_16, drawPosition
	INVOKE print_slotmachine, addr m7_17, drawPosition
	INVOKE print_slotmachine, addr m7_18, drawPosition
	INVOKE print_slotmachine, addr m7_19, drawPosition
	INVOKE print_slotmachine, addr m7_20, drawPosition
	INVOKE print_slotmachine, addr m7_21, drawPosition
	INVOKE print_slotmachine, addr m7_22, drawPosition
	

	INVOKE Sleep, 200                   ; delay
	  
	; Draw the slot machine runing handle8
	    mov drawPosition.x, 14
	    mov drawPosition.y, 6
	INVOKE print_slotmachine, addr m8_1, drawPosition
	INVOKE print_slotmachine, addr m8_2, drawPosition
	INVOKE print_slotmachine, addr m8_3, drawPosition
	INVOKE print_slotmachine, addr m8_4, drawPosition
	INVOKE print_slotmachine, addr m8_5, drawPosition
	INVOKE print_slotmachine, addr m8_6, drawPosition
	INVOKE print_slotmachine, addr m8_7, drawPosition
	INVOKE print_slotmachine, addr m8_8, drawPosition
	INVOKE print_slotmachine, addr m8_9, drawPosition
	INVOKE print_slotmachine, addr m8_10, drawPosition
	INVOKE print_slotmachine, addr m8_11, drawPosition
	INVOKE print_slotmachine, addr m8_12, drawPosition
	INVOKE print_slotmachine, addr m8_13, drawPosition
	INVOKE print_slotmachine, addr m8_14, drawPosition
	INVOKE print_slotmachine, addr m8_15, drawPosition
	INVOKE print_slotmachine, addr m8_16, drawPosition
	INVOKE print_slotmachine, addr m8_17, drawPosition
	INVOKE print_slotmachine, addr m8_18, drawPosition
	INVOKE print_slotmachine, addr m8_19, drawPosition
	INVOKE print_slotmachine, addr m8_20, drawPosition
	INVOKE print_slotmachine, addr m8_21, drawPosition
	INVOKE print_slotmachine, addr m8_22, drawPosition


	INVOKE Sleep, 200                   ; delay

	; Draw the slot machine runing handle9
	    mov drawPosition.x, 14
	    mov drawPosition.y, 6
	INVOKE print_slotmachine, addr m9_1, drawPosition
	INVOKE print_slotmachine, addr m9_2, drawPosition
	INVOKE print_slotmachine, addr m9_3, drawPosition
	INVOKE print_slotmachine, addr m9_4, drawPosition
	INVOKE print_slotmachine, addr m9_5, drawPosition
	INVOKE print_slotmachine, addr m9_6, drawPosition
	INVOKE print_slotmachine, addr m9_7, drawPosition
	INVOKE print_slotmachine, addr m9_8, drawPosition
	INVOKE print_slotmachine, addr m9_9, drawPosition
	INVOKE print_slotmachine, addr m9_10, drawPosition
	INVOKE print_slotmachine, addr m9_11, drawPosition
	INVOKE print_slotmachine, addr m9_12, drawPosition
	INVOKE print_slotmachine, addr m9_13, drawPosition
	INVOKE print_slotmachine, addr m9_14, drawPosition
	INVOKE print_slotmachine, addr m9_15, drawPosition
	INVOKE print_slotmachine, addr m9_16, drawPosition
	INVOKE print_slotmachine, addr m9_17, drawPosition
	INVOKE print_slotmachine, addr m9_18, drawPosition
	INVOKE print_slotmachine, addr m9_19, drawPosition
	INVOKE print_slotmachine, addr m9_20, drawPosition
	INVOKE print_slotmachine, addr m9_21, drawPosition
	INVOKE print_slotmachine, addr m9_22, drawPosition


	INVOKE Sleep, 200                   ; delay

	; Draw the slot machine runing handle10
	    mov drawPosition.x, 14
	    mov drawPosition.y, 6
	INVOKE print_slotmachine, addr m10_1, drawPosition
	INVOKE print_slotmachine, addr m10_2, drawPosition
	INVOKE print_slotmachine, addr m10_3, drawPosition
	INVOKE print_slotmachine, addr m10_4, drawPosition
	INVOKE print_slotmachine, addr m10_5, drawPosition
	INVOKE print_slotmachine, addr m10_6, drawPosition
	INVOKE print_slotmachine, addr m10_7, drawPosition
	INVOKE print_slotmachine, addr m10_8, drawPosition
	INVOKE print_slotmachine, addr m10_9, drawPosition
	INVOKE print_slotmachine, addr m10_10, drawPosition
	INVOKE print_slotmachine, addr m10_11, drawPosition
	INVOKE print_slotmachine, addr m10_12, drawPosition
	INVOKE print_slotmachine, addr m10_13, drawPosition
	INVOKE print_slotmachine, addr m10_14, drawPosition
	INVOKE print_slotmachine, addr m10_15, drawPosition
	INVOKE print_slotmachine, addr m10_16, drawPosition
	INVOKE print_slotmachine, addr m10_17, drawPosition
	INVOKE print_slotmachine, addr m10_18, drawPosition
	INVOKE print_slotmachine, addr m10_19, drawPosition
	INVOKE print_slotmachine, addr m10_20, drawPosition
	INVOKE print_slotmachine, addr m10_21, drawPosition
	INVOKE print_slotmachine, addr m10_22, drawPosition
	; ------------------end Draw moving slot machine handle------------------


	; ------------------Draw Waterfall------------------
	; Draw first block of slot
	    mov drawPosition.x, 20
	    mov drawPosition.y, 13

	Waterfall1:
	    INVOKE WriteConsoleOutputCharacter,
	        outputHandle,                       ; console output handle
	        ADDR Slot1,                         ; pointer to the top Slot line
	        SlotWidth,                          ; size of Slot line
	        drawPosition,                       ; coordinates of first char
	        ADDR count                          ; output count

	    inc drawPosition.y                      

	    INVOKE WriteConsoleOutputCharacter,
	        outputHandle,                       ; console output handle
	        ADDR Slot2,                         ; pointer to the top Slot line
	        SlotWidth,                          ; size of Slot line
	        drawPosition,                       ; coordinates of first char
	        ADDR count                          ; output count

	    inc drawPosition.y                      

	    INVOKE WriteConsoleOutputCharacter,
	        outputHandle,                       ; console output handle
	        ADDR Slot3,                         ; pointer to the top Slot line
	        SlotWidth,                          ; size of Slot line
	        drawPosition,                       ; coordinates of first char
	        ADDR count                          ; output count

	    inc drawPosition.y                      ; 座標換到下一行位置

	    INVOKE WriteConsoleOutputCharacter,
	        outputHandle,                       ; console output handle
	        ADDR Slot4,                         ; pointer to the top Slot line
	        SlotWidth,                          ; size of Slot line
	        drawPosition,                       ; coordinates of first char
	        ADDR count                          ; output count

	    inc drawPosition.y                      

	    INVOKE WriteConsoleOutputCharacter,
	        outputHandle,                       ; console output handle
	        ADDR Slot5,                         ; pointer to the top Slot line
	        SlotWidth,                          ; size of Slot line
	        drawPosition,                       ; coordinates of first char
	        ADDR count                          ; output count

	    inc drawPosition.y                      

	    INVOKE WriteConsoleOutputCharacter,
	        outputHandle,                       ; console output handle
	        ADDR Slot6,                         ; pointer to the top Slot line
	        SlotWidth,                          ; size of Slot line
	        drawPosition,                       ; coordinates of first char
	        ADDR count                          ; output count

	    inc drawPosition.y                      

	    INVOKE WriteConsoleOutputCharacter,
	        outputHandle,                       ; console output handle
	        ADDR Slot7,                         ; pointer to the top Slot line
	        SlotWidth,                          ; size of Slot line
	        drawPosition,                       ; coordinates of first char
	        ADDR count                          ; output count

	; Draw second block of slot
	    mov drawPosition.x, 33
	    mov drawPosition.y, 13
	    INVOKE Sleep, 400

	Waterfall2:
	    INVOKE WriteConsoleOutputCharacter,
	        outputHandle,                       ; console output handle
	        ADDR Slot8,                         ; pointer to the top Slot line
	        SlotWidth,                          ; size of Slot line
	        drawPosition,                       ; coordinates of first char
	        ADDR count                          ; output count

	    inc drawPosition.y                      ; 座標換到下一行位置

	    INVOKE WriteConsoleOutputCharacter,
	        outputHandle,                       ; console output handle
	        ADDR Slot9,                         ; pointer to the top Slot line
	        SlotWidth,                          ; size of Slot line
	        drawPosition,                       ; coordinates of first char
	        ADDR count                          ; output count

	    inc drawPosition.y                      

	    INVOKE WriteConsoleOutputCharacter,
	        outputHandle,                       ; console output handle
	        ADDR Slot10,                        ; pointer to the top Slot line
	        SlotWidth,                          ; size of Slot line
	        drawPosition,                       ; coordinates of first char
	        ADDR count                          ; output count

	    inc drawPosition.y                      

	    INVOKE WriteConsoleOutputCharacter,
	        outputHandle,                       ; console output handle
	        ADDR Slot11,                        ; pointer to the top Slot line
	        SlotWidth,                          ; size of Slot line
	        drawPosition,                       ; coordinates of first char
	        ADDR count                          ; output count

	    inc drawPosition.y                      

	    INVOKE WriteConsoleOutputCharacter,
	        outputHandle,                       ; console output handle
	        ADDR Slot12,                        ; pointer to the top Slot line
	        SlotWidth,                          ; size of Slot line
	        drawPosition,                       ; coordinates of first char
	        ADDR count                          ; output count

	    inc drawPosition.y                      

	    INVOKE WriteConsoleOutputCharacter,
	        outputHandle,                       ; console output handle
	        ADDR Slot13,                        ; pointer to the top Slot line
	        SlotWidth,                          ; size of Slot line
	        drawPosition,                       ; coordinates of first char
	        ADDR count                          ; output count

	    inc drawPosition.y                      

	    INVOKE WriteConsoleOutputCharacter,
	        outputHandle,                       ; console output handle
	        ADDR Slot14,                        ; pointer to the top Slot line
	        SlotWidth,                          ; size of Slot line
	        drawPosition,                       ; coordinates of first char
	        ADDR count                          ; output count

	; Draw third block of slot
	    mov drawPosition.x, 46
	    mov drawPosition.y, 13
	    INVOKE Sleep, 400

	Waterfall3:
	    INVOKE WriteConsoleOutputCharacter,
	        outputHandle,                       ; console output handle
	        ADDR Slot15,                        ; pointer to the top Slot line
	        SlotWidth,                          ; size of Slot line
	        drawPosition,                       ; coordinates of first char
	        ADDR count                          ; output count

	    inc drawPosition.y                      ; 座標換到下一行位置

	    INVOKE WriteConsoleOutputCharacter,
	        outputHandle,                       ; console output handle
	        ADDR Slot16,                        ; pointer to the top Slot line
	        SlotWidth,                          ; size of Slot line
	        drawPosition,                       ; coordinates of first char
	        ADDR count                          ; output count

	    inc drawPosition.y                      

	    INVOKE WriteConsoleOutputCharacter,
	        outputHandle,                       ; console output handle
	        ADDR Slot17,                        ; pointer to the top Slot line
	        SlotWidth,                          ; size of Slot line
	        drawPosition,                       ; coordinates of first char
	        ADDR count                          ; output count

	    inc drawPosition.y                      

	    INVOKE WriteConsoleOutputCharacter,
	        outputHandle,                       ; console output handle
	        ADDR Slot18,                        ; pointer to the top Slot line
	        SlotWidth,                          ; size of Slot line
	        drawPosition,                       ; coordinates of first char
	        ADDR count                          ; output count

	    inc drawPosition.y                      

	    INVOKE WriteConsoleOutputCharacter,
	        outputHandle,                       ; console output handle
	        ADDR Slot19,                        ; pointer to the top Slot line
	        SlotWidth,                          ; size of Slot line
	        drawPosition,                       ; coordinates of first char
	        ADDR count                          ; output count

	    inc drawPosition.y                      

	    INVOKE WriteConsoleOutputCharacter,
	        outputHandle,                       ; console output handle
	        ADDR Slot20,                        ; pointer to the top Slot line
	        SlotWidth,                          ; size of Slot line
	        drawPosition,                       ; coordinates of first char
	        ADDR count                          ; output count

	    inc drawPosition.y                      

	    INVOKE WriteConsoleOutputCharacter,
	        outputHandle,                       ; console output handle
	        ADDR Slot21,                        ; pointer to the top Slot line
	        SlotWidth,                          ; size of Slot line
	        drawPosition,                       ; coordinates of first char
	        ADDR count                          ; output count
	; ------------------end Draw Waterfall------------------


SlotRandom:
	mov edx, 0
    mov drawPosition.x, 20
	mov drawPosition.y, 13
    INVOKE Sleep, 400
    ; random
    call Randomize                      ; reset random seed
        mov ecx, 4                      ; random the first raw
        mov eax, 5
    call RandomRange                    ; get random number (0~4)
    	inc eax							; random number變(1~5)
    	mov SlotBody[0], al             ; 記下轉到什麼


        .IF eax == 1
            INVOKE Seven, drawPosition.x, drawPosition.y
        .ENDIF

        .IF eax == 2
            INVOKE Spade, drawPosition.x, drawPosition.y
        .ENDIF

        .IF eax == 3
            INVOKE Heart, drawPosition.x, drawPosition.y
        .ENDIF

        .IF eax == 4
            INVOKE Diamond, drawPosition.x, drawPosition.y
        .ENDIF

        .IF eax == 5
            INVOKE Club, drawPosition.x, drawPosition.y
        .ENDIF


    mov drawPosition.x, 33
    mov drawPosition.y, 13
    INVOKE Sleep, 400
    ; random
    call Randomize                      ; reset random seed
        mov ecx, 4                      ; random the first raw
        mov eax, 5
    call RandomRange                    ; get random number (0~4)
    	inc eax							; random number變(1~5)
    	mov SlotBody[1], al             ; 記下轉到什麼


    	.IF eax == 1
            INVOKE Seven, drawPosition.x, drawPosition.y
        .ENDIF

        .IF eax == 2
            INVOKE Spade, drawPosition.x, drawPosition.y
        .ENDIF

        .IF eax == 3
            INVOKE Heart, drawPosition.x, drawPosition.y
        .ENDIF

        .IF eax == 4
            INVOKE Diamond, drawPosition.x, drawPosition.y
        .ENDIF

        .IF eax == 5
            INVOKE Club, drawPosition.x, drawPosition.y
        .ENDIF


    mov drawPosition.x, 46
    mov drawPosition.y, 13
    INVOKE Sleep, 400
    ; random
    call Randomize                      ; reset random seed
        mov ecx, 4                      ; random the first raw
        mov eax, 5
    call RandomRange                    ; get random number (0~4)
        inc eax							; random number變(1~5)
        mov SlotBody[2], al             ; 記下轉到什麼

        .IF eax == 1
            INVOKE Seven, drawPosition.x, drawPosition.y
        .ENDIF

        .IF eax == 2
            INVOKE Spade, drawPosition.x, drawPosition.y
        .ENDIF

        .IF eax == 3
            INVOKE Heart, drawPosition.x, drawPosition.y
        .ENDIF

        .IF eax == 4
            INVOKE Diamond, drawPosition.x, drawPosition.y
        .ENDIF

        .IF eax == 5
            INVOKE Club, drawPosition.x, drawPosition.y
        .ENDIF
	

; Find how many same number in SlotBody
    mov bh, 1   		; bh: counter
    mov bl, 0

    mov bl, SlotBody[0]
    mov ecx, 2
LCompare1:                              ; if SlotBody[0] == [1], [2]
    push ecx
    .IF SlotBody[ecx] == bl
    	inc bh
    .ENDIF
    pop ecx
    loop LCompare1
    
    mov bl, SlotBody[1]                 ; if SlotBody[1] == [2]
    .IF SlotBody[2] == bl
    	inc bh
    .ENDIF


    ; 賭金放在eax, 目前現金放在esi
    mov eax, betMoney
    mov esi, currentMoney
   
    .IF bh == 1                         ; all different
        jmp LLose                       ; lose all betMoneyStr
    .ENDIF
    
    .IF bh == 2                         ; two same
       jmp LWin							; win 1*bet
    .ENDIF
       
    .IF bh == 4                         ; all same
        
    	.IF SlotBody[2] == 5            ; if 777，win 4*bet
        	add eax, eax
        	add eax, eax
    	.ELSE
        	add eax, eax                ; others, win 2*bet
        .ENDIF

        jmp LWin
    .ENDIF

LLose:
    sub esi, eax
    mov bl, 10
    mov edi, 6
    
LtoStr:
    div bl
    add ah, 30h                 ; 1 -> '1'
    push edi
    dec edi
    mov betMoneyStr[edi], ah
    
    pop edi
    movzx ax, al
    dec edi
    cmp al, 0
    ja LtoStr
    
    mov edi, 0
    

    ; You lose~ Lose $ ...
    INVOKE WriteConsoleOutputCharacter,
	    outputHandle,               
	    ADDR youLoseStr,                       
	    SIZEOF youLoseStr,                       
	    statusPosition,                           
	    ADDR count

    mov statusPosition.x, 42
    INVOKE WriteConsoleOutputCharacter,
	    outputHandle,               
	    ADDR betMoneyStr,                       
	    betMoneyStrWidth,                       
	    statusPosition,                           
	    ADDR count

    jmp Finishing

    
LWin:
    add esi, eax
    mov bl, 10
    mov edi, 6
LtoStr1:
    div bl
    add ah, 30h                 ; 1 -> '1'
    push edi
    dec edi
    mov betMoneyStr[edi], ah
    
    pop edi
    movzx ax, al
    dec edi
    cmp al, 0
    ja LtoStr1


    ; You win! Win $ ...
    INVOKE WriteConsoleOutputCharacter,
	    outputHandle,               
	    ADDR youWinStr,                       
	    SIZEOF youWinStr,                       
	    statusPosition,                           
	    ADDR count

    mov statusPosition.x, 40
    INVOKE WriteConsoleOutputCharacter,
	    outputHandle,               
	    ADDR betMoneyStr,                       
	    betMoneyStrWidth,                       
	    statusPosition,                           
	    ADDR count


Finishing:
	mov currentMoney, esi			; 儲存目前現金

	.IF currentMoney<=0
		jmp gameover
	.ELSEIF currentMoney>0
		INVOKE sleep, 3000
		jmp SlotMachine             ; 回到SlotMachine
	.ENDIF

Gameover:	
	call Clrscr

	; 顯示破產
	mov xyPosition.x, 11
	mov xyPosition.y, 10
	INVOKE print_lose, addr lose1, xyPosition
	INVOKE print_lose, addr lose2, xyPosition
	INVOKE print_lose, addr lose3, xyPosition
	INVOKE print_lose, addr lose4, xyPosition
	INVOKE print_lose, addr lose5, xyPosition
	INVOKE print_lose, addr lose6, xyPosition
	INVOKE print_lose, addr lose7, xyPosition

	Invoke Sleep, 4000

	exit
start@0 ENDP
END start@0