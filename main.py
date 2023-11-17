from Struct.Matrix import Matrix

def main():
    useUI()
    initializeBoard()
    win.mainloop()

# range: 2^1 - 2^11+ -> 2 - 2048+
def update() -> None:
    """called each tick by the window, by default 30 ticks per second"""
    if win.isKeyDown("Escape"):
        win.exit()
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
    ### Task 1 ###
    global board 
    board = Matrix(4, 4)
    ### Task 2 ###
    from random import choice
    from helper.utility import chance
    n = 0
    while n < 2:
        r, c = choice(range(4)), choice(range(4))
        if board[r][c] != 0:
            continue
        
        board[r][c] = bool(chance(50)) + 1
        n += 1
        
    boardGrid.updateBoard(board)

if __name__ == "__main__":
    main()