import pyxel

from model.coin import Coin
from model.player import Player
from model.utils import generate_random_coordinate, sprites_collide
from model.world import World

WORLD_WIDTH_PIXELS = World.WIDTH * World.TILE_SIZE
WORLD_HEIGHT_PIXELS = World.HEIGHT * World.TILE_SIZE
GAME_LENGTH_SECONDS = 30


class App:
    def __init__(self):
        pyxel.init(
            width=WORLD_WIDTH_PIXELS,
            height=WORLD_HEIGHT_PIXELS,
            title="Catch the coin",
            fps=World.FPS,
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
        self.__score = 0
        self.__framecount = 0

        pyxel.run(update=self.update, draw=self.draw)

    def _has_catched_coin(self):
        return sprites_collide(
            self.__player.x, self.__player.y, self.__coin.x, self.__coin.y
        )

    def _time_run_out(self):
        return self.__framecount > GAME_LENGTH_SECONDS * World.FPS

    def update(self):
        if self._has_catched_coin():
            self.__coin = Coin(
                x=generate_random_coordinate(WORLD_WIDTH_PIXELS),
                y=generate_random_coordinate(WORLD_HEIGHT_PIXELS),
            )
            self.__score += 1
        elif self.__coin.is_expired():
            self.__coin = Coin(
                x=generate_random_coordinate(WORLD_WIDTH_PIXELS),
                y=generate_random_coordinate(WORLD_HEIGHT_PIXELS),
            )

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
        if self._time_run_out():
            pyxel.cls(0)
            pyxel.text(
                WORLD_WIDTH_PIXELS // 2 - 20,
                WORLD_HEIGHT_PIXELS // 2,
                "Game Over",
                pyxel.COLOR_WHITE,
            )
            pyxel.text(
                WORLD_WIDTH_PIXELS // 2 - 20,
                WORLD_HEIGHT_PIXELS // 2 + 10,
                f"Score: {self.__score}",
                pyxel.COLOR_WHITE,
            )
            return

        self.__framecount += 1
        pyxel.cls(0)
        self.__player.draw()
        self.__coin.draw()
        pyxel.text(5, 5, f"Score: {self.__score}", pyxel.COLOR_WHITE)
        pyxel.text(
            5,
            15,
            f"Time: {GAME_LENGTH_SECONDS - self.__framecount // World.FPS}",
            pyxel.COLOR_WHITE,
        )


App()
