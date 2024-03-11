; Course: CE2012
; HW: 2
; convert blank to zero; '#' to one.
; call the convert procedure 8 times.
; print the results BitStrs to the screen.
; wating user click the "enter"

include Irvine32.inc

.data                       ; the last number of my student number is 3.
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

IterChStrs:          ; at first we have to iterate all the elements.
    shl ah, 1
    mov al, [esi]
    cmp al, '#'      ; if meet '#', then we keep going convert to one.

    jb ConvertZero   ; or we have to convert to zero.

ConvertOne:          ; convert to one.
    add ah, 1b
    jmp L0           ; next step.

ConvertZero:         ; convert to zero.
    add ah, 0b

L0:
    inc esi

    Loop IterChStrs  ; keep running.

    mov [edi], ah
    inc edi

    RET

change ENDP

main PROC
    mov ecx, 8       ; set how many times we have to run.

    mov esi, offset ChStrs
    mov edi, offset BitStrs

L1:
    CALL change
    Loop L1
    mov ecx, 8
    mov esi, offset BitStrs

L2:                  ; show out results on the secreen.
    mov eax, [esi]
    mov ebx, TYPE BYTE

    call writebinb
    call crlf
    inc esi

    Loop L2

    call WaitMsg

main ENDP
END main