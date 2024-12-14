import pyxel

from model.world import World

class Coin:
    IMG_BANK = 0
    WIDTH = 8
    HEIGHT = 8
    COIN_IMG_X = 1
    COIN_IMG_Y = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def draw(self):
        pyxel.blt(
            self.__x,
            self.__y,
            self.IMG_BANK,
            self.COIN_IMG_X * World.TILE_SIZE,
            self.COIN_IMG_Y * World.TILE_SIZE,
            self.WIDTH,
            self.HEIGHT,
        )
