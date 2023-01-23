.386
.model flat, stdcall
.stack 4096
ExitProcess PROTO, dwExitCode: DWORD

; INC and DEC

.data
myWord WORD 1000h

.code 
inc myWord          ; myWord = 1001h
mov bx, myWord      ; BX = 1001h
dec bx              ; BX = 1000h

; ADD

.data 
var1 DWORD 10000h
var2 DWORD 20000h

.code 
mov eax, var1       ; EAX = 10000h
add eax, var2       ; EAX = 30000h

; NEG (negate) reversing all the bits

; Rval = -Xval + (Yval - Zval)

.data
Rval SDWORD ?
Xval SDWORD 26 
Yval SDWORD 30
Zval SDWORD 40

.code
mov eax, Xval
neg eax             ; EAX = -26

mov ebx, Yval
sub ebx, Zval       ; EBX = -10

add eax, ebx
mov Rval, eax       ; -36

; Status Flags
; -------------------------------------------
; Carry flag: unsigned integer overflow.
; Overflow flag: signed integer overflow 
; Zero flag: an operation produced zero
; Sign flag: an operation produced a negative result.
; Parity flag: whether or not an even number of 1 bits 
;              occurs in the least significant byte of the destination operand, 
;              immediately after an arithmetic or boolean instruction has executed
; Auxiliary flag: when a 1 bit carries out of position 3 
;                 in the least significant byte of the destination operand


; Unsigned: zero, carry, auxiliary carry

; if the result equal 0 ==> zero flag equal 1 (true)
mov ecx, 1
sub ecx, 1              ; ECX = 0, ZF = 1
mov eax, 0FFFFFFFFh
inc eax                 ; EAX = 0, ZF = 1
inc eax                 ; EAX = 1, ZF = 0
dec eax                 ; EAX = 0, ZF = 1

; when the sum exceeds the storage size of its destination operand
; ==> carry flag equal 1
mov al, 0FFh
add al, 1               ; AL = 00, CF = 1


; Comparison
mov ax, 00FFh
add ax, 1               ; AX = 0100h, CF = 0

mov ax, 0FFFFh
add ax, 1               ; AX = 0000, CF = 1

mov al, 1
sub al, 2               ; AL = FFh, CF = 1

; Auxiliary carry
; carry or borrow out of bit 3 in the destination operand
mov al, 0Fh
add al, 1               ; AC = 1

; Parity
; when the least significant byte of the destination
; has an even number of 1 bits.
mov al, 10001100b       
add al, 00000010b       ; AL = 10001110, PF = 1
sub al, 10000000b       ; AL = 00001110, PF = 0

; sign, overflow flag

; sign
mov eax, 4
sub eax, 5              ; EAX = -1, SF = 1

mov bl, 1               ; BL = 01h
sub bl, 2               ; BL = FFh (-1), SF = 1

; overflow 
mov al, +127
add al, 1               ; OF = 1

mov al, -128
sub al, 1               ; OF = 1

; NEG 

; +128 won't fit into AL, then overflow flag = 1
mov al, -128            ; AL = 10000000b
neg al                  ; AL = 10000000b, OF = 1

; -127 is valided, then overflow flag is cleared.
mov al, +127            ; AL = 01111111b
neg al                  ; AL = 10000001b, OF = 0