INCLUDE Irvine32.inc
main EQU start@0

.stack 4096
CountMatches proto, aPtr: PTR SDWORD, bPtr: PTR SDWORD, arraySize: DWORD

.data
array1 sdword 10, 5, 4, -6, 2, 11, 12
array2 sdword 10, 5, 3,  1, 4,  2,  5
 
.code
main proc
    invoke CountMatches, ADDR array1, ADDR array2, LENGTHOF array1
    call WaitMsg
    invoke ExitProcess, 0
main endp
 
CountMatches proc,
    aPtr: PTR SDWORD, bPtr: PTR SDWORD, arraySize: DWORD
    mov esi, aPtr     
    mov edi, bPtr     
    mov eax, 0         
    mov ecx, arraySize

L1: 
    mov ebx, [esi]     
    cmp ebx, [edi]
    jne L2          
    add eax, 1

L2:   
    add edi, 4
    add esi, 4
    loop L1
    
    call WriteDec
    call Crlf
    
		ret

CountMatches endp
end main
