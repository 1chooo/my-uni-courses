; Lab: 7
; Group: 55

include Irvine32.inc

.data
dividend  WORD 1003d        ; Group leader's student id
divisor   WORD 100
quotient  WORD 1 DUP(?)
remainder WORD 1 DUP(?)

.code
divide MACRO dividend, divisor, quotient, remainder
    mov ax, dividend
    div byte ptr divisor
    mov byte ptr quotient, al       ; store quotient from al
    mov byte ptr remainder, ah      ; store remainder from ah
ENDM

Main PROC
    movsx eax, dividend
    call WriteDec
    call Crlf

    divide dividend, divisor, quotient, remainder       ; call devide MACRO

    movsx eax, quotient
    call WriteDec
    call Crlf

    movsx eax, remainder
    call WriteDec
    call Crlf

    call WaitMsg

    INVOKE ExitProcess, 0
    
Main ENDP
END Main