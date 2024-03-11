INCLUDE Irvine32.inc

main EQU start@0

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


main PROC
    call Example1

    exit
main ENDP

Example1 PROC
    push 6
    push 5
    call AddTwo
    add esp, 8                  ; remove arguments from the stack
    ret                         ; stack is corrupted!
Example1 ENDP


; STDCALL
AddTwo PROC
    push ebx
    mov ebp, esp            ; base of stack frame
    mov eax, [ebp + 12]     ; second parameter
    add eax, [ebp + 8]      ; first parameter
    pop ebp

    ret 8                   ; clean up the stack
AddTwo ENDP