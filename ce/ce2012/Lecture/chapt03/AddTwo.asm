; AddTwo.asm - adds two 32-bit integers
; Chapter 3 example

.386
.model flat, stdcall	; select the program's mrmory model and identify the calling convention.
.stack 4096				; sets aside 4096 bytes of storage for the runtimes stack
ExitProcess PROTO, dwExitCod:DWORD

.code 
main PROC
    mov eax, 5	; move 5 to the eax register
	add eax, 6	; add 6 to the eax register

	INVOKE ExitProcess, 0
main ENDP
END main
