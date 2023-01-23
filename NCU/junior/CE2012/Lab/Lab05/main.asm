include Irvine32.inc

.data
myID  BYTE "109601003"
myID2 BYTE "109601005"
size_ID BYTE 9
result BYTE 9 DUP(?)

.code 
Main PROC
    movzx ecx, size_ID
    mov dl, 0

L:
    push esi
    mov esi, OFFSET myID
    pop esi
    mov al, [esi]
    mov bl, [esi] + 9
    cmp al, bl

    mov esi, OFFSET result
    JB L1
    JA L2

    mov [esi], 41h  ; "A"
    JMP L3

L1:
    mov [esi], 43h  ; "C"
    JMP L3

L2:
    mov [eso], 42h  ; "B"
    JNA L3

L3:
    inc esi
    loop L

    exit

Main ENDP
END Main