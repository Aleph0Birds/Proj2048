from UI.window import window
import tkinter as tk

class boardgrid:
    def __init__(self) -> None:
        pass

    def initialize(self, window: window) -> None:
        content = tk.Frame(window.win, highlightthickness=6, highlightbackground="#b8aea1")
        content.place(relx=.5, rely=.5, anchor=tk.CENTER)

        for i in range(4):
            for j in range(4):
                frame = tk.Frame(content, 
                                 highlightthickness=6, 
                                 highlightbackground="#b8aea1",
                                 width=150, height=150, 
                                 background="#cac1b5"
                                )
                frame.grid(row=i, column=j)