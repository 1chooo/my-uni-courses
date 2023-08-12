include Irvine32.inc
printRect PROTO

BoxWidth = 70
BoxHeight = 20

.data
	windowTitleStr BYTE "Tank V.S Bogy",0
	consoleHandle    DWORD ?
	windowBound SMALL_RECT <0,0,80,25>					; 視窗大小
	score WORD 0
	changeScene BYTE 0
	levelNow BYTE 0

	xyPosition COORD <5,2>
	cellsWritten DWORD ?

	; 印開始長方形
	boxTop     BYTE 0dah, (BoxWidth - 2) DUP(0c4h), 0Bfh
	boxTop2    BYTE 0b3h, 2 DUP(' '), 0dah, (BoxWidth - 8) DUP(0c4h), 0Bfh, 2 DUP(' '), 0b3h
	boxBody    BYTE 0b3h, 2 DUP(' '), 0b3h, (BoxWidth - 8) DUP(' '), 0b3h, 2 DUP(' '), 0b3h
	boxBody2   BYTE 0b3h, 2 DUP(' '), 0b3h, 71 DUP(' '), '_ _ press any key to start _ _' , 71 DUP(' '), 0b3h, 2 DUP(' '), 0b3h
	boxBottom2 BYTE 0b3h, 2 DUP(' '), 0c0h, (BoxWidth - 8) DUP(0c4h), 0d9h, 2 DUP(' '), 0b3h
	boxBottom  BYTE 0c0h, (BoxWidth - 2) DUP(0c4h), 0d9h

	outputHandle DWORD 0
	bytesWritten DWORD 0
	count DWORD 0

	attributes0 WORD BoxWidth DUP(0ah)
	attributes1 WORD (BoxWidth-1) DUP(0ch),0bh
	attributes2 WORD BoxWidth DUP(0eh)

.code

; 印出長方形
printRect PROC
    INVOKE GetStdHandle, STD_OUTPUT_HANDLE ; Get the console ouput handle
    mov outputHandle, eax ; save console handle
    call Clrscr
    ; 畫出box的第一行
 
    INVOKE WriteConsoleOutputAttribute,
      outputHandle,
      ADDR attributes0,
      BoxWidth,
      xyPosition,
      ADDR count
 
    INVOKE WriteConsoleOutputCharacter,
       outputHandle,   ; console output handle
       ADDR boxTop,   ; pointer to the top box line
       BoxWidth,   ; size of box line
       xyPosition,   ; coordinates of first char
       ADDR count    ; output count
 
    inc xyPosition.y   ; 座標換到下一行位置

    INVOKE WriteConsoleOutputAttribute,
      outputHandle,
      ADDR attributes0,
      BoxWidth,
      xyPosition,
      ADDR count

    INVOKE WriteConsoleOutputCharacter,
       outputHandle,   ; console output handle
       ADDR boxTop2,   ; pointer to the top box line
       BoxWidth,   ; size of box line
       xyPosition,   ; coordinates of first char
       ADDR count    ; output count

    inc xyPosition.y   ; 座標換到下一行位置
 
    mov ecx, (BoxHeight-20)    ; number of lines in body
    
    L1: push ecx  ; save counter 避免invoke 有使用到這個暫存器

    INVOKE WriteConsoleOutputAttribute,
      outputHandle,
      ADDR attributes1,
      BoxWidth,
      xyPosition,
      ADDR count
   
   INVOKE WriteConsoleOutputCharacter,
       outputHandle,
       ADDR boxBody,   ; pointer to the box body
       BoxWidth,
       xyPosition,
       ADDR count 
 
    inc xyPosition.y   ; next line
    pop ecx   ; restore counter
    loop L1

    INVOKE WriteConsoleOutputAttribute,
      outputHandle,
      ADDR attributes1,
      BoxWidth,
      xyPosition,
      ADDR count
   
   INVOKE WriteConsoleOutputCharacter,
       outputHandle,
       ADDR boxBody2,   ; pointer to the box body
       BoxWidth,
       xyPosition,
       ADDR count

    inc xyPosition.y

    mov ecx, 15    ; number of lines in body
    
    L2: push ecx  ; save counter 避免invoke 有使用到這個暫存器

    INVOKE WriteConsoleOutputAttribute,
      outputHandle,
      ADDR attributes1,
      BoxWidth,
      xyPosition,
      ADDR count
   
   INVOKE WriteConsoleOutputCharacter,
       outputHandle,
       ADDR boxBody,   ; pointer to the box body
       BoxWidth,
       xyPosition,
       ADDR count 
 
    inc xyPosition.y   ; next line
    pop ecx   ; restore counter
    loop L2

    INVOKE WriteConsoleOutputAttribute,
      outputHandle,
      ADDR attributes0,
      BoxWidth,
      xyPosition,
      ADDR count

    INVOKE WriteConsoleOutputCharacter,
       outputHandle,   ; console output handle
       ADDR boxBottom2,   ; pointer to the top box line
       BoxWidth,   ; size of box line
       xyPosition,   ; coordinates of first char
       ADDR count    ; output count

    inc xyPosition.y   ; 座標換到下一行位置

    INVOKE WriteConsoleOutputAttribute,
      outputHandle,
      ADDR attributes2,
      BoxWidth,
      xyPosition,
      ADDR count
   
    INVOKE WriteConsoleOutputCharacter,
       outputHandle,
       ADDR boxBottom,   ; pointer to the bottom of the box
       BoxWidth,
       xyPosition,
       ADDR count 
     
    call WaitMsg

    mov ax,xyPosition.y   ; 座標換到下一行位置
    sub ax,17
    mov xyPosition.y, ax

    INVOKE WriteConsoleOutputAttribute,
      outputHandle,
      ADDR attributes2,
      BoxWidth,
      xyPosition,
      ADDR count
   
    INVOKE WriteConsoleOutputCharacter,
       outputHandle,
       ADDR boxBody,
       BoxWidth,
       xyPosition,
       ADDR count

    ret
printRect ENDP

main PROC
	INVOKE GetstdHandle, STD_OUTPUT_HANDLE
	mov consoleHandle, eax
	
	INVOKE SetConsoleTitle, ADDR windowTitleStr			; 設定視窗標題

	INVOKE SetConsoleWindowInfo,						; 設定視窗大小
     	consoleHandle,
     	TRUE,
     	ADDR windowBound

    INVOKE initialWindow


	call WaitMsg

ExitProgram:
	exit

main ENDP
END main