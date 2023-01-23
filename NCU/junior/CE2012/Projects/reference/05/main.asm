INCLUDE Irvine32.inc
main EQU start@0
WallWidth = 106
WallHeight = 30

; Game "Window" Setup:
; maxX EQU 106					
; maxY EQU 30

; Macros:
mGotoxy MACRO X:REQ, Y:REQ
	push edx
	mov	dh, Y
	mov	dl, X
	call Gotoxy
	pop	edx
ENDM

mWrite MACRO text:REQ
	LOCAL string
	.data
		string BYTE text, 0
	.code
		push edx
		mov	edx, OFFSET string
		call WriteString
		pop	edx
ENDM

mRead MACRO char:REQ
	push ecx
	push edx
L0_mRead:
	mGotoxy 54, 24
	mWrite "               "
	mGotoxy 54, 24
	mov	edx, OFFSET char
	mov	ecx, SIZEOF char
	call ReadString		; read in some thing
	cmp eax, 0
	je L0_mRead			; read until it is valid
	cmp eax, 13
	jg L0_mRead			; read until it is valid
	pop edx
	pop ecx
ENDM

mWriteString MACRO buffer:REQ
	push edx
	mov	edx, OFFSET buffer
	call WriteString	; print out something
	pop	edx
ENDM

.data
choice BYTE 0
endchoice BYTE 0
speed DWORD 0
batLength DWORD 0	; 18, 14, 10 ; bat location offset on the window
batLength1 DWORD 0	;  9,  7,  5 ; bat real width
batLength2 DWORD 0	;  4,  3,  2 ; bat half width the offset between ball
score SDWORD 4 DUP(?)
deltascore DWORD 0
Nameofplayer BYTE 4 DUP(13 DUP(?))
TmpName BYTE 13 DUP(?)
TmpName1 BYTE "             "

outputHandle DWORD 0
bytesWritten DWORD 0
count DWORD 0
xyPosition COORD <0,0>
cellsWritten DWORD ?
Plate BYTE 16 DUP(' ')
whiteball BYTE '.'
Horwall BYTE WallWidth DUP('=')
Verwall BYTE '=', (WallWidth - 2) DUP(' '), '='
Botwall BYTE WallWidth DUP('=')
Titlewall BYTE 2 DUP('        ')

attributes0 WORD WallWidth DUP(0F1h)
attributes1 WORD 0F1h,(WallWidth-2) DUP(00h), 0F1h
attributes2 WORD WallWidth DUP(0F1h)
attributes3 WORD 4 DUP(00h), 4 DUP(033h)
attributes4 WORD 4 DUP(033h), 4 DUP(00h)
attributes5 WORD (LENGTHOF Plate) DUP(055h)
attributes6 WORD 1 DUP(00Fh)

; main proc variable need to reset everytime when call the game
VK_LEFT	EQU	25h
VK_RIGHT EQU 27h
windowWidth WORD ?
windowHeight WORD ?
boxBat BYTE "▬▬"
boxBall BYTE "•"
boxWall1 BYTE "■"
boxWall2 BYTE "□"
boxSpace BYTE "  "
titleStr BYTE "Brick Break",0
inputStr BYTE ?

State BYTE 1800 DUP(?)	; 0 is Space, 1 is •, 2 is ▬, 3 is ■ or □
win BYTE 0				; 0 continue 1 lose 2 win

inputHandle DWORD 0
consoleInfo CONSOLE_SCREEN_BUFFER_INFO <>
notUsed DWORD ?
lpReserved DWORD 0
ballxyPosition COORD <?, ?>
batxyPosition COORD <?, ?>
wallxyPosition COORD <?, ?>
ballxDir SWORD 2	;x : -2 is left 2 is right
ballyDir SWORD -1	;y : -1 is up 1 is down

PreSet PROTO, bWidth:PTR WORD, bHeight:PTR WORD, bState:PTR BYTE
FillTheWindows PROTO, bWidth:WORD, bHeight:WORD, bState:PTR BYTE

.code
main PROC
	call StartGame	; the main just do calling StartGame proc
	ret
main ENDP

Game PROC
	INVOKE SetConsoleTitle, ADDR titleStr	; set the title of the console
	INVOKE GetStdHandle, STD_OUTPUT_HANDLE	; Get the console output handle
	mov outputHandle, eax					; save console output handle
	INVOKE GetStdHandle, STD_INPUT_HANDLE	; Get the console input handle
	mov inputHandle, eax					; save console input handle
	; get the console screen buffer info and set it in var consoleInfo
	INVOKE GetConsoleScreenBufferInfo, outputHandle, ADDR consoleInfo
	call Clrscr

	mov win, 0
	mov score, 0
	mov ballxyPosition.X, 60
	mov ballxyPosition.Y, 28
	mov eax, 60
	mov ebx, batLength1
	dec ebx
	sub eax, ebx
	mov batxyPosition.X, ax	; may have bug
	mov batxyPosition.Y, 29
	mov ballxDir, 2
	mov ballyDir, -1
	; preset width & height & all the state of the printable position
	INVOKE PreSet, OFFSET windowWidth, OFFSET windowHeight, OFFSET State
	; fill the console window by the state
	INVOKE FillTheWindows, windowWidth, windowHeight, OFFSET State
L0:
	mov eax, 50			; sleep, to allow OS to time slice
	call ReadKey		; look for keyboard input
	jz L1				; no key pressed yet
	cmp dx, VK_LEFT
	jne L0_5
	; movzx eax, al
	; call WriteDec
	; call WaitMsg
	; loop to solve the bat movement problem
	mov ecx, 2
L0_1:
	dec ecx
	cmp batxyPosition.X, 0
	jle L0_1_1
	jmp L0_1_2
L0_1_1:
	mov ecx, -1
	jmp L0_1_3
L0_1_2:
	push ecx
	sub batxyPosition.X, 2
	mov esi, OFFSET State
	add esi, 1740			; 1740 = 29 * 60
	movsx eax, batxyPosition.X
	xor edx, edx
	mov ebx, 2
	div ebx
	add esi, eax
	mov BYTE PTR [esi], 2
	; set the bat
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,		; output handle
		ADDR boxBat,		; pointer to the character to be written
		LENGTHOF boxBat,	; size of buffer
		batxyPosition,		; coordinates of first char
		ADDR count			; output count
	mov eax, batLength
	add batxyPosition.X, ax	; may have bug
	add esi, batLength1
	mov BYTE PTR [esi], 0
	; remove the bat
	add batxyPosition.X, 2
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,		; output handle
		ADDR boxSpace,		; pointer to the character to be written
		LENGTHOF boxSpace,	; size of buffer
		batxyPosition,		; coordinates of first char
		ADDR count			; output count
	sub batxyPosition.X, 2
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,		; output handle
		ADDR boxSpace,		; pointer to the character to be written
		LENGTHOF boxSpace,	; size of buffer
		batxyPosition,		; coordinates of first char
		ADDR count			; output count
	sub batxyPosition.X, 2
	mov eax, batLength
	sub eax, 2
	sub batxyPosition.X, ax	; may have bug
	pop ecx
L0_1_3:
	cmp ecx, 0
	jge L0_1
L0_5:
	cmp dx, VK_RIGHT
	jne L1
	; movzx eax, al
	; call WriteDec
	; call WaitMsg
	mov ecx, 2
L0_6:
	dec ecx
	mov ax, windowWidth
	mov ebx, batLength	; bat's width
	sub ax, bx			; may have bug
	sub ax, 1			; make sur no to overflow
	cmp batxyPosition.X, ax
	jge L0_6_1
	jmp L0_6_2
L0_6_1:
	mov ecx, -1
	jmp L0_6_3
L0_6_2:
	push ecx
	mov esi, OFFSET State
	add esi, 1740			; 1740 = 29 * 60
	movsx eax, batxyPosition.X
	xor edx, edx
	mov ebx, 2
	div ebx
	add esi, eax
	mov BYTE PTR [esi], 0
	; remove the bat
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,		; output handle
		ADDR boxSpace,		; pointer to the character to be written
		LENGTHOF boxSpace,	; size of buffer
		batxyPosition,		; coordinates of first char
		ADDR count			; output count
	mov eax, batLength
	add batxyPosition.X, ax	; may have bug
	add esi, batLength1
	mov BYTE PTR [esi], 2
	; set the bat
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,		; output handle
		ADDR boxBat,		; pointer to the character to be written
		LENGTHOF boxBat,	; size of buffer
		batxyPosition,		; coordinates of first char
		ADDR count			; output count
	mov eax, batLength
	sub eax, 2
	sub batxyPosition.X, ax	; may have bug
	pop ecx
L0_6_3:
	cmp ecx, 0
	jge L0_6
L1:
	; remove the ball
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,		; output handle
		ADDR boxSpace,		; pointer to the character to be written
		LENGTHOF boxSpace,	; size of buffer
		ballxyPosition,		; coordinates of first char
		ADDR count			; output count
	; test for right line
	mov ax, windowWidth
	sub ax, 2			; the printable charactor is place in 2 space
	mov bx, ballxyPosition.X
	add bx, ballxDir
	cmp bx, ax
	jle L2_1
	mov ax, ballxDir
	mov bx, -1
	mul bx
	mov ballxDir, ax
	jmp L2
L2_1:
	; test for left line
	cmp bx, 0
	jge L2
	mov ax, ballxDir
	mov bx, -1
	mul bx
	mov ballxDir, ax
L2:
	; test for bottom line
	mov ax, windowHeight
	sub ax, 1
	mov bx, ballxyPosition.Y
	add bx, ballyDir
	cmp bx, ax
	jle L3_1
	mov win, 1			; set state to lose
	; mov ax, ballyDir
	; mov bx, -1
	; mul bx
	; mov ballyDir, ax
	jmp L6
L3_1:
	; test for top line
	cmp bx, 0
	jge L3and4
	mov ax, ballyDir
	mov bx, -1
	mul bx
	mov ballyDir, ax
L3and4:
	; check left or right
	mov esi, OFFSET State
	movsx eax, ballxyPosition.X
	movsx edx, ballxDir
	add eax, edx
	xor edx, edx
	mov ebx, 2
	div ebx
	add esi, eax
	movsx eax, ballxyPosition.Y
	movsx ebx, windowWidth
	mul ebx
	xor edx, edx
	mov ebx, 2
	div ebx
	add esi, eax
	movsx eax, BYTE PTR [esi]
	; take out the state of the place next to the ball
	cmp eax, 3
	je L3
	; check up or down
	mov esi, OFFSET State
	movsx eax, ballxyPosition.X
	xor edx, edx
	mov ebx, 2
	div ebx
	add esi, eax
	movsx eax, ballxyPosition.Y
	movsx edx, ballyDir
	add eax, edx
	movsx ebx, windowWidth
	mul ebx
	xor edx, edx
	mov ebx, 2
	div ebx
	add esi, eax
	movsx eax, BYTE PTR [esi]
	; take out the state of the place next to the ball
	cmp eax, 3
	je L3
	; check the horizontal and vertical direction's wall
	mov esi, OFFSET State
	movsx eax, ballxyPosition.X
	movsx edx, ballxDir
	add eax, edx
	xor edx, edx
	mov ebx, 2
	div ebx
	add esi, eax
	movsx eax, ballxyPosition.Y
	movsx edx, ballyDir
	add eax, edx
	movsx ebx, windowWidth
	mul ebx
	xor edx, edx
	mov ebx, 2
	div ebx
	add esi, eax
	movsx eax, BYTE PTR [esi]
	; take out the state of the place next to the ball
	cmp eax, 3
	jne L3
	mov BYTE PTR [esi], 0
	; calculate the wall's place
	mov ax, ballxyPosition.X
	add ax, ballxDir
	mov wallxyPosition.X, ax
	mov bx, ballxyPosition.Y
	add bx, ballyDir
	mov wallxyPosition.Y, bx
	; remove the wall
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,		; output handle
		ADDR boxSpace,		; pointer to the character to be written
		LENGTHOF boxSpace,	; size of buffer
		wallxyPosition,		; coordinates of first char
		ADDR count			; output count
	cmp ballxDir, 0
	jg L3and4_1
	; on the left
	dec esi
	mov BYTE PTR [esi], 0
	jmp L3and4_2
L3and4_1:
	; on the right
	inc esi
	mov BYTE PTR [esi], 0
L3and4_2:
	; calculate the next wall's place
	mov ax, ballxyPosition.X
	add ax, ballxDir
	add ax, ballxDir			; do second time
	mov wallxyPosition.X, ax
	mov bx, ballxyPosition.Y
	add bx, ballyDir
	mov wallxyPosition.Y, bx
	; remove the wall
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,		; output handle
		ADDR boxSpace,		; pointer to the character to be written
		LENGTHOF boxSpace,	; size of buffer
		wallxyPosition,		; coordinates of first char
		ADDR count			; output count
	mov eax, deltascore
	add score, eax
	mov ax, ballxDir
	mov bx, -1
	mul bx
	mov ballxDir, ax
	mov ax, ballyDir
	mov bx, -1
	mul bx
	mov ballyDir, ax
L3:
	; check the horizontal direction's wall
	mov esi, OFFSET State
	movsx eax, ballxyPosition.X
	movsx edx, ballxDir
	add eax, edx
	xor edx, edx
	mov ebx, 2
	div ebx
	add esi, eax
	movsx eax, ballxyPosition.Y
	movsx ebx, windowWidth
	mul ebx
	xor edx, edx
	mov ebx, 2
	div ebx
	add esi, eax
	movsx eax, BYTE PTR [esi]
	; take out the state of the place next to the ball
	cmp eax, 3
	jne L4_1
	mov BYTE PTR [esi], 0
	; calculate the wall's place
	mov ax, ballxyPosition.X
	add ax, ballxDir
	mov wallxyPosition.X, ax
	mov bx, ballxyPosition.Y
	mov wallxyPosition.Y, bx
	; remove the wall
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,		; output handle
		ADDR boxSpace,		; pointer to the character to be written
		LENGTHOF boxSpace,	; size of buffer
		wallxyPosition,		; coordinates of first char
		ADDR count			; output count
	cmp ballxDir, 0
	jg L3_2
	; on the left
	dec esi
	mov BYTE PTR [esi], 0
	jmp L3_3
L3_2:
	; on the right
	inc esi
	mov BYTE PTR [esi], 0
L3_3:
	; calculate the next wall's place
	mov ax, ballxyPosition.X
	add ax, ballxDir
	add ax, ballxDir			; do second time
	mov wallxyPosition.X, ax
	mov bx, ballxyPosition.Y
	mov wallxyPosition.Y, bx
	; remove the wall
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,		; output handle
		ADDR boxSpace,		; pointer to the character to be written
		LENGTHOF boxSpace,	; size of buffer
		wallxyPosition,		; coordinates of first char
		ADDR count			; output count
	mov eax, deltascore
	add score, eax
	mov ax, ballxDir
	mov bx, -1
	mul bx
	mov ballxDir, ax
L4_1:
	; check the vertical direction's wall
	mov esi, OFFSET State
	movsx eax, ballxyPosition.X
	xor edx, edx
	mov ebx, 2
	div ebx
	add esi, eax
	movsx eax, ballxyPosition.Y
	movsx edx, ballyDir
	add eax, edx
	movsx ebx, windowWidth
	mul ebx
	xor edx, edx
	mov ebx, 2
	div ebx
	add esi, eax
	movsx eax, BYTE PTR [esi]
	; take out the state of the place next to the ball
	cmp eax, 3
	jne L4
	mov BYTE PTR [esi], 0
	; calculate the wall's place
	mov ax, ballxyPosition.X
	mov wallxyPosition.X, ax
	mov bx, ballxyPosition.Y
	add bx, ballyDir
	mov wallxyPosition.Y, bx
	; remove the wall
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,		; output handle
		ADDR boxSpace,		; pointer to the character to be written
		LENGTHOF boxSpace,	; size of buffer
		wallxyPosition,		; coordinates of first char
		ADDR count			; output count
	;  calculate the another wall's place
	mov edi, OFFSET State
	mov eax, esi
	sub eax, edi
	xor edx, edx
	; mov eax, esi
	mov ebx, 2
	div ebx
	cmp edx, 0	; check which type of wall
	je L4_2
	dec esi
	mov BYTE PTR [esi], 0
	; remain 1 the place now is on the right
	mov ax, ballxyPosition.X
	sub ax, 2
	mov wallxyPosition.X, ax
	mov bx, ballxyPosition.Y
	add bx, ballyDir
	mov wallxyPosition.Y, bx
	; remove the wall
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,		; output handle
		ADDR boxSpace,		; pointer to the character to be written
		LENGTHOF boxSpace,	; size of buffer
		wallxyPosition,		; coordinates of first char
		ADDR count			; output count
	jmp L4_3
L4_2:
	inc esi
	mov BYTE PTR [esi], 0
	; remain 0 the place now is on the left
	mov ax, ballxyPosition.X
	add ax, 2
	mov wallxyPosition.X, ax
	mov bx, ballxyPosition.Y
	add bx, ballyDir
	mov wallxyPosition.Y, bx
	; remove the wall
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,		; output handle
		ADDR boxSpace,		; pointer to the character to be written
		LENGTHOF boxSpace,	; size of buffer
		wallxyPosition,		; coordinates of first char
		ADDR count			; output count
L4_3:
	mov eax, deltascore
	add score, eax
	mov ax, ballyDir
	mov bx, -1
	mul bx
	mov ballyDir, ax
L4:
	; check the bat
	mov esi, OFFSET State
	movsx eax, ballxyPosition.X
	xor edx, edx
	mov ebx, 2
	div ebx
	add esi, eax
	movsx eax, ballxyPosition.Y
	movsx edx, ballyDir
	; check the ball's direction
	cmp edx, 1
	jne L5
	add eax, edx
	movsx ebx, windowWidth
	mul ebx
	xor edx, edx
	mov ebx, 2
	div ebx
	add esi, eax
	movsx eax, BYTE PTR [esi]
	; take out the state of the place next to the ball
	cmp eax, 2
	jne L5
	mov ax, ballyDir
	mov bx, -1
	mul bx
	mov ballyDir, ax
L5:
	; set the ball's next place
	mov ax, ballxyPosition.X
	add ax, ballxDir
	mov ballxyPosition.X, ax
	mov bx, ballxyPosition.Y
	add bx, ballyDir
	mov ballxyPosition.Y, bx
	; print out the ball
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,		; output handle
		ADDR boxBall,		; pointer to the character to be written
		LENGTHOF boxBall,	; size of buffer
		ballxyPosition,		; coordinates of first char
		ADDR count			; output count
	; check things before loop
	INVOKE Sleep, speed		; set the time to wait arround 45-150
	mov eax, 300
	mov ebx, deltascore
	mul ebx
	cmp score, eax			; changing to random therefore it become weird
	jl L6
	mov win, 2
L6:
	cmp win, 0		; check win or lose or continue
	je L0
	mGotoxy 45, 23
	call WaitMsg
	ret
Game ENDP

PreSet PROC, bWidth:PTR WORD, bHeight:PTR WORD, bState:PTR BYTE
	; get the window width
	mov ax, consoleInfo.srWindow.Right
	mov dx, consoleInfo.srWindow.Left
	sub ax, dx
	inc ax
	mov esi, bWidth
	mov WORD PTR [esi], ax
	; get the window height
	mov bx, consoleInfo.srWindow.Bottom
	mov dx, consoleInfo.srWindow.Top
	sub bx, dx
	inc bx
	mov edi, bHeight
	mov WORD PTR [edi], bx

	; set wall
	mov edi, bWidth
	movsx eax, WORD PTR [edi]
	mov ebx, 10
	mul ebx
	xor edx, edx
	mov ecx, 4
	div ecx
	mov ecx, eax
	mov esi, bState
	call Randomize
L01:
	call Random32		; make the brick random
	cmp eax, 0C0000000h
	ja L01_1			; 3/4 have brick 1/4 doesn't have brick
	mov BYTE PTR [esi], 3
	inc esi
	mov BYTE PTR [esi], 3
	inc esi
	jmp L01_2
L01_1:
	mov BYTE PTR [esi], 0
	inc esi
	mov BYTE PTR [esi], 0
	inc esi
L01_2:
	loop L01
	; set space
	mov edi, bWidth
	movsx eax, WORD PTR [edi]
	xor edx, edx
	mov ebx, 20
	mul ebx
	mov ecx, 2
	div ecx
	mov ecx, eax
L02:
	mov BYTE PTR [esi], 0
	inc esi
	loop L02
	mov esi, bState
	add esi, 1710		; 1710 = 28 * 60 + 30
	mov BYTE PTR [esi], 1
	mov eax, 60
	sub eax, batLength2
	add esi, eax
	mov ecx, batLength1
L03:
	mov BYTE PTR [esi], 2	; set the bat
	inc esi
	loop L03
	ret
PreSet ENDP

FillTheWindows PROC, bWidth:WORD, bHeight:WORD, bState:PTR BYTE
	movsx eax, bWidth
	movsx ebx, bHeight
	mul ebx
	xor edx, edx
	mov ecx, 2
	div ecx
	mov ecx, eax	; set the total loop time
	mov esi, bState	; point to the first place
L1:	push ecx	; save ecx to stack
	; take out the state of the printable position
	movsx eax, BYTE PTR [esi]
	cmp eax, 0	; if it is space
	jne L2
	; print Space
	INVOKE WriteConsole,
		outputHandle,		; output handle
		ADDR boxSpace,		; pointer to buffer
		LENGTHOF boxSpace,	; size of buffer
		ADDR count,			; output count
		lpReserved			; (not used)
	jmp L5
L2:	cmp eax, 1	; if it is ball
	jne L3
	; print Ball
	INVOKE WriteConsole,
		outputHandle,		; output handle
		ADDR boxBall,		; pointer to buffer
		LENGTHOF boxBall,	; size of buffer
		ADDR count,			; output count
		lpReserved			; (not used)
	jmp L5
L3:	cmp eax, 2	; if it is bat
	jne L4
	; print Bat
	INVOKE WriteConsole,
		outputHandle,		; output handle
		ADDR boxBat,		; pointer to buffer
		LENGTHOF boxBat,	; size of buffer
		ADDR count,			; output count
		lpReserved			; (not used)
	jmp L5
L4:	cmp eax, 3	; if it is wall
	jne L5
	mov edi, bState
	mov eax, esi
	sub eax, edi
	xor edx, edx
	; mov eax, esi
	mov ebx, 4
	div ebx
	cmp edx, 2	; check which type of wall
	jl L6
	; print Wall1
	INVOKE WriteConsole,
		outputHandle,		; output handle
		ADDR boxWall1,		; pointer to buffer
		LENGTHOF boxWall1,	; size of buffer
		ADDR count,			; output count
		lpReserved			; (not used)
	jmp L5
L6:	; print Wall2
	INVOKE WriteConsole,
		outputHandle,		; output handle
		ADDR boxWall2,		; pointer to buffer
		LENGTHOF boxWall2,	; size of buffer
		ADDR count,			; output count
		lpReserved			; (not used)
L5:	pop ecx	; pop back ecx
	inc esi	; point to next printable position
	dec ecx	; set loop time
	jnz L1	; jump (loop too far so do jump)
	ret
FillTheWindows ENDP

Walloutput PROC								; Walls to screen
	INVOKE GetStdHandle, STD_OUTPUT_HANDLE	; get the console ouput handle
	mov outputHandle, eax					; save console handle
	call Clrscr
	; output first line
	INVOKE WriteConsoleOutputAttribute,
		outputHandle,			; output handle                  
		ADDR attributes0,		; write attributes
		WallWidth,				; number of cells
		xyPosition,				; first coordinates
		ADDR cellsWritten		; numbers of written
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,					; console output handle
		ADDR Horwall,					; pointer to the top box line
		WallWidth,						; size of box line
		xyPosition,						; first coordinate
		ADDR count
	inc xyPosition.Y 
	mov ecx, (WallHeight-2)	; number of lines in body
L1:	push ecx	; save counter
	INVOKE WriteConsoleOutputAttribute,
		outputHandle,
		ADDR attributes1,
		WallWidth,
		xyPosition,
		ADDR cellsWritten
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,
		ADDR Verwall,    
		WallWidth,
		xyPosition,
		ADDR count 
	inc xyPosition.Y	; next line
	pop ecx				; restore counter
	loop L1
	INVOKE WriteConsoleOutputAttribute,
		outputHandle,
		ADDR attributes2,
		WallWidth,
		xyPosition,
		ADDR cellsWritten
	; draw bottom of the box
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,
		ADDR Botwall,					; pointer to the bottom of the box
		WallWidth,
		xyPosition,
		ADDR count
	sub xyPosition.Y, (WallHeight - 1)	; let xyPosition back to <0,1>
	ret
Walloutput ENDP

TitleScreen PROC
	; this part use many INVOKE to fill the window with pictures
	call ClrScr
	call Walloutput
	mov xyPosition.X, 1
	mov xyPosition.Y, 2
	mov ecx, 13
L1:	push ecx
	INVOKE WriteConsoleOutputAttribute,
		outputHandle,
		ADDR attributes3,
		8,
		xyPosition,
		ADDR cellsWritten
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,
		ADDR Titlewall,    
		8,
		xyPosition,
		ADDR count 
	add xyPosition.X, 8
	pop ecx                          
	loop L1
	inc xyPosition.Y
	sub xyPosition.X, 104
	mov ecx, 13
L2:	push ecx                                      
	INVOKE WriteConsoleOutputAttribute,
		outputHandle,
		ADDR attributes4,
		8,
		xyPosition,
		ADDR cellsWritten
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,
		ADDR Titlewall,    
		8,
		xyPosition,
		ADDR count 
	add xyPosition.X, 8
	pop ecx                                 
	loop L2
	inc xyPosition.Y
	sub xyPosition.X, 104
	mov ecx, 13
L3:	push ecx                                
	INVOKE WriteConsoleOutputAttribute,
		outputHandle,
		ADDR attributes3,
		8,
		xyPosition,
		ADDR cellsWritten
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,
		ADDR Titlewall,    
		8,
		xyPosition,
		ADDR count 
	add xyPosition.X, 8
	pop ecx                                     
	loop L3
	mGotoxy 21, 6
	mWrite	"  ___                      _         ____   __  "	
	mGotoxy 21, 7
	mWrite	" |___/  _ __  ___   __ _  | |__     /  __\ |  |  ___   _ __   ___"
	mGotoxy 21, 8
	mWrite	" |   \ | '_/ / -_) / _` | | / /     | |__  |  | | _ | | '. | / -_)"
	mGotoxy 21, 9
	mWrite	" |___/ |_|   \___| \__,_| |_\_\     \____/ |__| |___| |_||_| \___|"		
	sub xyPosition.X, 104
	mov xyPosition.Y, 12
	mov ecx, 13
L4:	push ecx                                
	INVOKE WriteConsoleOutputAttribute,
		outputHandle,
		ADDR attributes4,
		8,
		xyPosition,
		ADDR cellsWritten
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,
		ADDR Titlewall,    
		8,
		xyPosition,
		ADDR count 
	add xyPosition.X, 8
	pop ecx                                     
	loop L4
	sub xyPosition.X, 104
	inc xyPosition.Y
	mov ecx, 13
L5:	push ecx                                
	INVOKE WriteConsoleOutputAttribute,
		outputHandle,
		ADDR attributes3,
		8,
		xyPosition,
		ADDR cellsWritten
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,
		ADDR Titlewall,    
		8,
		xyPosition,
		ADDR count 
	add xyPosition.X, 8
	pop ecx                                     
	loop L5
	sub xyPosition.X, 104
	inc xyPosition.Y
	mov ecx, 13
L6:	push ecx                                
	INVOKE WriteConsoleOutputAttribute,
		outputHandle,
		ADDR attributes4,
		8,
		xyPosition,
		ADDR cellsWritten
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,
		ADDR Titlewall,    
		8,
		xyPosition,
		ADDR count 
	add xyPosition.X, 8
	pop ecx                                     
	loop L6
	mov xyPosition.X, 75
	mov xyPosition.Y, 28
	INVOKE WriteConsoleOutputAttribute,
		outputHandle,
		ADDR attributes5,
		LENGTHOF Plate,
		xyPosition,
		ADDR cellsWritten
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,
		ADDR Plate,    
		LENGTHOF Plate,
		xyPosition,
		ADDR count
	mov xyPosition.X, 25
	mov xyPosition.Y, 20
	INVOKE WriteConsoleOutputAttribute,
		outputHandle,
		ADDR attributes6,
		LENGTHOF whiteball,
		xyPosition,
		ADDR cellsWritten
	INVOKE WriteConsoleOutputCharacter,
		outputHandle,
		ADDR whiteball,    
		LENGTHOF whiteball,
		xyPosition,
		ADDR count
	mov xyPosition.X, 1
	mov xyPosition.Y, 0

	mGotoxy 40, 25
	call WaitMsg
	mGotoxy 0, 0    
	ret
TitleScreen ENDP

Menu PROC
L0:
	; show the start menu
	call ClrScr
	call Walloutput
	mGotoxy 46, 5
	mWrite "~ Menu  Menu ~"
	mGotoxy 46, 12
	mWrite "~ Difficulty ~"
	mGotoxy 40, 14
	mWrite "1.Easy"
	mGotoxy 48, 14
	mWrite "2.Normal"
	mGotoxy 58, 14
	mWrite "3.Hard"
	mGotoxy 44, 16 
	mWrite "Your Selection: "
	call ReadChar
	mov choice, al		;get difficult choice
	call WriteChar
	cmp choice, '1'
	jne L1
	mov speed, 100
	mov batLength, 18	; 18 = 9 * 2
	mov batLength1, 9
	mov batLength2, 4
	mov deltascore, 1
	jmp L3
L1:
	cmp choice, '2'
	jne L2
	mov speed, 70
	mov batLength, 14	; 14 = 7 * 2
	mov batLength1, 7
	mov batLength2, 3
	mov deltascore, 3
	jmp L3
L2:
	cmp choice, '3'
	jne L3_5
	mov speed, 50
	mov batLength, 10	; 10 = 5 * 2
	mov batLength1, 5
	mov batLength2, 2
	mov deltascore, 5
	jmp L3
L3_5:
	jmp L0
L3:
	INVOKE sleep, speed		; set the sleep time
	mGotoxy 43, 24
	mWrite "Your Name: "
	mRead Nameofplayer	; read the input
	mGotoxy 0, 0	
	call ClrScr		
	ret
Menu ENDP

Gameover PROC
L0:
	call ClrScr
	call Walloutput
	; print ou top of the window
	mGotoxy 46, 5
	cmp win, 2
	je L1
	jmp L2
L1:
	mWrite "!~~~! Win !~~~!"
	jmp L3
L2:
	mWrite "!! Game Over !!"
L3:
	; print out the scorebroad
	mGotoxy 30, 8
	mWrite "Your Name"
	mGotoxy 30, 9
	mWritestring Nameofplayer
	mGotoxy 65, 8
	mWrite "Your Score"
	mGotoxy 65, 9
	mov eax, score
	call Writeint
	cld
	mov ecx, 13
	mov esi, OFFSET TmpName1
	mov edi, OFFSET TmpName
	rep movsb
	mov eax, score
	cmp eax, score[12]	; the third num
	jle L4
	mov score[12], eax
	cld
	mov ecx, 13
	mov esi, OFFSET Nameofplayer
	mov edi, OFFSET Nameofplayer[39]
	rep movsb
	cmp eax, score[8]	; the second num
	jle L4
	mov ebx, score[8]
	mov score[8], eax
	mov score[12], ebx
	cld
	mov ecx, 13
	mov esi, OFFSET Nameofplayer[26]
	mov edi, OFFSET TmpName
	rep movsb
	cld
	mov ecx, 13
	mov esi, OFFSET Nameofplayer
	mov edi, OFFSET Nameofplayer[26]
	rep movsb
	cld
	mov ecx, 13
	mov esi, OFFSET TmpName
	mov edi, OFFSET Nameofplayer[39]
	rep movsb
	cld
	mov ecx, 13
	mov esi, OFFSET TmpName1
	mov edi, OFFSET TmpName
	rep movsb
	cmp eax, score[4]	; the first num
	jle L4
	mov ebx, score[4]
	mov score[4], eax
	mov score[8], ebx
	cld
	mov ecx, 13
	mov esi, OFFSET Nameofplayer[13]
	mov edi, OFFSET TmpName
	rep movsb
	cld
	mov ecx, 13
	mov esi, OFFSET Nameofplayer
	mov edi, OFFSET Nameofplayer[13]
	rep movsb
	cld
	mov ecx, 13
	mov esi, OFFSET TmpName
	mov edi, OFFSET Nameofplayer[26]
	rep movsb
	cld
	mov ecx, 13
	mov esi, OFFSET TmpName1
	mov edi, OFFSET TmpName
	rep movsb
L4:
	; print out middle of the window
	mGotoxy 48, 13
	mWrite "ScoreBoard"
	mGotoxy 33, 14
	mWrite "Name"
	mGotoxy 68, 14
	mWrite "Score"
	; doing swap of the score
	cmp score[4], 0
	jle L4_1
	mGotoxy 33, 15
	mWritestring Nameofplayer[13]
	mGotoxy 68, 15
	mov eax, score[4]
	call Writeint
L4_1:
	; doing swap of the score
	cmp score[8], 0
	jle L4_2
	mGotoxy 33, 16
	mWritestring Nameofplayer[26]
	mGotoxy 68, 16
	mov eax, score[8]
	call Writeint
L4_2:
	; doing swap of the score
	cmp score[12], 0
	jle L4_3
	mGotoxy 33, 17
	mWritestring Nameofplayer[39]
	mGotoxy 68, 17
	mov eax, score[12]
	call Writeint
L4_3:
	; print out the buttom window
	mGotoxy 45, 22
	mWrite "(1) Back to Menu!"
	mGotoxy 45, 24
	mWrite "(2) Exit..."
	mGotoxy 45, 26
	mWrite "Your choose: "
	call ReadChar
	mov endchoice, al	; get input whether need to play again
	call WriteChar
	cmp endchoice, '1'
	je L5
	cmp endchoice, '2'
	jne L0
	call Clrscr
	exit
L5:
	ret
Gameover ENDP
	
StartGame PROC										
	call TitleScreen	; show the start picture
X1:	
	call Menu		; show the menu
	call Game		; get into the game
	call clrscr		; clear the output on window
 	call Gameover	; determine whether the game is over
	jmp X1			; if not loop
	ret
StartGame ENDP
END main