def main():
    useUI()
    initializeBoard()
    win.mainloop()

# range: 2^1 - 2^11+ -> 2 - 2048+
def update() -> None:
    """called each tick by the window, by default 30 ticks per second"""
    if win.isKeyDown("Escape"):
        win.exit()

    for dir in ["Up", "Down", "Right", "Left"]:
        ### Task 3 ###
        # wait for user to release the keys
        if win.isKeyUp(dir):
            board.gravity(dir)
            break
    # start working here

### Task 10 ###
def useUI():
    from UI.boardgrid import boardgrid 
    from UI.window import window
    from UI.indicator import indicator
    
    global win
    global boardGrid
    global indicate
    win = window()
    boardGrid = boardgrid(win)
    indicate = indicator(win)
    win.subscribeUpdate(update)

def initializeBoard():
    ### Task 1 + Task 2 ###
    from board import Board
    global board 
    board = Board(boardGrid)

if __name__ == "__main__":
    main()