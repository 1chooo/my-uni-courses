include Irvine32.inc
.data
myID BYTE "109601003"
myID2 BYTE "109601005"
size_ID = 9
result byte 9 DUP(?)

.code
main PROC
	mov esi, OFFSET myID

	L1:
		mov al, myID[esi]
		mov el, myID2[esi]
		cmp al, el
		jmp L2
		cmp el, al
		jmp L3
		mov dl, 'A'
		mov [esi], dl 

	L2:
		mov bl, 'B'
		mov [esi], bl
		jmp L1

	L3:
		mov cl, 'C'
		mov [esi], cl
		jmp L1

	L4:
		inc esi
		loop L1
		exit
main ENDP
END main