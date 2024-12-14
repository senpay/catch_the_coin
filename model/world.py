class World:

    # it is in tiles, where
    # each tile is 8x8 pixels
    HEIGHT = 16
    WIDTH = 16
    TILE_SIZE = 8


def sprites_collide(x1, y1, x2, y2):

    # Check if one sprites is to the left of the other
    if x1 + TILE_SIZE <= x2 or x2 + TILE_SIZE <= x1:
        return False

    # Check if one sprites is above the other
    if y1 + TILE_SIZE <= y2 or y2 + TILE_SIZE <= y1:
        return False

    return True
