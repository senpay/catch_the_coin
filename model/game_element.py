import pyxel

from model.world import World


class GameElement:
    IMG_BANK = 0
    WIDTH = 8
    HEIGHT = 8
    IMG_X = 1
    IMG_Y = 0

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def draw(self):
        pyxel.blt(
            self._x,
            self._y,
            self.IMG_BANK,
            self.IMG_X * World.TILE_SIZE,
            self.IMG_Y * World.TILE_SIZE,
            self.WIDTH,
            self.HEIGHT,
        )
