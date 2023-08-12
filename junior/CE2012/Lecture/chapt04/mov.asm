; no more than one memory operand permitted
; MOV destination, source
; SIZE matched
; CS, DS, EIP, IP and immediate value cannot be the destination

.386
.model flat, stdcall
.stack 4096
ExitProcess PROTO, dwExitCode: DWORD

.data
count BYTE 100
wVal  WORD 2

.code 
    mov bl, count   ; 8-bits
    mov ax, wVal    ; 16-bits
    mov count, al   ;

    mov al, wVal    ; error
    mov ax, count   ; error
    mov eax, count  ; error

.data
bVal  BYTE 100
bVal2 BYTE ?
wVal  WORD 2
dVal  DWORD 5

.code
    mov ds, 45          ; immediate move to DS not permitted
    mov esi, wVal       ; size mismatch
    mov eip, dVal       ; EIP cannot be the destination
    mov 25, bVal        ; immediate value cannot be destionation
    mov bVal2, bVal     ; memory-to-memory move not permitted