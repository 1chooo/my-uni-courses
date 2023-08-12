INCLUDE Irvine32.inc

main EQU start@0
Str_remove PROTO, pStart:PTR BYTE, nChars:DWORD

.data
target1 BYTE "109601003",0                ; fill the studend ID of team member 1
target2 BYTE "109601005",0                ; fill the studend ID of team member 2
target3 BYTE "999999999",0

.code
main PROC

    INVOKE Str_remove, OFFSET target1, 5       ; Remove 5 char
    mov edx,OFFSET target1
    call WriteString
    call Crlf

    INVOKE Str_remove, OFFSET target2, 2       ; remove 2 char
    mov edx,OFFSET target2
    call WriteString
    call Crlf

    INVOKE Str_remove, OFFSET [target2+1], 15  ; remove the length over the target
    mov edx,OFFSET target2
    call WriteString
    call Crlf

    call WaitMsg
    exit

main ENDP

Str_remove PROC,
    pStart:PTR BYTE,                           ; points to first character to delete
    nChars:DWORD                               ; number of characters to delete

    INVOKE Str_length, pStart                  ; get the string length
    mov ecx, eax                               ; the length save in ecx, it will be used by loop

    .IF nChars <= ecx                          ; check whether nChars exceeds the string size
        sub ecx,nChars                         ; if no exceed, then ecx minus nChars    
    .ENDIF

    mov esi, pStart                            ; Set the begining of the copy source
    add esi, nChars                            ; Move the starting to the correct location
    mov edi, pStart                            ; Set the destination position

    cld                                        ; clear direction flag (forward)
    rep movsb                                  ; do the move, repeat it
    mov BYTE PTR [edi],0                       ; insert new null byte

Exit_proc:
    ret

Str_remove ENDP

END main