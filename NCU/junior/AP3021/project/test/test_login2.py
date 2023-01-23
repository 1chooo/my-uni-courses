import tkinter as tk

class LoginForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        # 建立文本框，用於輸入用戶名稱和密碼
        username_label = tk.Label(self, text="用戶名稱:")
        username_label.grid(row=0, column=0, sticky="E")
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1)

        password_label = tk.Label(self, text="密碼:")
        password_label.grid(row=1, column=0, sticky="E")
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1)

        # 建立按鈕，用於提交登錄資訊
        submit_button = tk.Button(self, text="提交", command=self.on_submit)
        submit_button.grid(row=2, column=1, sticky="E")

    def on_submit(self):
        # 取得用戶輸入的用戶名稱和密碼
        username = self.username_entry.get()
        password = self.password_entry.get()

        # 驗證用戶名稱和密碼是否正確
        if username == "admin" and password == "admin":
            # 如果用戶名稱
