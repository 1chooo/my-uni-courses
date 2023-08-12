; Course: CE2012
; HW: 1
; This program is to merge the four digits into MyID.

include Irvine32.inc

.data
MyID DWORD ?
Digit0 BYTE 1
Digit1 BYTE 0
Digit2 BYTE 0
Digit3 BYTE 3

.code
main PROC
    ; |  1 |  0 |  0 |  3 |
    ; | bh | bl | ah | al |
    mov bh, Digit0
    mov bl, Digit1
    mov ah, Digit2
    mov al, Digit3

    ; make 0100 -> 00000100
    movzx ebx, bx
    ; make 00000100 -> 01000000
    shl ebx, 16

    ; make 0003 -> 00000003
    movzx eax, ax
    
    ; 01000000 + 00000003
    add ebx, eax
    mov MyID, ebx

    exit
main ENDP
END main