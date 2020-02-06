import math as math
import matplotlib.pyplot as plt
import numpy as np

from multiprocessing import Pool

# Configuration

STAR_RADIUS = 5000
STAR_LIMB_DARKENING_COEFFICIENT = 0.80
STAR_LIMB_DARKENING_ALPHA = 0.85
PLANET_RADIUS = 500
KM_PER_PIXEL = 10
PLANET_INCLINATION = 0.2
SAMPLE_RATE = 0.05
NUMBER_OF_WORKERS = 12

# private variables

_star_pixel_radius = int(STAR_RADIUS / KM_PER_PIXEL)
_planet_pixel_radius = int(PLANET_RADIUS / KM_PER_PIXEL)
_grid_size = int(2 * _star_pixel_radius + 1)
_planet_y = _grid_size * PLANET_INCLINATION


def calc_star_brightness(d_star_center):
    tmp = (1 - ((d_star_center / _star_pixel_radius) ** 2)) ** 0.5
    limb = 1 - STAR_LIMB_DARKENING_COEFFICIENT * (1 - (tmp ** STAR_LIMB_DARKENING_ALPHA))
    return 255 * limb


def generate_snapshot_image(planet_x):
    grid = np.zeros((_grid_size, _grid_size))

    for x in range(_grid_size):
        for y in range(_grid_size):
            dx_star_center = _star_pixel_radius - x
            dy_star_center = _star_pixel_radius - y
            d_star_center = math.sqrt(dx_star_center ** 2 + dy_star_center ** 2)

            if d_star_center > _star_pixel_radius:
                continue

            dx_planet_center = abs(planet_x - x)
            dy_planet_center = abs(_planet_y - y)
            d_planet_center = math.sqrt(dx_planet_center ** 2 + dy_planet_center ** 2)

            if d_planet_center < _planet_pixel_radius:
                continue

            grid[x, y] = calc_star_brightness(d_star_center)

    return grid


def worker_function(x):
    snapshot = generate_snapshot_image(x)
    return snapshot.mean()


if __name__ == '__main__':
    with Pool(NUMBER_OF_WORKERS) as pool:
        transit = pool.map(worker_function, np.arange(0, _grid_size, _grid_size * SAMPLE_RATE, dtype=int))

    plt.plot(transit)
    plt.show()
