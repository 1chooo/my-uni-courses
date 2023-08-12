include Irvine32.inc
.data

.code
main PROC
	mov al, 00000011b
	mov ah, 05d
	mov ax, 3ebh
	mov dx, 0eeeah
	sub dx, ax
main ENDP
END main
