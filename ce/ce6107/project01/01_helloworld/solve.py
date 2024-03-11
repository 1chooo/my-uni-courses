# -*- coding: utf-8 -*-
"""
Created Date: 2023/10/17
Project: 01
Author: 1chooo (Hugo ChunHo Lin)
Student Number: 109601003
"""

#!/usr/bin/env python3

from pwn import *
import sys
from typing import Union

binary = ELF("./helloworld")

context.binary = binary

# print(context)