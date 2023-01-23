import tkinter as tk

# 建立主窗口
root = tk.Tk()
root.title("切換畫面")

# 建立主畫面
frame = tk.Frame(root)
frame.pack()

# 建立按鈕，用於打開新畫面
button = tk.Button(frame, text="打開新畫面", command=open_new_window)
button.pack()

# 定義打開新畫面的函數
def open_new_window():
    # 隱藏主畫面
    root.withdraw()

    # 建立新畫面
    new_window = tk.Toplevel(root)
    new_window.title("新畫面")

    # 建立按鈕，用於關閉新畫面
    button = tk.Button(new_window, text="關開新畫面", command=close_new_window)
    button.pack()

# 定義關開新畫面的函數
def close_new_window():
    # 銷毀新畫面
    new_window.destroy()

    # 顯示主畫面
    root.deiconify()

root.mainloop()
