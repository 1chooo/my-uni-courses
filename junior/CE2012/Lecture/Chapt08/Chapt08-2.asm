push ebx                    ; save register values
push ecx
push esi
mov esi, OFFSET array       ; starting OFFSET
mov ecx, LENGTHOF array     ; size, in units
mov ebx, TYPE array         ; doubleword format
call DumpMem                ; display mamory
pop esi                     ; restore register values
pop ecx
pop ebx


push ebx                    ; save register values
push ecx
push esi
mov esi, OFFSET array       ; starting OFFSET
mov ecx, LENGTHOF array     ; size, in units
mov ebx, TYPE array         ; doubleword format
call DumpMem                ; display mamory
cmp eax, 1                  ; error flag set?
je error_exit               ; exit with flag set

pop esi                     ; restore register values
pop ecx
pop ebx

ret

error_exit:
mov edx, OFFSET error_msg

ret


; if DumpMem use stack parameters
push TYPE array
push LENGTHOF array
push OFFSET array
call DumpMem


; Passing by value
.data
val1 DWORD 5
val2 DWORD 6

.code
push val2
push val1
call AddTwo     ; in C++ int sum = AddTwo(val1, val2);


AddTwo PROC
    push ebx
    mov ebp, esp            ; base of stack frame
    mov eax, [ebp + 12]     ; second parameter
    add eax, [ebp + 8]      ; first parameter
    pop ebp

    ret
AddTwo ENDP

; Explicit Stack parameter

x_parameter = EQU[ebp + 12]
y_parameter = EQU[ebp + 8]

AddTwo PROC
    push ebx
    mov ebp, esp                ; base of stack frame
    mov eax, x_parameter        ; second parameter
    add eax, y_parameter        ; first parameter
    pop ebp

    ret
AddTwo ENDP


; Passing by reference
push OFFSET val2
push OFFSET val1
call Swap

; in C++ Swap(&val1, &val2);


; Passing arrays
.data
array DWORD 50 DUP(?)

.code
push OFFSET array
call ArrayFill




MySub PROC
    push ebp
    mov ebp, esp
    sub esp, 8                      ; create locals
    mov DWORD PTR [ebp - 4], 10     ; X
    mov DWORD PTR [ebp - 8], 20     ; Y
    mov esp, ebp                    ; remove locals from stack
    pop ebp

    ret
MySub ENDP


MySub PROC
    push ebp
    mov ebp, esp
    sub esp, 8                      ; create locals
    mov DWORD PTR [ebp - 4], 10     ; X
    mov DWORD PTR [ebp - 8], 20     ; Y
    pop ebp             

    ret                             ; return to invalid address!
MySub ENDP


X_local EQU DWORD PTR[ebp - 4]
Y_local EQU DWORD PTR[ebp - 8]

MySub PROC
    push ebp
    mov ebp, esp
    sub esp, 8                      ; create locals
    mov X_local 10     ; X
    mov Y_local, 20     ; Y
    mov esp, ebp                    ; remove locals from stack
    pop ebp

    ret
MySub ENDP


; ArrayFill

.data 
count = 100
array WORD count DUP(?)

.code 
push OFFSET array
push count
call ArrayFill


ArrayFill PROC
    push ebp
    mov ebp, esp
    pushad                      ; save registers
    mov esi, [ebp + 12]         ; offset of array
    mov ecx, [ebp + 8]          ; array length
    cmp ecx, 0                  ; ECX == 0?
    je L2                       ; yes: skip over loop

L1:
    mov eax, 10000h             ; get random 0 - FFFFh
    call RandomRange            ; from the link library
    mov [esi], ax               ; insert value in array
    add esi, TYPE WORD          ; move to next element
    loop L1

L2: popad                       ; restore registers
    pop ebp

    ret 8                       ; clean up the stack
ArrayFill ENDP


; void makeArray() {
;   char myString[30];
;   for (int i = 0; i < 30; i++) 
;	    myString[i] = '*';
; }


makeArray PROC

	push ebp
	mov ebp, esp
	sub esp, 32						; myString is at EBP - 30
	lea esi, [ebp - 30]				; load address of myString
	mov ecx, 30						; loop counter

L1: 

    mov BYTE PTR [esi], '*'         ; fill one position
    inc esi                         ; move to next
    loop L1                         ; continue until ECX = 0
    add esp, 32                     ; remove the array (return ESP)
    pop ebp

    ret
makeArray ENDP