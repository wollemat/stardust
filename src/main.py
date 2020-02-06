
import math as math
import matplotlib.pyplot as plt
import numpy as numpy

# Configuration

STAR_PIXEL_RADIUS = 256
STAR_LIMB_DARKENING_COEFFICIENT = 0.80
STAR_LIMB_DARKENING_ALPHA = 0.85

# private variables

_grid_width = 2 * STAR_PIXEL_RADIUS + 1
_grid_height = _grid_width


def generate_star():
    grid = numpy.zeros((_grid_width, _grid_height))
    for x in range(_grid_width):
        for y in range(_grid_height):
            dx_star_center = STAR_PIXEL_RADIUS - x
            dy_star_center = STAR_PIXEL_RADIUS - y
            pixel_distance_star_center = math.sqrt(dx_star_center**2 + dy_star_center**2)

            if pixel_distance_star_center <= STAR_PIXEL_RADIUS:
                tmp = (1 - ((pixel_distance_star_center / STAR_PIXEL_RADIUS)**2))**0.5
                limb = 1 - STAR_LIMB_DARKENING_COEFFICIENT * (1 - (tmp**STAR_LIMB_DARKENING_ALPHA))
                grid[x, y] = 255 * limb
    return grid


if __name__ == '__main__':
    star = generate_star()
    plt.imshow(star)
    plt.show()
