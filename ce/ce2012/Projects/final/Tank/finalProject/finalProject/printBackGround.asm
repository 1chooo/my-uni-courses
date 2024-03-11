INCLUDE Irvine32.inc
EXTERN lab1_01@0:PROC

BoxWidth = 180
BoxHeight = 40
 
.data
boxTop     BYTE 0dah, (BoxWidth - 2) DUP(0c4h), 0Bfh
boxTop2    BYTE 0b3h, 2 DUP(' '), 0dah, (BoxWidth - 8) DUP(0c4h), 0Bfh, 2 DUP(' '), 0b3h
boxBody    BYTE 0b3h, 2 DUP(' '), 0b3h, (BoxWidth - 8) DUP(' '), 0b3h, 2 DUP(' '), 0b3h
boxBody2   BYTE 0b3h, 2 DUP(' '), 0b3h, 71 DUP(' '), '_ _ press any key to start _ _' , 71 DUP(' '), 0b3h, 2 DUP(' '), 0b3h
boxBottom2 BYTE 0b3h, 2 DUP(' '), 0c0h, (BoxWidth - 8) DUP(0c4h), 0d9h, 2 DUP(' '), 0b3h
boxBottom  BYTE 0c0h, (BoxWidth - 2) DUP(0c4h), 0d9h
 
outputHandle DWORD 0
bytesWritten DWORD 0
count DWORD 0
xyPosition COORD <5,5>
 
cellsWritten DWORD ?
attributes0 WORD BoxWidth DUP(0ah)
attributes1 WORD (BoxWidth-1) DUP(0ch),0bh
attributes2 WORD BoxWidth DUP(0eh)
          
 
.code
printBackGround PROC
 
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

    call lab1_01@0
    exit
printBackGround ENDP
END printBackGround