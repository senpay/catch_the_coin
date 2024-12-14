import pyxel


class Coin:
    IMG = 0
    WIDTH = 8
    HEIGHT = 8
    COIN_IMG_X = 3
    COIN_IMG_Y = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def draw(self):
        pyxel.blt(
            self.__x,
            self.__y,
            self.IMG,
            self.COIN_IMG_X,
            self.COIN_IMG_Y,
            self.WIDTH,
            self.HEIGHT,
            pyxel.COLOR_BLACK,
        )
