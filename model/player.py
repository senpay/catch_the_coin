import pyxel

from model.world import World
from model.utils import round_float_if_close


class Player:
    IMG_BANK = 0
    WIDTH = 8
    HEIGHT = 8
    DX = 0.5
    ROUNDING_ERROR_DELTA = 0.1
    PLAYER_IMG_X = 3
    PLAYER_IMG_Y = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def stop_moving(self):
        self.__x = round_float_if_close(self.__x, self.ROUNDING_ERROR_DELTA)
        self.__y = round_float_if_close(self.__y, self.ROUNDING_ERROR_DELTA)

    # dx should be 1 or -1 (for right or left)
    def move_horizontally(self, dx):
        new_x = self.__x + dx * self.DX
        self.__x = new_x

    def move_left(self):
        self.move_horizontally(-1)

    def move_right(self):
        self.move_horizontally(1)

    # dy should be 1 or -1 (for down or up)
    def move_vertically(self, dy):
        new_y = self.__y + dy * self.DX

        self.__y = new_y

    def move_up(self):
        self.move_vertically(-1)

    def move_down(self):
        self.move_vertically(1)

    def draw(self):
        pyxel.blt(
            self.__x,
            self.__y,
            self.IMG_BANK,
            self.PLAYER_IMG_X * World.TILE_SIZE,
            self.PLAYER_IMG_Y * World.TILE_SIZE,
            self.WIDTH,
            self.HEIGHT,
        )
