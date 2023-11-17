
def main():

    useUI()


def update() -> None:
    """called each tick by the window, by default 30 ticks per second"""
    if win.isKeyDown("Escape"):
        win.exit()
    # start working here

def useUI():
    from UI.boardgrid import boardgrid 
    from UI.window import window
    from UI.indicator import indicator
    
    global win
    global board
    global indicate
    win = window()
    board = boardgrid(win)
    indicate = indicator(win)
    win.subscribeUpdate(update)
    win.mainloop()

if __name__ == "__main__":
    main()
