import tkinter as tk

# 建立主窗口
root = tk.Tk()
root.title("切換畫面範例")

# 建立菜單
menu = tk.Menu(root)
root.config(menu=menu)

# 建立第一個畫面
frame1 = tk.Frame(root)
frame1.pack()

# 在第一個畫面中建立文本框
username_label = tk.Label(frame1, text="用戶名稱:")
username_label.grid(row=0, column=0, sticky="E")
username_entry = tk.Entry(frame1)
username_entry.grid(row=0, column=1)

# 建立第二個畫面
frame2 = tk.Frame(root)

# 在第二個畫面中建立文本框
password_label = tk.Label(frame2, text="密碼:")
password_label.grid(row=0, column=0, sticky="E")
password_entry = tk.Entry(frame2, show="*")
password_entry.grid(row=0, column=1)

# 定義切換到第一個畫面的函數
def switch_to_frame1():
    frame1.pack()
    frame2.pack_forget()

# 定義切換到第二個畫面的函數
def switch_to_frame2():
    frame1.pack_forget()
    frame2.pack()
    
# 建立切換畫面的菜單項目
switch_frame_menu = tk.Menu(menu)
menu.add_cascade(label="切換畫面", menu=switch_frame_menu)
switch_frame_menu.add_command(label="第一個畫面", command=switch_to_frame1)
switch_frame_menu.add_command(label="第二個畫面", command=switch_to_frame2)


root.mainloop()
