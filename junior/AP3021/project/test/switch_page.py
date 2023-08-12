import tkinter as tk

class BaseDesk() :

    def __init__(self, master) :

        self.root = master
        self.root.config()
        self.root.title("Base Page")
        self.root.geometry("200x200")

        initface(self.root)

class initface() :

    def __init__(self, master) :
        
        self.master = master
        self.master.config(bg="green")

        self.initface = tk.Frame(self.master,)
        self.initface.pack()
        btn = tk.Button(self.initface, text="change", command=self.change)
        btn.pack()

    def change(self, ) :

        self.initface.destroy()
        face1(self.master)

class face1() :

    def __init__(self, master) :

        self.master = master
        self.master.config(bg="blue")
        self.face1 = tk.Frame(self.master,)
        self.face1.pack()
        btn_back = tk.Button(self.face1, text="face1 back", command=self.back)
        btn_back.pack()

    def back(self) :

        self.face1.destroy()
        initface(self.master)

if __name__ == "__main__" :

    root = tk.Tk()
    BaseDesk(root)
    root.mainloop()