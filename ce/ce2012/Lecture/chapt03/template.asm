; Program template (tenplate.asm)

.386
.model flat, stdcall
.stack 4096
ExitProcess PROTO, dwExitCode: DWORD

.data  
    ; declare variable here

.code
main PROC
    ; write your code here

    INVOKE ExitProcess, 0
mian ENDP
END main