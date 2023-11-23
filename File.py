from pathlib import Path

loc = "bscore.txt"

class file:
    
    @staticmethod
    def saveBestScore(score: int):
        # if they want to cheat then let them cheat cuz they are not having fun
        with open(loc, "w") as f:
            f.write(str(score))
    
    @staticmethod
    def readBestScore() -> int:
        if not Path(loc).exists(): return 0
        with open(loc, "r") as f:
            return int(f.read())