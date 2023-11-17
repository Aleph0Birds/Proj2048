import UI.window as win
import tkinter as tk

SBWidth = 15
SBHeight = 2

class indicator:
    def __init__(self, window: win.window) -> None:
        title = tk.Label(window.win, foreground=win.GrayColor, background=win.BackgroundColor, 
                         text="2048", font=(20))
        title.grid(row = 0, column = 0, columnspan=2)
        curScore = tk.Label(window.win, background= win.GrayColor, foreground="white",
                            text="Score\n0", width=SBWidth, anchor="center", pady=10, height=SBHeight)
        curScore.grid(row = 0, column=2)
        bestScore = tk.Label(window.win, background= win.GrayColor, foreground="white",
                             text="Best\n0", width=SBWidth, anchor="center", pady=10, height=SBHeight)
        bestScore.grid(row = 0, column=3)
        uselessLabel = tk.Label(window.win, background=win.BackgroundColor, foreground=win.GrayColor, text="Join the number and blah blah")
        uselessLabel.grid(row=1)
        
        self.curScoreWidget = curScore
        self.bestScoreWidget = bestScore
        
        self.curScore = 0
        self.bestScore = 0
        
       