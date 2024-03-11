INCLUDE Irvine32.inc

.386
.model flat, stdcall
.stack 4096

ExitProcess proto, dwExitCode:dword                     ;delcare prototype
DifferentInputs proto, v1:dword, v2:dword, v3:dword     ;delcare prototype
main     EQU start@0

.data
.code

main proc

    invoke DifferentInputs, 2, 2, 3
    invoke DifferentInputs, 2, 3, 2
    invoke DifferentInputs, 3, 5, 5
    invoke DifferentInputs, 2, 2, 2
    invoke DifferentInputs, 104522064, 109601003, 109601005 ;fill your IDs

    call WaitMsg
    invoke ExitProcess, 0

main endp

DifferentInputs proc,
    v1:dword, v2:dword, v3:dword

    mov eax, v1       ; take out v1
    cmp v2, eax       ; compare v1 to v2    
    je Label_Equal    ; if (v1==v2) jump to Label_Equal, return 0

    cmp v3, eax       ; compare v1 to v3  
    je Label_Equal    ; if (v1==v3) jump to Label_Equal, return 0


    mov eax, v2       ; take out v2
    cmp v3, eax       ; compare v2 to v3
    je Label_Equal    ; if (v2==v3) jump to Label_Equal, return 0

Label_NotEqual:
    mov eax, 1        ; return 1
    jmp exit_label    ; return true

Label_Equal:
    mov  eax,0        ; return false

exit_label:
    call DumpRegs
    ret

DifferentInputs endp

end main
