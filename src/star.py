import math
import numpy as np

from config import STAR_RADIUS
from config import STAR_LIMB_DARKENING_COEFFICIENT
from config import STAR_LIMB_DARKENING_ALPHA
from config import MARGIN
from config import _GRID_SIZE


#
# This function calculates the brightness of the star at a certain distance from the center. The effect
# of limb darkening has been allowed for.
#
# d_star_center: The pixel distance from the center of the star.
#
def calc_star_brightness(d_star_center):
    tmp = (1 - ((d_star_center / STAR_RADIUS) ** 2)) ** 0.5
    return 1 - STAR_LIMB_DARKENING_COEFFICIENT * (1 - (tmp ** STAR_LIMB_DARKENING_ALPHA))


#
# This function generates an image of a star and returns the image grid.
#
def generate_star():
    grid = np.zeros((_GRID_SIZE, _GRID_SIZE, 3), dtype=np.uint8)

    for x in range(_GRID_SIZE):
        for y in range(_GRID_SIZE):
            dx_star_center = STAR_RADIUS + MARGIN - x
            dy_star_center = STAR_RADIUS + MARGIN - y
            d_star_center = math.sqrt(dx_star_center ** 2 + dy_star_center ** 2)

            if d_star_center < STAR_RADIUS:
                brightness = calc_star_brightness(d_star_center)
                grid[x, y, 2] = 255 * brightness
                grid[x, y, 1] = 165 * brightness

    return grid
