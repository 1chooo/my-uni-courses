.386
.model flat, stdcall
.stack 4096
ExitProcess PROTO, dwExitCode: DWORD

; offset

.data
bVal  BYTE ?
wVal  WORD ?
dVal  DWORD ?
dVal2 DWORD ?

.code
mov esi, OFFSET bVal           ; ESI = 00404000h
mov esi, OFFSET wVal           ; ESI = 00404001h
mov esi, OFFSET dVal           ; ESI = 00404003h
mov esi, OFFSET dVal2          ; ESI = 00404007h

.data
myArray WORD 1, 2, 3, 4, 5

.code
mov esi, OFFSET myArray + 4    ; ESI points to the third integer in the array

; the following statement loads pointer's value into ESI
.data
bigArray DWORD 500 DUP(?)
pArray   DWORD bigArray

.code
mov esi, pArray

; ALIGN
; directive aligns a variable on type boundary
bVal  BYTE ?                    ; 00404000h
ALIGN 2
wVal  WORD ?                    ; 00404002h
bVal2 BYTE ?                    ; 00404004h

; dVal  DWORD ?                   ; 00404005
ALIGN 4
dVal  DWORD ?                   ; after ALIGN 4: 00404008h
dVal2 DWORD ?                   ; 0040400Ch

; ptr 
.data
myDouble DWORD 12345678h

.code 
mov ax, myDouble                ; error
mov ax, WORD PTR myDouble       ; It is possible to move low-order word to AX
; little endian storage format:
; 78h | 56h | 34h | 12h