import tkinter as tk

class window:
    def __init__(self) -> None:
        pass

    def init(self) -> None:
        self.win = tk.Tk()

        self.win.geometry("606x606")
        self.win.resizable(False, False)
        self.win.config(bg="#323232")

    def mainloop(self) -> None:
        self.win.mainloop()