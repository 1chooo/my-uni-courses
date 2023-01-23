include Irvine32.inc


.data
ChStrs BYTE "########"
       BYTE "      ##"
       BYTE "      ##"
       BYTE "########"
       BYTE "########"
       BYTE "      ##"
       BYTE "      ##"
       BYTE "########"
BitStrs BYTE 8 dup(?)

.code
change PROC USES ecx
    
    mov ah, 0
    mov ecx, 8

ScanChstrs:
    shl ah, 1
    mov al, [esi]
    cmp al, '#'

    jb SetZero
SetOne:
    add ah, 1b
    jmp L
SetZero:
    add ah, 0b
L:
    inc esi
    
    Loop ScanChstrs

    mov [edi], ah
    inc edi

    RET
change ENDP

main PROC
    MOV ECX, 8

    mov esi, offset ChStrs
    mov edi, offset BitStrs

L1:
    CALL change

    LOOP L1

    MOV ECX, 8
    mov esi, offset BitStrs
L2:
    mov eax, [esi]
    mov ebx, TYPE byte
    call writebinb
    call crlf
    inc esi
    Loop L2

main ENDP
END main