from asyncio import run
from File import file

def main():
    useUI()
    score = file.readBestScore()
    initializeBoard(score)
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
            indicate.updateScore(board.score)
            
            if board.isGameover():
                if board.score > board.bestScore:
                    board.bestScore = board.score

                indicate.setBestScore(board.bestScore)
                if win.askRestart():
                    board.restartBoard()    
                    boardGrid.updateBoard(board.mat)
                    indicate.updateScore(board.score)
                else: 
                    win.exit()
              
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

def initializeBoard(score: int):
    ### Task 1 + Task 2 ###
    from board import Board
    global board 
    board = Board(boardGrid)
    board.bestScore = score
    win.board = board
    indicate.setBestScore(score)

if __name__ == "__main__":
    main()