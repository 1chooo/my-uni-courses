include Irvine32.inc
.data
Value1 SBYTE 03h
Value2 SBYTE 02h
Value3 SBYTE 8fh
Result SDWORD ?
.code
main PROC
	; Rval = -(val3 - 14 * (Val1 + Val2))
	mov al, Value1
	mov bl, Value2
	mov cl, Value3

	add al, bl
	mov bl, al

	shl al, 4
	shl bl, 1
	sub al, bl

	neg al
	add al, cl
	neg al
	movzx eax, al
	mov Result, eax
	
	exit
main ENDP
END main
