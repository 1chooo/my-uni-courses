# https://steam.oxxostudio.tw/category/python/tkinter/menu.html

import tkinter as tk

root = tk.Tk()
root.title('oxxo.studio')
root.geometry('200x200')

menu = tk.Menu(root)

menubar_1 = tk.Menu(menu)                        # 建立第一個選單的子選單，有三個選項
menubar_1.add_command(label="Open")              # 子選單第一個選項
menubar_1.add_command(label="Save")              # 子選單第二個選項
menubar_1.add_command(label="Exit")              # 子選單第三個選項
menu.add_cascade(label='File', menu=menubar_1)   # 建立第一個選單 File，綁定子選單

menubar_2 = tk.Menu(menu)                        # 建立第二個選單的子選單，有三個選項
menubar_2.add_command(label="AAA")               # 子選單第一個選項
menubar_2.add_command(label="BBB")               # 子選單第一個選項
menubar_2.add_command(label="CCC")               # 子選單第一個選項
menubar_2.add_separator()                        # 子選單分隔線

menubar_2_more = tk.Menu(menubar_2)              # 建立子選單內的子選單，有三個選項
menubar_2_more.add_command(label="X")            # 子選單的子選單的第一個選項
menubar_2_more.add_command(label="Y")            # 子選單的子選單的第二個選項
menubar_2_more.add_command(label="Z")            # 子選單的子選單的第三個選項
menubar_2.add_cascade(label='File', menu=menubar_2_more)
menu.add_cascade(label='Test', menu=menubar_2)   # 建立第二個選單 File，綁定子選單

root.config(menu=menu)                           # 綁定選單

root.mainloop()