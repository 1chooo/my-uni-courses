; AddTwo program

include Irvine32.inc

.code
main PROC
    mov eax, 5
    add eax, 6

    INVOKE ExitProcess, 0
main ENDP
END main