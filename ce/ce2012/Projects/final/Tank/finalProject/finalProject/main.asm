include Irvine32.inc

EXTERN printBackGround@0:PROC


.data

.code

main PROC

	call printBackGround@0
	
	exit

main ENDP
END main