; Data Transfer Examples
; moves.asm

.386
.model flat, stdcall
.stack 4096
ExitProcess PROTO, dwExitCode: DWORD

.data
val1   WORD  1000h
val2   WORD  2000h
arrayB BYTE  10h, 20h, 30h, 40h, 50h
arrayW WORD  100h, 200h, 300h
arrayD DWORD 10000h, 20000h

.code
main PROC
; Demonstrating MOVZX instruction:
    mov   bx , 0A69Bh
    movzx eax, bx                   ; EAX = 0000A69Bh
    movzx edx, bl                   ; EDX = 0000009Bh
    movzx cx , bl                   ; CX = 009Bh

; Demonstration MOVSX instruction:
    mov   bx , 0A69Bh
    movsx eax, bx                   ; EAX = FFFFA69Bh
    movsx edx, bl                   ; EDX = FFFFA69Bh
    mov   bl , 7Bh
    movsx cx , bl                   ; CX = 007Bh

; Memory-to-memory exchange:
    mov  ax  , val1                 ; AX = 1000h
    xchg ax  , val2                 ; AX = 2000h
    mov  val1, ax                   ; val1 = 2000h

; Direct-Offset Addressing (BYTE array):
    mov al, arrayB                  ; AL = 10h
    mov al, [arrayB + 1]            ; AL = 20h
    mov al, [arrayB + 2]            ; AL = 30h

; Direct-Offset Addressing (WORD array):
    mov ax, arrayW                  ; AX = 100h
    mov ax, [arrayW + 2]            ; AX = 200h

; Direct-Offset Addressing (DWORD array):
    mov eax, arrayD                 ; EAX = 10000h
    mov eax, [arrayD + 4]           ; EAX = 20000h
    mov eax, [arrayD + 4]           ; EAX = 20000h

    INVOKE ExitProcess, 0

main ENDP
END main

; Each flags
; | OV (Overflow) | UP (Direction) | EI (Interrupt) | PL (Sign) |
; | ------------- | -------------- | -------------- | --------- |
; |       00      |       00       |        01      |     00    |
; |   ZR (Zero)   | AC (Aux Carry) |   PE (Parity)  | CY (Carry)|
; | ------------- | -------------- | -------------- | --------- |
; |       01      |       00       |       01       |     00    |