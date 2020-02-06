import math
import numpy as np

from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc

from multiprocessing import Process
from multiprocessing import Pipe

# Configuration

STAR_RADIUS = 462
STAR_LIMB_DARKENING_COEFFICIENT = 0.80
STAR_LIMB_DARKENING_ALPHA = 0.85

PLANET_RADIUS = 50
PLANET_INCLINATION = -250

MARGIN = 50
NUMBER_OF_WORKERS = 16

# Private variables

_grid_size = int(2 * (STAR_RADIUS + MARGIN))
_planet_y = int(STAR_RADIUS + MARGIN + PLANET_INCLINATION)


def calc_star_brightness(d_star_center):
    tmp = (1 - ((d_star_center / STAR_RADIUS) ** 2)) ** 0.5
    return 1 - STAR_LIMB_DARKENING_COEFFICIENT * (1 - (tmp ** STAR_LIMB_DARKENING_ALPHA))


def generate_star():
    grid = np.zeros((_grid_size, _grid_size, 3), dtype=np.uint8)

    for x in range(_grid_size):
        for y in range(_grid_size):
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
    for x in range(max(0, abs(planet_x - PLANET_RADIUS)), min(_grid_size, planet_x + PLANET_RADIUS)):
        for y in range(max(0, abs(_planet_y - PLANET_RADIUS)), min(_grid_size, _planet_y + PLANET_RADIUS)):
            dx_planet_center = abs(planet_x - x)
            dy_planet_center = abs(_planet_y - y)
            d_planet_center = math.sqrt(dx_planet_center ** 2 + dy_planet_center ** 2)

            if d_planet_center < PLANET_RADIUS:
                grid[x, y, 0] = 0
                grid[x, y, 1] = 0
                grid[x, y, 2] = 0

    return np.flip(np.swapaxes(grid, 0, 1), 0)


def worker_function(conn):
    msg = conn.recv()

    if isinstance(msg, int):
        conn.send(cut_out_planet(msg))
        worker_function(conn)
        return

    if isinstance(msg, str):
        if msg == "stop":
            return

    print("Something went wrong")


def initialize_workers(conns, processes):
    for i in range(NUMBER_OF_WORKERS):
        parent_connection, child_connection = Pipe()
        process = Process(target=worker_function, args=(child_connection,))
        processes.append(process)
        conns.append(parent_connection)
    print("Workers are initialized")


def start_workers(processes):
    for i in range(NUMBER_OF_WORKERS):
        processes[i].start()
    print("Workers have started")


def delegate_workers(conns, counter):
    start_counter = counter
    for i in range(NUMBER_OF_WORKERS):
        if counter == _grid_size:
            break
        conns[i].send(counter)
        counter += 1
    print("Frames %d until %d have been delegated" % (start_counter, counter - 1))


def collect_from_workers(conns, counter, video):
    start_counter = counter
    for i in range(NUMBER_OF_WORKERS):
        if counter == _grid_size:
            break
        video.write(conns[i].recv())
        counter += 1
    print("Frames %d until %d have been collected" % (start_counter, counter - 1))


def stop_workers(conns, processes):
    for i in range(NUMBER_OF_WORKERS):
        conns[i].send("stop")
    for i in range(NUMBER_OF_WORKERS):
        processes[i].join()
    print("Workers have been stopped")


if __name__ == '__main__':
    video = VideoWriter('./data/transit.mkv', VideoWriter_fourcc(*'X264'), 24.0, (_grid_size, _grid_size))
    counter = 0
    processes = []
    conns = []

    initialize_workers(conns, processes)
    start_workers(processes)

    while counter < _grid_size:
        delegate_workers(conns, counter)
        collect_from_workers(conns, counter, video)
        counter += NUMBER_OF_WORKERS

    stop_workers(conns, processes)

    video.release()
