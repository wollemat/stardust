import math

import numpy as np

from star import generate_star

from config import PLANET_RADIUS
from config import _PLANET_Y
from config import _GRID_SIZE

_STAR = generate_star()


def cut_out_planet(planet_x):
    grid = _STAR.copy()
    for x in range(max(0, abs(planet_x - PLANET_RADIUS)), min(_GRID_SIZE, planet_x + PLANET_RADIUS)):
        for y in range(max(0, abs(_PLANET_Y - PLANET_RADIUS)), min(_GRID_SIZE, _PLANET_Y + PLANET_RADIUS)):
            dx_planet_center = abs(planet_x - x)
            dy_planet_center = abs(_PLANET_Y - y)
            d_planet_center = math.sqrt(dx_planet_center ** 2 + dy_planet_center ** 2)

            if d_planet_center < PLANET_RADIUS:
                grid[x, y, 0] = 0
                grid[x, y, 1] = 0
                grid[x, y, 2] = 0

    return np.flip(np.swapaxes(grid, 0, 1), 0)
