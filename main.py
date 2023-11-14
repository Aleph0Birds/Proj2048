
def main():
    pass
# start doing here :skull:

def useUI():
    from UI.boardgrid import boardgrid 
    from UI.window import window
    
    win = window()
    win.init()
    board = boardgrid()
    board.initialize(win)

    win.mainloop()

if __name__ == "__main__":
    main()
