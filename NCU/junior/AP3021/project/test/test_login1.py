import tkinter as tk

# 建立主窗口
root = tk.Tk()
root.title("登錄系統")

# 建立文本框，用於輸入用戶名稱和密碼
username_label = tk.Label(root, text="用戶名稱:")
username_label.grid(row=0, column=0, sticky="E")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)

password_label = tk.Label(root, text="密碼:")
password_label.grid(row=1, column=0, sticky="E")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

# 建立按鈕，用於提交登錄資訊
submit_button = tk.Button(root, text="提交")
submit_button.grid(row=2, column=1, sticky="E")

root.mainloop()
