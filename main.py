import pyxel

from model.coin import Coin
from model.player import Player
from model.utils import generate_random_coordinate
from model.world import World

WORLD_WIDTH_PIXELS = World.WIDTH * World.TILE_SIZE
WORLD_HEIGHT_PIXELS = World.HEIGHT * World.TILE_SIZE


class App:
    def __init__(self):
        pyxel.init(
            WORLD_WIDTH_PIXELS,
            WORLD_HEIGHT_PIXELS,
            title="Catch the coin",
        )
        pyxel.load("mygame.pyxres")

        self.__player = Player(
            x=generate_random_coordinate(WORLD_WIDTH_PIXELS),
            y=generate_random_coordinate(WORLD_HEIGHT_PIXELS),
        )
        self.__coin = Coin(
            x=generate_random_coordinate(WORLD_WIDTH_PIXELS),
            y=generate_random_coordinate(WORLD_HEIGHT_PIXELS),
        )

        pyxel.run(update=self.update, draw=self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.__player.move_left()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.__player.move_right()
        elif pyxel.btn(pyxel.KEY_UP):
            self.__player.move_up()
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.__player.move_down()
        elif pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        else:
            self.__player.stop_moving()

    def draw(self):
        pyxel.cls(0)
        self.__player.draw()
        self.__coin.draw()


App()
