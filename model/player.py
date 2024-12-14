from model.game_element import GameElement
from model.utils import round_float_if_close


class Player(GameElement):
    DX = 0.5
    ROUNDING_ERROR_DELTA = 0.1
    IMG_X = 3
    IMG_Y = 0

    def stop_moving(self):
        self._x = round_float_if_close(self._x, self.ROUNDING_ERROR_DELTA)
        self._y = round_float_if_close(self._y, self.ROUNDING_ERROR_DELTA)

    # dx should be 1 or -1 (for right or left)
    def move_horizontally(self, dx):
        new_x = self._x + dx * self.DX
        self._x = new_x

    def move_left(self):
        self.move_horizontally(-1)

    def move_right(self):
        self.move_horizontally(1)

    # dy should be 1 or -1 (for down or up)
    def move_vertically(self, dy):
        new_y = self._y + dy * self.DX

        self._y = new_y

    def move_up(self):
        self.move_vertically(-1)

    def move_down(self):
        self.move_vertically(1)
