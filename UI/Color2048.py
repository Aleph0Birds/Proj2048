

class Color:

    colors: list[str] = [
                         None, "#eee4da", "#ede0c8", # white
                         "#f2b179", "#f59563", "#f67c5f", "#f65e3b", # redish orange
                         "#edcf72", "#edcc61", "#edc850", "#edc53f", "#edc22e", # yellow
                         "#3e3933" # black
                        ]
    @staticmethod
    def getColor(n: int) -> str:
        """Gets the color according to the nth power of 2

        Parameters
        ----------
        n : int
            the nth power of 2

        Returns
        -------
        str
            the color in hexadecimal format 

        Raises
        ------
        TypeError
            if n is not integer
        ValueError
            if n is smaller than 0
        """
        if not isinstance(n, int): raise TypeError(f"Hiya n should be an integer not {type(n)} just like there is no platform 9¾")
        if n < 0: raise ValueError(f"Hiya you want {n} of the colors that's too small bruh.")
        return Color.colors[-1] if n >= len(Color.colors) else Color.colors[n]