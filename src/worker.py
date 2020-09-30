from multiprocessing import Process
from multiprocessing import Pipe

from planet import take_snapshot

from config import NUMBER_OF_WORKERS
from config import IMAGE_SIZE


#
# This function is executed by the worker thread of the script.
#
# conn: The endpoint connection of the Pipe used to communicate with the main thread.
#
def worker_function(conn):
    msg = conn.recv()

    if isinstance(msg, int):
        conn.send(take_snapshot(msg))
        worker_function(conn)
        return

    if isinstance(msg, str):
        if msg == 'stop':
            return

    print('Something went wrong')


#
# This function initializes the worker threads.
#
# conns: The endpoints of the pipes to the main thread. This list is initially empty and filled by the function.
# processes: The processes created by the function are collected in this list.
#
def initialize_workers(conns, processes):
    for i in range(NUMBER_OF_WORKERS):
        parent_connection, child_connection = Pipe()
        process = Process(target=worker_function, args=(child_connection,))
        processes.append(process)
        conns.append(parent_connection)

    print('Workers are initialized')


#
# This function starts the worker threads.
#
# processes: The list of processes to be started.
#
def start_workers(processes):
    for i in range(NUMBER_OF_WORKERS):
        processes[i].start()

    print('Workers have started')


#
# This function delegates the different frames to be rendered to the worker threads.
#
# conns: The pipe connections to the workers.
# counter: The current frame to be rendered.
#
def delegate_workers(conns, counter):
    for i in range(NUMBER_OF_WORKERS):
        if counter == IMAGE_SIZE:
            break

        conns[i].send(counter)
        counter += 1


#
# This function collects the rendered images from the worker threads.
#
# conns: The pipe connections to the worker threads.
# counter: The current expected frame.
# video: The video writer used to write frames.
#
def collect_from_workers(conns, counter, video, transit):
    for i in range(NUMBER_OF_WORKERS):
        if counter == IMAGE_SIZE:
            break

        frame = conns[i].recv()
        transit[counter] = frame.mean()
        video.write(frame)
        counter += 1


#
# This function stops all the worker threads and cleans up after them.
#
# conns: The pipe connections to the threads.
# processes: The list of processes to be killed.
#
def stop_workers(conns, processes):
    for i in range(NUMBER_OF_WORKERS):
        conns[i].send('stop')

    for i in range(NUMBER_OF_WORKERS):
        processes[i].join()

    print('Workers have been stopped')
