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