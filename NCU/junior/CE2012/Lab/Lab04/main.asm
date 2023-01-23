Include Irvine32.inc

.data
myID BYTE '1', '0', '9', '6', '0', '1', '0', '0', '3'
myID2 BYTE  '1', '0', '9', '6', '0', '1', '0', '0', '5'
size_ID BYTE ?
size_ID2 BYTE ?

.code
Convert PROC USES eax ebx ecx edx esi   ; this no need comma
L1:
    mov al, [esi]
    add al, 17d
    mov [esi], al
    inc esi

    loop L1

    ret
Convert ENDP

Convert2 PROC
    push eax
    push ebx
    push ecx
    push edx
    push esi

L2:
    
    mov al, [esi]
    add al, 17d
    mov [esi], al
    inc esi

    loop L2

    pop esi
    pop edx
    pop ecx
    pop ebx
    pop eax

    ret
Convert2 ENDP

Main PROC
    mov eax, 9999h
    mov ebx, 9999h
    mov edx, 9999h
    
    mov size_ID, LENGTHOF myID
    movzx ecx, size_ID
    mov esi, OFFSET myID
    call Convert

    mov size_ID2, LENGTHOF myID2
    movzx ecx, size_ID2
    mov esi, OFFSET myID2
    call Convert2

    exit
Main ENDP
END Main