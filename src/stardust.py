from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc

from config import NUMBER_OF_WORKERS
from config import _GRID_SIZE

from worker import initialize_workers
from worker import start_workers
from worker import delegate_workers
from worker import collect_from_workers
from worker import stop_workers


if __name__ == '__main__':
    video = VideoWriter('./data/transit.mkv', VideoWriter_fourcc(*'X264'), 24.0, (_GRID_SIZE, _GRID_SIZE))
    counter = 0
    processes = []
    conns = []

    initialize_workers(conns, processes)
    start_workers(processes)

    while counter < _GRID_SIZE:
        delegate_workers(conns, counter)
        collect_from_workers(conns, counter, video)
        counter += NUMBER_OF_WORKERS

    stop_workers(conns, processes)

    video.release()
