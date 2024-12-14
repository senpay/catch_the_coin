import pyxel

from model.player import Player
from model.world import World


class App:
    def __init__(self):
        pyxel.init( World.WIDTH * World.TILE_SIZE, World.HEIGHT * World.TILE_SIZE, title="Catch the coin")
        pyxel.load("mygame.pyxres")

        self.__player = Player(x=0, y=0)

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



App()
