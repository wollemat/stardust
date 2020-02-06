import math as math
import matplotlib.pyplot as plt
import numpy as numpy

# Configuration

STAR_RADIUS = 5000
STAR_LIMB_DARKENING_COEFFICIENT = 0.80
STAR_LIMB_DARKENING_ALPHA = 0.85

PLANET_RADIUS = 500

KM_PER_PIXEL = 10

# private variables

_star_pixel_radius = int(STAR_RADIUS / KM_PER_PIXEL)
_planet_pixel_radius = int(PLANET_RADIUS / KM_PER_PIXEL)
_grid_size = int(2 * _star_pixel_radius + 1)


def generate_star():
    grid = numpy.zeros((_grid_size, _grid_size))
    for x in range(_grid_size):
        for y in range(_grid_size):
            dx_star_center = _star_pixel_radius - x
            dy_star_center = _star_pixel_radius - y
            pixel_distance_star_center = math.sqrt(dx_star_center ** 2 + dy_star_center ** 2)

            if pixel_distance_star_center <= _star_pixel_radius:
                tmp = (1 - ((pixel_distance_star_center / _star_pixel_radius) ** 2)) ** 0.5
                limb = 1 - STAR_LIMB_DARKENING_COEFFICIENT * (1 - (tmp ** STAR_LIMB_DARKENING_ALPHA))
                grid[x, y] = 255 * limb
    return grid


def cut_out_planet(original_star, planet_x, planet_y):
    grid_copy = numpy.copy(original_star)

    for x in range(max(0, planet_x - _planet_pixel_radius), min(planet_x + _planet_pixel_radius, _grid_size)):
        for y in range(max(0, planet_y - _planet_pixel_radius), min(planet_y + _planet_pixel_radius, _grid_size)):
            dx = abs(planet_x - x)
            dy = abs(planet_y - y)
            dp = math.sqrt(dx ** 2 + dy ** 2)

            if dp < _planet_pixel_radius:
                grid_copy[x, y] = 0

    return grid_copy


if __name__ == '__main__':
    star = cut_out_planet(generate_star(), 300, 700)
    plt.imshow(star.T, origin='lower')
    plt.show()
