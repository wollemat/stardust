import math
import numpy as np

from config import STAR_RADIUS
from config import STAR_LIMB_DARKENING_COEFFICIENT
from config import STAR_LIMB_DARKENING_ALPHA
from config import PLANET_RADIUS
from config import MARGIN
from config import _GRID_SIZE
from config import _PLANET_Y


def calc_star_brightness(d_star_center):
    tmp = (1 - ((d_star_center / STAR_RADIUS) ** 2)) ** 0.5
    return 1 - STAR_LIMB_DARKENING_COEFFICIENT * (1 - (tmp ** STAR_LIMB_DARKENING_ALPHA))


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


_star = generate_star()


def cut_out_planet(planet_x):
    grid = _star.copy()
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
