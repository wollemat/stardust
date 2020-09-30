import math
import numpy as np

from config import STAR_LIMB_DARKENING_COEFFICIENT
from config import STAR_LIMB_DARKENING_ALPHA

from config import STAR_CHANNEL_RED
from config import STAR_CHANNEL_GREEN
from config import STAR_CHANNEL_BLUE

from config import IMAGE_SIZE
from config import IMAGE_MARGIN

_STAR_RADIUS = int(IMAGE_SIZE / 2 - IMAGE_MARGIN)


#
# This function calculates the brightness of the star at a certain distance from the center. The effect
# of limb darkening has been allowed for. Credit for the formula goes to Theo Min.
#
# d_star_center: The pixel distance from the center of the star.
#
def calc_star_brightness(d_star_center):
    tmp = (1 - ((d_star_center / _STAR_RADIUS) ** 2)) ** 0.5
    return 1 - STAR_LIMB_DARKENING_COEFFICIENT * (1 - (tmp ** STAR_LIMB_DARKENING_ALPHA))


#
# This function generates an image of a star and returns the image grid.
#
# side_size: The size of the image. The image is square so the width and the height are equal.
#
def generate_star(side_size):
    grid = np.zeros((side_size, side_size, 3), dtype=np.uint8)

    for x in range(side_size):
        for y in range(side_size):
            dx_star_center = _STAR_RADIUS + IMAGE_MARGIN - x
            dy_star_center = _STAR_RADIUS + IMAGE_MARGIN - y
            d_star_center = math.sqrt(dx_star_center ** 2 + dy_star_center ** 2)

            if d_star_center < _STAR_RADIUS:
                brightness = calc_star_brightness(d_star_center)
                grid[x, y, 2] = STAR_CHANNEL_RED * brightness  # Set the red channel
                grid[x, y, 1] = STAR_CHANNEL_GREEN * brightness  # Set the green channel
                grid[x, y, 0] = STAR_CHANNEL_BLUE * brightness  # Set the blue channel

    return grid
