import math

import numpy as np

from star import generate_star

from config import PLANET_1_RADIUS
from config import PLANET_1_INCLINATION

from config import PLANET_2
from config import PLANET_2_RADIUS
from config import PLANET_2_INCLINATION
from config import PLANET_2_SPEED_FACTOR
from config import PLANET_2_OFFSET

from config import PLANET_3
from config import PLANET_3_RADIUS
from config import PLANET_3_INCLINATION
from config import PLANET_3_SPEED_FACTOR
from config import PLANET_3_OFFSET

from config import STAR_RADIUS
from config import MARGIN
from config import _GRID_SIZE

_STAR = generate_star()  # Cached star image.
_PLANET_1_Y = int(STAR_RADIUS + MARGIN + PLANET_1_INCLINATION)  # Y coordinate of planet 1.
_PLANET_2_Y = int(STAR_RADIUS + MARGIN + PLANET_2_INCLINATION)  # Y coordinate of planet 2.
_PLANET_3_Y = int(STAR_RADIUS + MARGIN + PLANET_3_INCLINATION)  # Y coordinate of planet 3.


#
# This function takes an image grid representing a star and cuts out a planet.
#
# grid: The image grid representing a star.
# planet_x: The x coordinate of the planet center.
# planet_y: The y coordinate of the planet center.
# planet_radius: The pixel radius of the planet.
#
def cut_out_planet(grid, planet_x, planet_y, planet_radius):
    for x in range(max(0, abs(planet_x - planet_radius)), min(_GRID_SIZE, planet_x + planet_radius)):
        for y in range(max(0, abs(planet_y - planet_radius)), min(_GRID_SIZE, planet_y + planet_radius)):
            dx_planet_center = abs(planet_x - x)
            dy_planet_center = abs(planet_y - y)
            d_planet_center = math.sqrt(dx_planet_center ** 2 + dy_planet_center ** 2)

            if d_planet_center < planet_radius:
                grid[x, y, 0] = 0
                grid[x, y, 1] = 0
                grid[x, y, 2] = 0


#
# This function makes a copy of the cached star image and cuts out the 3 planets. Afterwards it flips
# and transposes the image such that it is rendered correctly.
#
# x: The x coordinate of the center of planet 1.
#
def cut_out_planets(x):
    grid = _STAR.copy()

    cut_out_planet(grid, x, _PLANET_1_Y, PLANET_1_RADIUS)
    if PLANET_2:
        cut_out_planet(grid, int(x * PLANET_2_SPEED_FACTOR + PLANET_2_OFFSET), _PLANET_2_Y, PLANET_2_RADIUS)
    if PLANET_3:
        cut_out_planet(grid, int(x * PLANET_3_SPEED_FACTOR + PLANET_3_OFFSET), _PLANET_3_Y, PLANET_3_RADIUS)

    return np.flip(np.swapaxes(grid, 0, 1), 0)
