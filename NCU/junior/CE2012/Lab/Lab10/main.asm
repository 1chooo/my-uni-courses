INCLUDE Irvine32.inc

Str_copyN PROTO,
	source:PTR BYTE,	; source string address
	target:PTR BYTE,	; target string address
	maxChars:DWORD	; maximum number of characters to copy

main EQU start@0

.data
string_1 BYTE "109601003", 0	; Fill in first student’s id
string_2 BYTE "109601005", 0	; Fill in second student’s id

.code
main PROC
	INVOKE Str_copyN,			; copy string_1 to string_2
		OFFSET string_1,
		OFFSET string_2 + 9,
		(SIZEOF string_2) - 1	; save space for null byte

	; display the destination string:
	mov  edx, OFFSET string_2		
	call WriteString
	call Crlf
	call WaitMsg
	exit
main ENDP
 

Str_copyN PROC USES eax ecx esi edi,
	source:PTR BYTE,		; source string
	target:PTR BYTE,		; target string
	maxChars:DWORD		; max chars to copy

	; Copy a string from source to target, limiting the number of 
	; characters to copy by maxChars.
	; The value in maxChars does not include the null byte.

	mov ecx, maxChars		; set counter for REP
	mov esi, source		; assign source
	mov edi, target		; assign target
	cld			; clear direction flag (direction = forward)
	rep movsb		; copy the string

	mov BYTE PTR [edi], 0	; append null byte
	ret
Str_copyN ENDP

END main