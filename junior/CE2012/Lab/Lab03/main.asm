include Irvine32.inc

.data
Result BYTE 9 DUP(?)

.code
main PROC
	mov ecx, 9
	mov esi, OFFSET Result
	mov al, 09h

L: 
	mov [esi], al

L2:
	inc esi
	add al, 09h

	Loop L

main ENDP
END main