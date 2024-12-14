import pyxel
import random

from model.game_element import GameElement
from model.world import World


class Coin(GameElement):

    IMG_X = 1
    IMG_Y = 0

    def __init__(self, x, y):
        super().__init__(x, y)
        self.__framecount = 0
        self.__ttl_seconds = random.randint(2, 5)

    def draw(self):
        self.__framecount += 1
        super().draw()

    def is_expired(self):
        return self.__framecount > self.__ttl_seconds * World.FPS
