from asyncio import run

def main():
    useUI()
    initializeBoard()
    run(win.mainloop())

# range: 2^1 - 2^11+ -> 2 - 2048+
async def update() -> None:
    """called each tick by the window, by default 30 ticks per second"""
    if win.isKeyDown("Escape"):
        win.exit()

    for dir in ["Up", "Down", "Right", "Left"]:
        ### Task 3 ###
        # wait for user to release the keys
        if win.isKeyUp(dir):
            board.gravity(dir)
            ## waits for the animation to complete ##
            await boardGrid.waitAnimation()
            board.generateNewTile()
            boardGrid.updateBoard(board.mat)
            break


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