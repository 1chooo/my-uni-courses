; Data Transfer Examples
; AddSubTet.asm
; Show below implements various arithmetic expressions
; using the ADD, SUB, INC, DEC, NEG, and how status flags are affected.

.386
.model flat, stdcall
.stack 4096
ExitProcess PROTO, dwExitCode: DWORD

.data
Rval SDWORD ?
Xval SDWORD 26 
Yval SDWORD 30
Zval SDWORD 40

.code 
main PROC

    ; INC and DEC
    mov ax, 1000h
    inc ax                  ; AX = 1001h
    dec ax                  ; AX = 1000h

    ; Expression:
    ; Rval = -Xval + (Yval - Zval)
    mov eax, Xval
    neg eax                 ; EAX = -26
    mov ebx, Yval
    sub ebx, Zval           ; EBX = -10
    add eax, ebx
    mov Rval, eax           ; Rval = -36

    ; zero flag example:
    mov cx, 1
    sub cx, 1               ; ZF = 1
    mov ax, 0FFFFh          
    inc ax                  ; ZF = 1

    ; sign flag example:
    mov cx, 0
    sub cx, 1               ; SF = 1
    mov ax, 7FFFh
    add ax, 2               ; SF = 1

    ; carry flag example:
    mov al, 0FFh
    add al, 1               ; CF = 1, AL = 00

    ; Overflow flag example:
    mov al, +127
    add al, 1               ; OF = 1
    mov al, -128
    sub al, 1               ; OF = 1

    INVOKE ExitProcess, 0

main ENDP
END main