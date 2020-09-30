import sys
import numpy as np

from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc

from config import NUMBER_OF_WORKERS
from config import VIDEO_FPS
from config import IMAGE_SIZE

from worker import initialize_workers
from worker import start_workers
from worker import delegate_workers
from worker import collect_from_workers
from worker import stop_workers


#
# This function prints a progress bar in the terminal. The progress bar needs to be manually updated
# with the current progress.
#
# progress: Value between 0.0 and 1.0 representing the progress.
#
def print_progress_bar(progress):
    fill = '█'
    length = 80
    percent = '{0:.1f}'.format(100 * progress)
    filled_length = int(length * progress)
    bar = fill * filled_length + '-' * (length - filled_length)
    print('\r|%s| %s%%' % (bar, percent), end='\r')
    if progress >= 1.0:
        print()


#
# The main function of the script. The program starts here.
#
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Invalid arguments: Usage is stardust.py name_of_directory')
        exit()

    video = VideoWriter(sys.argv[1], VideoWriter_fourcc(*'avc1'), VIDEO_FPS, (IMAGE_SIZE, IMAGE_SIZE))
    counter = 0
    processes = []
    conns = []
    transit = np.zeros(IMAGE_SIZE)

    initialize_workers(conns, processes)
    start_workers(processes)

    print()
    while counter < IMAGE_SIZE:
        delegate_workers(conns, counter)
        collect_from_workers(conns, counter, video, transit)
        counter += NUMBER_OF_WORKERS
        if counter > IMAGE_SIZE:
            counter = IMAGE_SIZE
        print_progress_bar(counter / IMAGE_SIZE)
    print()

    stop_workers(conns, processes)
    video.release()
    print('Video has been saved to %s' % sys.argv[1])
