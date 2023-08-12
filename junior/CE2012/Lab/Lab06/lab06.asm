include Irvine32.inc

.data
result byte 81 DUP(?)

.code
lab06 PROC

    mov edi, offset result + 80
    Mov ecx, 9h
L1:
    Push cx
    mov bl, cl
    Mov cx, 9h
L2:
    mov al, bl
    mul cl
    mov [edi], al

    dec edi

    Loop L2

    Pop cx

    Loop L1
    ret
lab06 ENDP
END lab06