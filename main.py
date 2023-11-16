
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
    
    global win
    global board
    win = window()
    win.init()
    board = boardgrid()
    board.initialize(win)
    win.subscribeUpdate(update)
    win.mainloop()

if __name__ == "__main__":
    main()
