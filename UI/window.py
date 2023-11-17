import tkinter as tk

WinWidth: int = 450
WinHeight: int = 600
GrayColor = "#323232"
BorderColor = "#b8aea1"
BoardColor = "#cac1b5"
BackgroundColor = "#faf8f1"

class window:
    def __init__(self, tickRate: int = 30) -> None:
        win = tk.Tk()

        win.geometry(f"{WinWidth}x{WinHeight}")
        win.title("Proj2048")
        win.resizable(False, False)
        win.config(bg=BackgroundColor)
        win.grid_columnconfigure(2, weight=1)
        win.grid_columnconfigure(3, weight=1)
        # win.grid_rowconfigure(0)
        self.tickRate = tickRate
        self.deltaTimeSeconds = 1 / tickRate
        self.updating = False
        self.updateFx: list[function] = []

        win.protocol("WM_DELETE_WINDOW", self.exit)

        self.keysPressed: list[str] = []
        self.keysReleased: list[str] = []
        win.bind("<KeyPress>", lambda event: self.keysPressed.append(event.keysym))
        win.bind("<KeyRelease>", lambda event: self.keysReleased.append(event.keysym))
        self.win = win
    
    def subscribeUpdate(self, function) -> None:
        """Subscribe a function to be updated

        Parameters
        ----------
        function : function
        """
        self.updateFx.append(function)

    def initialize(self, *func) -> None:
        """calls functions after window initialized

        Parameters
        ----------
        *func : function
            arguments of function
        """
        for fx in func:
            fx()

    def mainloop(self) -> None:
        """Main loop of the window, should be called after initialized, suppresses code execution outside update functions."""

        self.updating = True
        if len(self.updateFx) <= 0:
            self.win.mainloop()
        else:
            import time
            while True:
                if not self.updating: break
                self.win.update()

                for fx in self.updateFx:
                    fx()

                self.__clearKeys__()
                time.sleep(self.deltaTimeSeconds)

    def getPressedKeys(self) -> list[str]:
        """Gets a list of symbols of key pressed

        Returns
        -------
        list[str]
            a list of keys pressed at the moment
        """
        return self.keysPressed
    
    def isKeyDown(self, key: str) -> bool:
        """Check if a key is down, case matters

        Parameters
        ----------
        key : str
            key to be checked, i.e. "a" != "A", "Enter"

        Returns
        -------
        bool
        """
        return bool(key) and (key in self.keysPressed)
    
    def isKeyUp(self, key: str) -> bool:
        """Check if a key is realeased, case matters

        Parameters
        ----------
        key : str
            key to be checked, i.e. "a" != "A", "Enter"

        Returns
        -------
        bool
        """
        return bool(key) and (key in self.keysReleased)
    
    def __clearKeys__(self) -> None: self.keysPressed.clear(); self.keysReleased.clear()

    def exit(self) -> None:
        """Exits the window update loop"""
        self.updating = False
        self.win.destroy()