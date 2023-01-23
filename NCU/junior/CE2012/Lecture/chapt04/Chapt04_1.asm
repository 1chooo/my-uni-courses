.386
.model flat, stdcall
.stack 4096
ExitProcess PROTO, dwExitCode: DWORD

; mov
; no more than one memory operand permitted
; MOV destination, source
; SIZE matched
; CS, DS, EIP, IP and immediate value cannot be the destination

.data
count BYTE 100
wVal  WORD 2

.code 
    mov bl, count   ; 8-bits
    mov ax, wVal    ; 16-bits
    mov count, al   ;

    mov al, wVal    ; error
    mov ax, count   ; error
    mov eax, count  ; error

.data
bVal  BYTE 100
bVal2 BYTE ?
wVal  WORD 2
dVal  DWORD 5

.code
    mov ds, 45          ; immediate move to DS not permitted
    mov esi, wVal       ; size mismatch
    mov eip, dVal       ; EIP cannot be the destination
    mov 25, bVal        ; immediate value cannot be destionation
    mov bVal2, bVal     ; memory-to-memory move not permitted

.data
oneBYTE  BYTE  78h
oneWORD  WORD  1234h
oneDWORD DWORD 12345678h

.code 
mov eax, 0
mov al, oneBYTE     ; EAX = 00000000h
mov ax, oneWORD     ; EAX = 00000078h
mov eax, oneDWORD   ; EAX = 12345678h
mov ax, 0           ; EAX = 12340000h


; Zero and sign extension of integers
; add zero or sign bit to smaller registers.

.data
count WORD 1

.code
mov ecx, 0
mov cx, count

.data
signedVal SWORD -16     ; FFF0h (-16)

.code
mov ecx, 0
mov cx, signedVal       ; ECX = 0000FFF0h
; if we fill ECX with FFFFFFFFh then copied signedVal to CX, then we truely get (-16) in ECX.
mov ecx, 0FFFFFFFFh
mov cx, signedVal       ; ECX = FFFFFFF0h (-16)

; MOVZX

.data
byteVal BYTE 10001111b

.code 
movzx ax, byteVal           ; AX = 0000000010001111b

mov bx, 0A69Bh
movzx eax, bx               ; EAX = 0000A69Bh
movzx edx, bl               ; EDX = 0000009Bh
movzx cx, bl                ; CX = 009Bh


.data
byte1 BYTE 9Bh
word1 WORD 0A69Bh

.code 
movzx eax, word1            ; EAX = 0000A69Bh
movzx edx, byte1            ; EDX = 0000009Bh
movzx cx, byte1             ; CX = 009Bh

; MOVSX

.data
byteVal BYTE 10001111b

.code 
movsx ax, byteVal           ; AX = 1111111110001111b

mov   bx , 0A69Bh
movsx eax, bx               ; EAX = FFFFA69Bh
movsx edx, bl               ; EDX = FFFFFF9Bh
movsx cx , bl               ; CX = FF9Bh

; LAHF and SAHF
; LAHF: load status flags into AH.
; SAHF: store AH into status flags.

.data
saveflags BYTE ?

.code 
lahf                        ; load flags into AH
mov saveflags, ah           ; save flags in AHin a variable

mov ah, saveflags           ; load saved flags into AH
sahf                        ; copy into Flags register from AH

; XCHG exchanges the value of two operands.
; At least one operand must be a register.
; No immediate operands are permitted.

.data
var1 WORD 1000h
var2 WORD 2000h

.code
xchg ax, bx     ; exchange 16-bits registers
xchg ah, al     ; exchange  8-bits registers
xchg var1, bx   ; exchange memory, registers
xchg eax, ebx   ; exchange 32-bits registers

xchg var1, var2 ; error: two memory operands


; Direct-Offset

; 8-bits
.data
arrayB BYTE 10h, 20h, 30h, 40h, 50h

.code
mov al, arrayB                          ; AL = 10h
mov al, [arrayB + 1]                    ; AL = 20h
mov al, [arrayB + 2]                    ; AL = 30h

; 16-bits
.data
arrayW WORD 100h, 200h, 300h

.code 
mov ax, arrayW                          ; AX = 100h
mov ax, [arrayW + 2]                    ; AX = 200h

; 32-bits
.data
arrayD DWORD 10000h, 20000h

.code
mov eax, arrayD                         ; EAX = 10000h
mov eax, [arrayD + 4]                   ; EAX = 20000h