import math

import numpy as np

from star import generate_star

from config import PLANET_1_RADIUS
from config import PLANET_1_INCLINATION

from config import PLANET_2_RADIUS
from config import PLANET_2_INCLINATION
from config import PLANET_2_SPEED_FACTOR
from config import PLANET_2_OFFSET

from config import PLANET_3_RADIUS
from config import PLANET_3_INCLINATION
from config import PLANET_3_SPEED_FACTOR
from config import PLANET_3_OFFSET

from config import STAR_RADIUS
from config import MARGIN
from config import _GRID_SIZE

_STAR = generate_star()
_PLANET_1_Y = int(STAR_RADIUS + MARGIN + PLANET_1_INCLINATION)
_PLANET_2_Y = int(STAR_RADIUS + MARGIN + PLANET_2_INCLINATION)
_PLANET_3_Y = int(STAR_RADIUS + MARGIN + PLANET_3_INCLINATION)


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


def cut_out_planets(x):
    grid = _STAR.copy()

    cut_out_planet(grid, x, _PLANET_1_Y, PLANET_1_RADIUS)
    cut_out_planet(grid, int(x * PLANET_2_SPEED_FACTOR + PLANET_2_OFFSET), _PLANET_2_Y, PLANET_2_RADIUS)
    cut_out_planet(grid, int(x * PLANET_3_SPEED_FACTOR + PLANET_3_OFFSET), _PLANET_3_Y, PLANET_3_RADIUS)

    return np.flip(np.swapaxes(grid, 0, 1), 0)
