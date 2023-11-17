import UI.window as win
import tkinter as tk
import tkinter.font as tkf

SBWidth = 12
SBHeight = 20
TitleColor = "#7a6e66"

class indicator:
    def __init__(self, window: win.window) -> None:
        titleFont = tkf.Font(window.win, family="Segoe UI Semibold", size=32, weight="bold")
        title = tk.Label(window.win, foreground=TitleColor, background=win.BackgroundColor, 
                         text="2048")
        title.configure(font=titleFont)
        title.grid(row = 0, column = 0, columnspan=2, pady=SBHeight, padx=SBWidth - 4)

        curScore = tk.Label(window.win, background= win.BorderColor, foreground=win.BackgroundColor,
                            text="Score\n0", width=SBWidth, anchor="n")
        curScore.grid(row = 0, column=2, sticky="ne", pady=24)

        bestScore = tk.Label(window.win, background= win.BorderColor, foreground=win.BackgroundColor,
                             text="Best\n0", width=SBWidth, anchor="n")
        bestScore.grid(row = 0, column=3, sticky="nw", padx=16, pady=24)

        uselessLabel = tk.Label(window.win,
                                background=win.BackgroundColor, foreground=TitleColor,
                                text="Join the numbers and get to the 2048 tile", pady=15, padx=20)
        uselessLabel.grid(row=1, column=0, columnspan=2, sticky="w")
        
        self.curScoreWidget = curScore
        self.bestScoreWidget = bestScore
        
        self.curScore = 0
        self.bestScore = 0
        
       