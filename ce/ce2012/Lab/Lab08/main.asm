INCLUDE Irvine32.inc

main EQU start@0

.stack 4096
ExitProcess proto, dwExitCode: dword
FindLargest proto aPtr: PTR SDWORD, arraySize: DWORD     ; Declare the prototype of FindLargest procedure

.data
Ex1Array sdword 105522063 , 109601003 , 109601005       ; Initialize with 105522063, student ID1 , student ID2
Ex2Array sdword -105522063 , -109601003 , -109601005    ; Initialize with-105522063, negative ID1 ,negative ID2

.code
main PROC
    INVOKE FindLargest, ADDR Ex1Array, LENGTHOF Ex1Array
    INVOKE FindLargest, ADDR Ex2Array, LENGTHOF Ex2Array
    ; call FindLargest procedure
    call WaitMsg
    INVOKE ExitProcess, 0
main ENDP

FindLargest PROC,
    ptrArray: PTR SDWORD, sizeArray:DWORD
    push esi
    push ecx
    mov eax, 80000000h          ; smallest possible 32bit signed integer
    mov esi, ptrArray           ; point to the first element
    mov ecx, sizeArray            ; set iteration times
    
L1:    
    cmp eax, [esi]              ; compare the current value and current maximum
    jg L2                       ; if smaller than max, jump to L2
    mov eax, [esi]              ; update max value

L2:    
    add esi, 4                  ; make esi point to next SDWORD number
    loop L1                     ; loop L1
    call WriteInt               ; print out the number
    call Crlf
    pop ecx
    pop esi

    ret                         ; Return from subroutine
FindLargest ENDP
END main
