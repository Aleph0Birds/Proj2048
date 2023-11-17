

class Color:

    colors: list[str] = [
                         None, "#eee4da", "#ede0c8", "#f2b179",
                         "#f59563", "#f67c5f", "#f65e3b", "#edcf72",
                         "#edcc61", "#edc850", "#edc53f", "#3e3933"
                        ]
    @staticmethod
    def getColor(n: int) -> list[str]:
        if n is not int: raise TypeError(f"Hiya n should be an integer just like there is no platform 9¾")
        if n < 0: raise ValueError(f"Hiya you want {n} of the colors that's too small bruh.")
        return Color.colors[-1] if n >= len(Color.colors) else Color.colors[n]