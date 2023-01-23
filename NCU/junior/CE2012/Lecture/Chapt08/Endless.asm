; Endless Recursion
INCLUDE Irvine32.inc

.data
endlessStr BYTE "The recursion never stops", 0

.code
main PROC
    call Endless

    exit
main ENDP

Endless PROC
    mov edx, OFFSET endlessStr
    call WriteString
    call Endless

    ret                             ; never executes
Endless ENDP
END main