import pyxel
import random

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
        self.__framecount = 0
        self.__ttl_seconds = random.randint(2, 5)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def draw(self):
        self.__framecount += 1
        pyxel.blt(
            self.__x,
            self.__y,
            self.IMG_BANK,
            self.COIN_IMG_X * World.TILE_SIZE,
            self.COIN_IMG_Y * World.TILE_SIZE,
            self.WIDTH,
            self.HEIGHT,
        )

    def is_expired(self):
        return self.__framecount > self.__ttl_seconds * World.FPS
