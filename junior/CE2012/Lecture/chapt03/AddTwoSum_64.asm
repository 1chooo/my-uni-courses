; AddTwoSum_64.asm

ExitProcess PROTO

.data
sum DWORD 0

.code 
main PROC
    mov eax, 5
    add eax, 6
    mov sum, eax
    
    mov ecx, 0

    call ExitProcess
main ENDP
END main

; use 64-bit registers and variables
.code 
main PROC
    mov rax, 5
    add rax, 6
    mov sum, rax
    
    mov ecx, 0

    call ExitProcess
main ENDP
END main