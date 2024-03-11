# -*- coding: utf-8 -*-
"""
Date: 2023/11/06
Question: 02
Author: 林群賀
Student Number: 109601003
"""

account_a_saving = int(input("請輸入 A 帳戶餘額: "))
account_b_saving = int(input("請輸入 B 帳戶餘額: "))

transfer = int(input("請輸入欲從 A 帳戶轉入 B 帳戶之金額: "))


if transfer > account_a_saving:
    transfer = account_a_saving
print("------------------")
print("轉帳後，A 帳戶新餘額:", account_a_saving - transfer, "元")
print("轉帳後，B 帳戶新餘額:", account_b_saving + transfer, "元")