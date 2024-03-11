; saving the results of our addition in a variable named sum.

include Irvine32.inc

.data
sum DWORD 0

.code
main PROC
    mov eax, 5
    add eax, 6
    mov sum, eax

    INVOKE ExitProcess, 0
main ENDP
END main