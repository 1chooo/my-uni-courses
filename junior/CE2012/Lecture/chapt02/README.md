# Chapter 02


### 8-bits, 16-bits, 32-bits
| 32-bits | 16-bits | 8-bits (high) | 8-bits (low) |
| :-----: | :-----: | :-----------: | :----------: |
|   EAX   |    AX   |       AH      |      AL      |
|   EBX   |    BX   |       BH      |      BL      |
|   ECX   |    CX   |       CH      |      CL      |
|   EDX   |    DX   |       DH      |      DL      |


### only 16-bits for their lower half
| 32-bits | 16-bits |
| :-----: | :-----: |
|   ESI   |    SI   |
|   EDI   |    DI   |
|   EBP   |    BP   |
|   ESP   |    SP   |


### Some Specialized Register

* General
  * EAX: accumulator
  * ECX: loop counter
  * ESP: stack pointer
  * ESI, EDI: index register
* Segment
  * CS: code segment
  * DS: data segment
  * SS: stack segment
  * ES,FS, GS: additional segments
* EIP: instruction pointer
* EFLAGS
  * status and control flags
    * Carry (bit 0): unsigned arithmetic out of range
    * Overflow (bit 11): signed arithmetic out of range
    * Sign (bit 7): result is negative
    * Zero (bit 6): result is zero
    * Auxiliary Carry (bit 4): carry from bit 3 to bit 4
    * Parity (bit 2): sum of 1 bits is an even number
  * each flag is a single binary bit