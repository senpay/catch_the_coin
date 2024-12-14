import math
import random

from model.world import World


def round_float_if_close(number, delta):
    lower = math.floor(number)
    upper = math.ceil(number)

    # Calculate the difference to the lower and upper integers
    diff_to_lower = abs(number - lower)
    diff_to_upper = abs(number - upper)

    # Determine the closest integer and its difference
    if diff_to_lower <= delta:
        result = lower
    elif diff_to_upper <= delta:
        result = upper
    else:
        result = number

    return int(result)


def generate_random_coordinate(world_size):
    return random.uniform(0, world_size)


def sprites_collide(x1, y1, x2, y2):

    # Check if one sprites is to the left of the other
    if x1 + World.TILE_SIZE <= x2 or x2 + World.TILE_SIZE <= x1:
        return False

    # Check if one sprites is above the other
    if y1 + World.TILE_SIZE <= y2 or y2 + World.TILE_SIZE <= y1:
        return False

    return True
